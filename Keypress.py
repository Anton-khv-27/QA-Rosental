import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Настройки Chrome
options = Options()

# Инициализация драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

keyboard_input = ("xpath",'//input[@id="target"]')

driver.get("https://the-internet.herokuapp.com/key_presses")

time.sleep(2)

driver.find_element(*keyboard_input).send_keys("anbcjsncjsnjcnsjncl")
time.sleep(2)

driver.find_element(*keyboard_input).send_keys(Keys.CONTROL + "A")
time.sleep(2)

driver.find_element(*keyboard_input).send_keys(Keys.BACKSPACE)
time.sleep(2)