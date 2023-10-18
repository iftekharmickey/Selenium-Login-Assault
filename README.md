# Selenium-Login-Assault

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-3.141.0-green)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Author](#author)

---

## Overview

The Selenium-Login-Assault is a Python script that automates the process of attempting logins with provided username and password lists on a target website using the Selenium web automation framework. This tool is designed for educational and research purposes and should not be used for any malicious activities.

---

## Features

- Easy customization for different websites using Selenium.
- Supports reading usernames and passwords from external files.
- Can detect successful logins and provide the credentials used.
- Utilizes explicit waits for improved reliability.

---

## Getting Started

### Prerequisites

Before using this script, ensure that you have met the following requirements:

- Python 3.8 or higher.
- Selenium 3.141.0 or a compatible version.
- Chrome web driver (for Chrome) or the appropriate driver for your browser.
- The required Python packages, which can be installed using `pip install selenium`.

### Installation

1. Clone the repository to your local machine:

   ```python
   git clone https://github.com/iftekharmickey/Selenium-Login-Assault.git

2. Install the required Python packages:

   ```python
   pip install -r requirements.txt

---

## Usage

1. Edit the configuration variables in the script to suit your testing needs. These variables include:

   - `WAIT_TIME`: Adjust this value to change the waiting time for elements (e.g., `WAIT_TIME = 10`).
   - `URL`: The URL of the login page you want to target (e.g., `URL = 'https://example.com/login'`).
   - `USERNAME_FILE`: The file containing a list of usernames to test (e.g., `USERNAME_FILE = 'usernames.txt'`).
   - `PASSWORD_FILE`: The file containing a list of passwords to test (e.g., `PASSWORD_FILE = 'passwords.txt'`).

2. Customize the element locators in the script to match your specific website. In the script, you'll find lines like:

   ```python
   username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
   password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
   login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'btn-outline-primary') and contains(@class, 'm-2')]"))
   ```

   Update the `By.ID` and `By.XPATH` elements to match the HTML structure of your login page. By customizing these elements, you ensure that the script interacts correctly with your website's login page.

3. Additionally, be prepared to handle website-specific error prompts in the script to ensure accurate detection of login outcomes.

   For example, if your website displays "No Record Found" or "Credential Mismatched" as error messages upon failed login attempts, you can customize the script to check for these messages and log the corresponding outcomes.

   Here's a simple example of handling "No Record Found" and "Credential Mismatched" prompts in the script:

   ```python
   if "No Record Found" in driver.page_source:
       logger.info("Login Failed: No Record Found")
   elif "Credential Mismatched" in driver.page_source:
       logger.info("Login Failed: Credential Mismatched")
   else:
       logger.info("Successful Login")
   ```
   
4. Run the script:

   ```python
   python login_scraper.py
   ```

   Please make sure you have the appropriate web driver installed for your selected browser.

6. The script will prompt you for the URL of the login page, username list, and password list.

7. The script will automate login attempts using the provided username and password lists. If it successfully logs in, it will display the combination of the correct username and password.

---

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/iftekharmickey/Selenium-Login-Assault/blob/main/LICENSE) file for details.

---

## Disclaimer

This script is provided for educational and research purposes. Please use this tool responsibly and only for legal and ethical purposes. Unauthorized or malicious use of this script may violate the law and is not endorsed or supported.

The author of this script is not responsible for any misuse of this tool. Users are solely responsible for their actions, and they should adhere to the laws and regulations of their respective jurisdictions.

---

## Author

This tool was developed by Iftekhar Tahir.

Enjoy using the Selenium-Login-Assault! For questions, issues, or feedback, don't hesitate to contact me at iftekhar.tahir@proton.me.
