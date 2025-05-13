from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from unidecode import unidecode
import string
from generate import Email, Password, Username,  Name, Birthday, Gender

firstname = Name().generate_firstname()
lastname = Name().generate_lastname()

print(firstname, lastname)

# Generate a random number
random_number = random.randint(1000, 9999)

username = Username().generate()
birthday =  Birthday().generate() #dd mm yyyy exp : 24 11 2003
gender = Gender().generate(firstname) # 1:F 2:M 3:Not say 4:Custom
password = Password().generate()

service = webdriver.ChromeService(executable_path = r"./geckodriver.exe")
driver = webdriver.Chrome(service=service)

    
driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

time.sleep(3)
# Fill in name fields
first_name = driver.find_element(By.NAME, "firstName")
last_name = driver.find_element(By.NAME, "lastName")
first_name.clear()
first_name.send_keys(firstname)
last_name.clear()
last_name.send_keys(lastname)
next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
next_button.click()

time.sleep(1)

# Wait for birthday fields to be visible
wait = WebDriverWait(driver, 20)
day = wait.until(EC.visibility_of_element_located((By.NAME, "day")))

# Fill in birthday
birthday_elements = birthday.split()
month_dropdown = Select(driver.find_element(By.ID, "month"))
month_dropdown.select_by_value(birthday_elements[1])
day_field = driver.find_element(By.ID, "day")
day_field.clear()
day_field.send_keys(birthday_elements[0])
year_field = driver.find_element(By.ID, "year")
year_field.clear()
year_field.send_keys(birthday_elements[2])

# Select gender
gender_dropdown = Select(driver.find_element(By.ID, "gender"))
gender_dropdown.select_by_value(gender)
next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
next_button.click()
        
# Create custom email
time.sleep(2)
if driver.find_elements(By.ID, "selectionc4") :
    create_own_option = wait.until(EC.element_to_be_clickable((By.ID,"selectionc4") ))
    create_own_option.click()
        
create_own_email = wait.until(EC.element_to_be_clickable((By.NAME, "Username")))
username_field = driver.find_element(By.NAME, "Username")
username_field.clear()
username_field.send_keys(username)
next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
next_button.click()
        
# Enter and confirm password
password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
password_field.clear()
password_field.send_keys(password)
# Locate the parent div element with the ID "confirm-passwd"
confirm_passwd_div = driver.find_element(By.ID, "confirm-passwd")
 #Find the input field inside the parent div
password_confirmation_field = confirm_passwd_div.find_element(By.NAME, "PasswdAgain")
password_confirmation_field.clear()
password_confirmation_field.send_keys(password)
next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
next_button.click()

# Skip phone number and recovery email steps
skip_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
for button in skip_buttons:
    button.click()

# Agree to terms
agree_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
agree_button.click()

print(f"Your Gmail successfully created:\n{{\ngmail: {username}@gmail.com\npassword: {password}\n}}")

    # except Exception as e:
    #     print("Failed to create your Gmail, Sorry")
    #     print(e)
    # finally:
    #     driver.quit()

# Execute the function to fill out the form
#fill_form(driver)
