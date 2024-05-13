from selenium import webdriver
from base import BaseScrapper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
class LinkedInScraper(BaseScrapper):
    
    job_type_keys = {'Internship':'1','Entry Level':'2','Associate':'3','Mid-Senior Level':'4','Director':'5'}

    def __init__(self,job_title,job_location,job_type):
        super().__init__(job_title,job_location,job_type)

    # changes the url based on the entry fields
    def format_for_url(self):

        title = self.job_title.replace(" ","%20")
        type = self.job_type_keys[self.job_type]
        url = f"https://www.linkedin.com/jobs/search?keywords={title}&location={self.job_location}&geoId=102713980&f_TPR=&f_E={type}&position=1&pageNum=0"
        return url
    
    #opens the website with the formatted url
    def open_site(self):
        super().open_site(self.format_for_url())
        self.press_job_cards()
    
    def press_job_cards(self):
        wait = WebDriverWait(self.driver, 3.5) 
        # Finds the number of job listings available
        rows_no = int(self.driver.find_element(By.CLASS_NAME,'results-context-header__job-count').text)
        for i in range(1,rows_no+1):
            # After the 160 card a load more button must be pressed which then loads 25 more cards
            if i in range(100,rows_no+1,25):
                self.load_more()

            item_selector = f'/html/body/div[1]/div/main/section[2]/ul/li[{i}]/div' # sets the job card
            try:
                item = wait.until(EC.visibility_of_element_located((By.XPATH, item_selector)))
                item.click()
                time.sleep(2)
                base_info = self.get_metadata(item)
                base_info.append(self.get_description())
                base_info.insert(0,i)
                self.store(base_info)
                time.sleep(2)
            except TimeoutException: #Some cards are not a div, but are a link so the methods dont work on them
                continue
                
        
        self.close_driver()
    
    def get_metadata(self,item):
        # get metadata from the job card
        job_title = item.find_element(By.CLASS_NAME,'base-search-card__title').text
        company_name = item.find_element(By.CLASS_NAME,'base-search-card__subtitle').text
        location = item.find_element(By.CLASS_NAME,'job-search-card__location').text
        try:
            date_div = item.find_element(By.CLASS_NAME,'job-search-card__listdate')
            date = date_div.get_attribute('datetime')
        except NoSuchElementException:
            date = ""
        return [job_title,company_name,location,date]
    
    def get_description(self): 
        try:      
            description = self.driver.find_element(By.XPATH, "//div[@class='description__text description__text--rich']")
            html = description.text # gets the html of the description
            if len(html)==0:
                return description.get_attribute('innerHTML')

            return html.lower()
        except NoSuchElementException:
            self.driver.refresh()
            self.get_description()

    def load_more(self):
        try:
            button = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/main/section[2]/button')
            try:
                WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'infinite-scroller__show-more-button')))
                button.click()
            except TimeoutException:return
        except NoSuchElementException:
            return
        

