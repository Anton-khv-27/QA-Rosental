from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import csv
from dotenv import load_dotenv

# Настройка драйвера (для Chrome)
driver = webdriver.Chrome()
driver.maximize_window()
load_dotenv()

# Переход на сайт
driver.get("https://test.rozentalgroup.ru/demo/authorization/")

# Ожидание загрузки поля логина
wait = WebDriverWait(driver, 10)
username_input = wait.until(EC.presence_of_element_located((By.NAME, "login")))
password_input = driver.find_element(By.NAME, "password")

# Вводим логин и пароль
username_input.send_keys(os.environ["login"])  # Вставь свои данные
password_input.send_keys(os.environ["password"])  # Вставь свои данные

# Нажимаем кнопку входа
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Ждём редиректа/результата
wait.until(EC.url_changes("https://test.rozentalgroup.ru/demo/authorization/"))
time.sleep(5)
driver.get("https://test.rozentalgroup.ru/demo/dispetcher/debtors/")

# Шаг 3. Ждём обновления таблицы
time.sleep(3)

# Найти поле поиска и ввести запрос
search_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Поиск..."]')))
time.sleep(5)
search_input.clear()
search_input.send_keys("санитарная")
search_input.send_keys(Keys.RETURN)
time.sleep(2)

# Ждём появления таблицы с результатами
table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table tbody tr")))

# Сохраняем строки таблицы в список
results = []
for row in table_rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = [cell.text for cell in cells]
    results.append(row_data)

# Сохраняем в CSV-файл
with open("таблица_результатов.csv", "w", newline='', encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    for row in results:
        writer.writerow(row)

print("✅ Данные сохранены в файл 'таблица_результатов.csv'")

# Не закрываем сразу, чтобы увидеть результат
input("Нажмите Enter для выхода...")

driver.quit()