# Create a Scraper that extracts information about job descriptions
# 1. Open up website
# 2. Parse the HTML and gather content objects from the indeed page
#    - list of Job Titles
#    - list of Job Descriptions


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json
import time

with open("aggregate_job_info.json", "r") as f:
    aggregate_job_info = json.load(f)

try:
    driver_path = r"chromedriver.exe"  # Replace with your Chrome driver path
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    driver.get(r"https://www.indeed.com/jobs?q=data+science+internship&start=110&pp=gQClAAABiS3ZE3IAAAACCW0yDAAZAQATGktWR-z-gBIl3tZnH8Uv--FtKRLxTAAA") 

    # aggregate_job_info = []

    running = True
    while running:
        time.sleep(1)
            
        link_elements = driver.find_elements(By.CLASS_NAME, "jcs-JobTitle.css-jspxzf.eu4oa1w0")

        for link_element in link_elements:
            
            job_info = {}
            req_list = []
            
            link_element.click()
            time.sleep(0.5) 

            job_title_element = driver.find_element(By.CLASS_NAME, "icl-u-xs-mb--xs.icl-u-xs-mt--none.jobsearch-JobInfoHeader-title.is-embedded")
            job_info["title"] = job_title_element.text

            job_description_element = driver.find_element(By.ID, "jobDescriptionText")
            unordered_lists = job_description_element.find_elements(By.TAG_NAME, "ul")
            
            for unordered_list in unordered_lists:
                list_items = unordered_list.find_elements(By.TAG_NAME, "li")
                for list_item in list_items:
                    print(list_item.text)
                    req_list.append(list_item.text)
            job_info["reqs"] = req_list
            aggregate_job_info.append(job_info)

        # next_buttons = driver.find_elements(By.CLASS_NAME, "e8ju0x50")
        # if(len(next_buttons) == 6):
        #     running = False
        # else:
        #     next_buttons[len(next_buttons)-2].click()
except:
   pass

with open("aggregate_job_info.json", "w") as f:
    json.dump(aggregate_job_info, f)

driver.quit()
