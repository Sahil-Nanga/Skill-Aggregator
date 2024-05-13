import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from parsers.html_parser import Simplifier

import os
class BaseScrapper():
    def __init__(self,job_title,job_location,job_type):
        self.driver = webdriver.Firefox()
        self.job_title = job_title
        self.job_location = job_location
        self.job_type = job_type

    def open_site(self,base_url):
        self.driver.get(base_url)
        time.sleep(3)


    def store(self,val):
        with open('temp_data.txt','a',encoding="utf-8") as file:
            file.write(str(val))
        file.close()

    def close_driver(self):
        self.driver.close()
        s = Simplifier()
        s.simplify_data()
        os.remove('temp_data.txt')

