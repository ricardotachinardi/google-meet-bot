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



def runbot(url, year, month, day, hour, minutes, session_length = 3600):

  pause.until(datetime(year, month, day, hour, minutes))
  print("starting meeting with the url: " + url)

  options = webdriver.ChromeOptions()
  options.add_argument("user-data-dir=selenium") 
  options.add_argument("--disable-infobars")
  options.add_argument("--window-size=800,600")

  options.add_experimental_option("prefs", { \
      "profile.default_content_setting_values.media_stream_mic": 2,     # 1:allow, 2:block
      "profile.default_content_setting_values.media_stream_camera": 2,
       "profile.default_content_setting_values.notifications": 2
    })
  browser = webdriver.Chrome(options=options)

  browser.get(url)

  time.sleep(10)
  
  element = browser.find_element_by_class_name('CwaK9')
  browser.execute_script("arguments[0].click();", element)
  
  try:
    browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Join now' )]").click()
  except NoSuchElementException:
    try:
      browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Ask to join')]").click()
    except NoSuchElementException:
      try:
        browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Participar agora')]").click()
      except NoSuchElementException:
        browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Pedir para participar')]").click()
  
  time.sleep(session_length)
  print("closing meeting with the url: " + url)
  browser.close()

url = input("meet url: ").lower
print("DO NOT PUT ZEROS BEFORE THE NUMBERS")
year = int(input("year: "))
month = int(input("month: "))
day = int(input("day: "))
hour = int(input("start hour: "))
minutes = int(input("start minutes: "))
session_length = int(input("session lenght: "))

print("We will open an browser window at the start time of your session")

runbot(url, year, month, day, hour, minutes)