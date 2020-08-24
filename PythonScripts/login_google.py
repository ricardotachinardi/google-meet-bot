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

def google_sign_in(email, password, internet):

    if internet == 'n':
        extratime = 7
    else:
        extratime = 0

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

    browser.get('https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3A7df599f842c1c0ce%2C10%3A1598275142%2C16%3A711b928803291f44%2Cd0c138b07c19d9d5eb84f1bd1b19ab2404b4db091a4bb6270fb887a665114b3d%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22a0b44e88bafc415789def65b91b12e3e%22%7D&response_type=code&hl=en&flowName=GeneralOAuthFlow')

    time.sleep(3+extratime)

    browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email+Keys.ENTER)

    browser.implicitly_wait(10)
    time.sleep(extratime)

    browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password+Keys.ENTER)


    browser.implicitly_wait(1)
    browser.close()




email = input("Email: ")

passe = input("Password: ")

internet = input("Your internet connection is fast? (y/n): ").lower()
while internet != ('y' or 'n'):
    internet = input("Your internet connection is fast? type 'y' for yes or 'n' for no: ").lower()

print("We will open an browser window to login on your google account using the StackOverflow API")
print("Please sit down and watch while our bot works, it should take less than 60 seconds")

pause.sleep(5)

google_sign_in(email, passe, internet)

print()
print("Succesfully logged in, you can now use the scheduler")