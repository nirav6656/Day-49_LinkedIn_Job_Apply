from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3901037376&f_AL=true&f_E=2&geoId=101174742&keywords=python%20developer&location=Canada&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

click_sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]").click()

time.sleep(2)

enter_username = driver.find_element(By.ID, "username").send_keys(USERNAME)
enter_password = driver.find_element(By.ID, "password").send_keys(PASSWORD)

time.sleep(2)
final_sign_in = driver.find_element(By.CLASS_NAME, "btn__primary--large").click()
time.sleep(2)

click_easy_apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button").click()