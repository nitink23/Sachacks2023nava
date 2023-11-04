from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re


def cleanResume(resumeText):
    resumeText = re.sub('http\S+\s*', ' ', resumeText)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
    resumeText = re.sub('#\S+', '', resumeText)  # remove hashtags
    resumeText = re.sub('@\S+', '  ', resumeText)  # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""!"$%&'()*,-./:;<=>?@[\]^_`{|}~"""), ' ', resumeText)  # remove punctuations
    resumeText = re.sub(r'[^\x00-\x7f]',r' ', resumeText) 
    resumeText = re.sub('\s+', ' ', resumeText)  # remove extra whitespace
    return resumeText

driver_path = r"chromedriver.exe"  # Replace with your Chrome driver path
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get(r"https://www.livecareer.com/resume-search/search?jt=software+engineer&pg=1") 

time.sleep(1)
            
df = pd.DataFrame(columns=["Job Role", "Job Field", "Resume"])

running = True


try:
    while running:

        link_elements = driver.find_elements(By.CLASS_NAME, "sc-1dzblrg-0.fEqilq.sc-1os65za-2.jhoVRR")
        
        for link_element in link_elements:
            # driver.execute_script("arguments[0].scrollIntoView(true);", link_element)  # Scroll to the element
            driver.execute_script("var element = arguments[0];var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);var elementTop = element.getBoundingClientRect().top;window.scrollBy(0, elementTop - (viewPortHeight / 2));", link_element)
            time.sleep(0.5)
            link_element.click()
            time.sleep(2) 

            driver.switch_to.window(driver.window_handles[1])
            
            wait = WebDriverWait(driver, 10)
            resume_element = driver.find_element(By.CLASS_NAME, "document")
            resume_content = resume_element.text
            cleaned_resume_content = cleanResume(resume_content)
            print(cleaned_resume_content)
            # Add scraped resume to DataFrame
            df = df.append({"Job Role": "Software Engineering", "Job Field": "Engineering", "Resume": cleaned_resume_content}, ignore_index=True)


            driver.close()

            driver.switch_to.window(driver.window_handles[0])

        next_buttons = driver.find_elements(By.CLASS_NAME, "sc-19xfkc1-0.lmkNDx")
        print(len(next_buttons))
        if(len(next_buttons) != 2):
            running = False
        else: 
            driver.execute_script("var element = arguments[0];var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);var elementTop = element.getBoundingClientRect().top;window.scrollBy(0, elementTop - (viewPortHeight / 2));", next_buttons[0])
            next_buttons[0].click()
except:
    pass

df.to_csv("resume_data.csv", index=False)

driver.quit()


