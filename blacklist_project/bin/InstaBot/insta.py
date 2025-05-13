import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Set the new path where geckodriver.exe is located
firefox_path = r"./geckodriver.exe"
service = Service(executable_path=firefox_path)

# Initialize Firefox WebDriver with the new path
driver = webdriver.Firefox(service=service)

try:
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)

    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys("issamabenlabin")

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("NHL789ch!")
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)

    post_url = "https://www.instagram.com/p/DBrp5DZvQOy/?img_index=1"
    driver.get(post_url)
    time.sleep(3)

    comments = responses = [
        "1",
        "I will vote for number 1",
        "1 is top-notch!",
        "Number 1 all the way!",
        "Definitely going with 1!",
        "No contest, it's 1!",
        "1 is the best choice!",
        "All votes to number 1!",
        "Without a doubt, it's 1!",
        "1 stands out!",
        "You can't go wrong with 1!",
        "1 has my vote!",
        "1 is the clear winner!",
        "I fully support number 1!",
        "Team 1 for sure!",
        "1 is simply unbeatable!",
        "1 deserves to win!",
        "Let's rally behind 1!",
        "1 shines above the rest!",
        "I endorse number 1!",
        "Count me in for 1!",
        "1 is the people's choice!"
]

    for i in range (20):
        attempts = 3  # Number of retry attempts in case of a stale element exception
        for attempt in range(attempts):
            try:
                # Locate the comment box with WebDriverWait
                comment_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[aria-label="Add a comment…"]'))
                )
                # Click on the comment box and send a comment
                comment_box.click()
                random_comment = random.choice(comments)
                comment_box.send_keys(random_comment)
                time.sleep(1)

                # Submit the comment
                comment_box.send_keys(Keys.RETURN)
                time.sleep(2)
                break  # Exit the loop if successful
            except selenium.common.exceptions.StaleElementReferenceException:
                if attempt == attempts - 1:
                    print("Failed to locate the comment box after multiple attempts.")
                else:
                    print("Encountered a stale element, retrying...")

finally:
    driver.quit()
