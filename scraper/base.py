import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
#from parsers.html_parser import Simplifier
import sqlite3
from datetime import datetime
import os
class BaseScrapper():
    def __init__(self,job_title,job_location,job_type):
        self.driver = webdriver.Firefox()
        self.job_title = job_title
        self.job_location = job_location
        self.job_type = job_type
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()
        self.current_time = datetime.now()
        self.month_date =self.current_time.strftime("%m%d")

    def open_site(self,base_url):
        self.driver.get(base_url)
        time.sleep(3)


    def store(self,val):
       #stores the data in a database
       #[job_title,company_name,location,date,link,desc]
       val.append(None)
       sql = "INSERT INTO job_Data (id,title,company,location,postdate,link,description,field) VALUES (?,?,?,?,?,?,?,?)"
       self.cursor.execute(sql,val)
       self.conn.commit()
       
    def close_driver(self):
        self.cursor.close()
        self.driver.close()
        #s = Simplifier()
        #s.simplify_data()
        #os.remove('temp_data.txt')

    def check_if_present(self,title,company):
        self.cursor.execute("SELECT * FROM job_Data WHERE title=? AND company = ?", (title,company))
        result = self.cursor.fetchall()
        if not result:
            return False
        else:
            return True