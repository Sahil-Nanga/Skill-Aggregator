from LinkedInScraper import LinkedInScraper

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime

start = time.time()
scraper = LinkedInScraper('Computer Science','India','Internship')
scraper.open_site()

end = time.time()

print(f"\n time take = {end-start}")
#time taken for 440 jobs - 1839 or 30 min
