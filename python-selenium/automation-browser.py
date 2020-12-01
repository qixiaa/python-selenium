from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def read_info():
    with open("info.txt", "r") as f:
        lines = f.readlines()
        return lines


browser_link = read_info()[0].strip()
keyword = read_info()[1].strip()
context_link_text = read_info()[2].strip()

driver = webdriver.Chrome()
driver.get(browser_link)

search = driver.find_element_by_name("search_query")
search.send_keys(keyword)
search.send_keys(Keys.RETURN)


link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, context_link_text))
)
link.click()
