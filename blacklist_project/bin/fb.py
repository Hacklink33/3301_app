from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import random
import time

from generate import Email, Password, Name, Birthday, Username, Gender

service = webdriver.ChromeService(executable_path = r"./geckodriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.facebook.com/r.php?next=https%3A%2F%2Fwww.facebook.com%2F&locale=en_GB&display=page")

time.sleep(3)

first_name = driver.find_element(By.NAME, "firstname")
last_name = driver.find_element(By.NAME, "lastname")
first_name.clear()
first_name.send_keys(random.choice('firstname'))
last_name.clear()
last_name.send_keys(random.choice('lastname'))

email = driver.find_element(By.NAME, 'reg_email__')
email.clear()
email.send_keys('email@gmail.com')

password = driver.find_element(By.NAME, 'reg_passwd__')
password.clear()
password.send_keys("password121289347123%)_")

dropdown = Select(driver.find_element('id', "day"))
dropdown.select_by_value("8")
dropdown = Select(driver.find_element('id', "month"))
dropdown.select_by_value("5")
dropdown = Select(driver.find_element('id', "year"))
dropdown.select_by_value("1999")
verification = driver.find_element(By.NAME, 'reg_email_confirmation__')
verification.send_keys("email@gmail.com")

time.sleep(1)

random_num = random.randint(0, 2)
radio_button_values = {
    1: "Male",
    2: "Female",
    3: "Custom"
}
sex = driver.find_element(By.XPATH, f"//*[contains(text(), '{radio_button_values[1]}')]")
sex.click()

time.sleep(1)

sign_up = driver.find_element(By.NAME, 'websubmit')
sign_up.click()

time.sleep(60)



