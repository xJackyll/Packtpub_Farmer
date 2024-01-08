# PacktPub_FreeLearning.pyw
#
# Creation Date: 19/02/2023
# Last Modified: 09/27/2023
# Version: 2.0
# Author: xJackyll
#
# This script, reading a text file, redeems the book of the day for each specified account.
# Warning: captcha are not supported by this script.
#
# N.B. Do not modify the script unless you are clear about what you are doing.


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
import os

# --------------------------------------------------------------------------------------------------

# Change these variables if not running
Accounts_Path = "accounts.txt"
ChromeUser_Dir = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data', 'Default') # This is an exmple, put your own Chrome User Profile
log_Path = "Packtpub.log"


# --------------------------------------------------------------------------------------------------

# LOG FUNCTION

def log_info(message):
    logging.info(message)


def log_warning(message):
    logging.warning(message)


def log_error(message):
    logging.error(message)

# --------------------------------------------------------------------------------------------------


# READING CREDENTIAL FUNCTION
def read_users():
    with open(Accounts_Path) as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        username = lines[i].strip()
        i += 1
        password = lines[i].strip()
        i += 1
        i += 1  # Skip the third line
        # Yield the usernames and passwords
        yield username, password

# --------------------------------------------------------------------------------------------------


# FUNZIONE DI RICHIESTA WEB
def WebRequest(XPATH, Key = Keys.ENTER):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, XPATH))).send_keys(Key)

# --------------------------------------------------------------------------------------------------

# LOG SETUP

# Set the logging level to display info, warning and error
logging.basicConfig(level=logging.INFO)

errors = 0

# Create a log file and set the format of the log message.
log_file = os.path.join(log_Path)
file_handler = logging.FileHandler(log_file)
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logging.getLogger().addHandler(file_handler)

# --------------------------------------------------------------------------------------------------

# SETUP CHROME WITH SELENIUM
# setup selenium options (using a default user, don't opening Chrome window tabs etc...)

# Warning: sometimes a captcha appears and break the code.
# if you comment out the headless argument line you can manually do the captcha.
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=" + ChromeUser_Dir)
#options.add_argument('--headless=new')
options.add_argument("--disable-gpu")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# --------------------------------------------------------------------------------------------------

# SCRIPT START

# Opening Chrome
log_info("Opening Chrome... ")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
log_info("Chrome opened with Custom Option")

# For each user it redeems the daily book

for user, passwd in read_users():
    time.sleep(5)
    log_info("USER: " + user)
    log_info("PackPub Default Page")
    driver.get("https://www.packtpub.com/free-learning")

    try:

        # Check that the login button exists, if it is not found it is assumed that we are already authenticated.
        try:
            log_info("Login attempt... ")
            time.sleep(3)
            #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/header/div/div[2]/div/div[2]/div[1]/form/div[5]/div/div[2]/a/button"))).click()
            WebRequest('/html/body/div[1]/div/main/header/div/div[2]/div/div[2]/div[1]/form/div[5]/div/div[2]/a/button')

            # Immetto le credenziali di accesso nella pagina di login
            log_info('Login page reached!')
            log_info("Input the credentials")
            time.sleep(3)
            WebRequest('/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[1]/div[1]/input', user)
            WebRequest('/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[1]/div[2]/input', passwd)
            WebRequest('/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[1]/div[2]/input')   

        except:
            log_info("Already authenticated")

        # Clicking the Redeem Button
        time.sleep(3)
        WebRequest("/html/body/div[1]/div/main/header/div/div[2]/div/div/div/div[2]/button")
        log_info("Book redeemed!")
        # WebRequest("/html/body/div[1]/div/div[2]/nav/div[4]/a[3]")
        driver.get("https://subscription.packtpub.com/logout")
        log_info("Logout... ")

    except:
        log_error("Error!!! Account: " + user)


driver.quit()
log_info("The script ended with %d errors." % errors)
