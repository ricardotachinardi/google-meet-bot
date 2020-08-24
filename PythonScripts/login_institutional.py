from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pause
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException

def institutional_sign_in():

    options = webdriver.ChromeOptions()

    options.add_argument("--no-sandbox")
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument("--user-data-dir=selenium") 
    options.add_argument("start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("useAutomationExtension", False)

    browser = webdriver.Chrome(options=options)

    browser.get('https://accounts.google.com/signin/v2/identifier?service=accountsettings&hl=pt-BR&continue=https%3A%2F%2Fmyaccount.google.com%2Fintro%3Fhl%3Dpt-BR&flowName=GlifWebSignIn&flowEntry=ServiceLogin')



print("We will open an browser window for you to login on your google services using an institutional account")
print('Come back here after logging in to your account')

pause.time(5)

institutional_sign_in()

input("Press enter after you have succesfully logged in your acount")

print()
print("Succesfully logged in, you can now use the scheduler")
