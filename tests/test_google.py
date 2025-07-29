from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
