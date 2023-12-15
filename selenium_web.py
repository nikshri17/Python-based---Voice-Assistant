import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # TASK performing main fxn
    def get_info(self,query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element(By.XPATH,'//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(By.XPATH,'//*[@id="search-form"]/fieldset/button')
        enter.click()
        time.sleep(5000)
        
