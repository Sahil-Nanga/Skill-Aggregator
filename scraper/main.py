from LinkedInScraper import LinkedInScraper
import time

start = time.time()
scraper = LinkedInScraper('Computer Science','India','Internship')
scraper.open_site()

end = time.time()

print(f"\n time take = {end-start}")
#time taken for 440 jobs - 1839 or 30 min