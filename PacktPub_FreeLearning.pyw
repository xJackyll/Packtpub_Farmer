# PacktPub_FreeLearning.pyw
#
# Data Creazione: 19/02/2023
# Ultima Modifica: 27/09/2023
# Versione: 2.0
# Autore: xJackyll
#
# Questo script, leggendo un file di testo, riscatta il libro del giorno per ogni account specificato.
# Attenzione: i captcha non sono supportati da questo script.
#
# N.B.  Non modificare lo script se non si ha chiaro cosa si sta facendo


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

# Change this variables if not running
Accounts_Path = "accounts.txt"
ChromeUser_Dir = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data', 'Default') # This is an exmple, put your own Chrome User Profile
log_Path = "Packtpub.log"


# --------------------------------------------------------------------------------------------------

# FUNZIONI DI LOG

def log_info(message):
    logging.info(message)


def log_warning(message):
    logging.warning(message)


def log_error(message):
    logging.error(message)

# --------------------------------------------------------------------------------------------------

# FUNZIONE DI LETTURA USERNAME E PASSWORDS

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

# SETUP LOG

# Imposta il livello di log per visualizzare info, warning ed error
logging.basicConfig(level=logging.INFO)

errori = 0

# Crea un file di log e imposta il formato del messaggio di log
log_file = os.path.join(log_Path)
file_handler = logging.FileHandler(log_file)
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logging.getLogger().addHandler(file_handler)

# --------------------------------------------------------------------------------------------------

# SETUP CHROME CON SELENIUM

# SETUP CHROME CON SELENIUM
# setup opzioni selenium (uso un default user, non apro la finestra di chrome etc...)
# Warning: sometimes a captcha appears and break the code. if you comment out the headless argument line you can manually do the captcha.
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=" + ChromeUser_Dir)
options.add_argument('--headless=new')
options.add_argument("--disable-gpu")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# --------------------------------------------------------------------------------------------------

# INIZIO EFFETTIVO DELLO SCRIPT

# Apro Chrome
log_info("Apro Chrome")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
log_info("Chrome aperto con le Custom Option")

# Per ogni utente riscatto il libro

for user, passwd in read_users():
    time.sleep(5)
    log_info("USER: " + user)
    log_info("Pagina di default di Packtpub")
    driver.get("https://www.packtpub.com/free-learning")

    try:

        #  Controllo che esista il bottone di sign in, se non lo trovo sul sito assumo che siamo gia' autenticati
        try:
            log_info("Tentivo di accedere alla pagina di login")
            time.sleep(3)
            #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/header/div/div[2]/div/div[2]/div[1]/form/div[5]/div/div[2]/a/button"))).click()
            WebRequest('/html/body/div[1]/div/main/header/div/div[2]/div/div[2]/div[1]/form/div[5]/div/div[2]/a/button')

            # Immetto le credenziali di accesso nella pagina di login
            log_info('Pagina di login raggiunta!')
            log_info("Immetto email e pw...")
            time.sleep(3)
            WebRequest('/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[1]/div[1]/input', user)
            WebRequest('/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[1]/div[2]/input', passwd)
            WebRequest('/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[1]/div[2]/input')   

        except:
            log_info("siamo gia' autenticati")

        # Bottone di riscatto del libro
        time.sleep(3)
        WebRequest("/html/body/div[1]/div/main/header/div/div[2]/div/div/div/div[2]/button")
        log_info("Libro riscattato!")
        #WebRequest("/html/body/div[1]/div/div[2]/nav/div[4]/a[3]")
        driver.get("https://subscription.packtpub.com/logout")
        log_info("Logout dell'account eseguito")

    except:
        log_error("c'e' stato un errore!!! Account: " + user)


driver.quit()
log_info("Lo script e' terminato con %d errori." % errori)
