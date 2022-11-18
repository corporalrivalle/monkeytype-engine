import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import keyboard as key
# import undetected_chromedriver as uc

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})

browser = webdriver.Chrome()
browser.get("https://monkeytype.com")
# time.sleep(5)
html = browser.page_source
try:
    myElem = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, 'words')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

# print(html)

soup = BeautifulSoup(html, features = "html.parser")
bodypart = soup.body
app = bodypart.contents[8]
centerContent = app.contents[1]
middle = centerContent.contents[1]
pagetest = middle.contents[1]
typingTest = pagetest.contents[2]
wordWrapper = typingTest.contents[7]
i=0
print("Loading contents")
print("Loading.")
while(i<=20):
    time.sleep(1)
    i+=1
    if(i%3==0):
        print("Loading.")
    elif (i%3==1):
        print("Loading..")
    elif (i%3==2):
        print("Loading...")
words = wordWrapper.contents[2]
print(words.contents[0])
newString=""
for singleWords in words.contents:
    for letters in singleWords.contents:
        newString+=letters.string
        print(letters)
    newString+=" "

print("WORDS SUCCESSFULY COUNTED")
print("-------------------------------------------------------------------")
print("READY TO GO! CLICK INTO THE TYPING BOX! ENGINE BEGINS IN 10 SECONDS")
print("-------------------------------------------------------------------")
i = 0
while i<=10:
    print(10-i)
    time.sleep(1)
    i+=1
print("LAUNCHING")
key.write(newString)

print("PROGRAM SUCCESSFUL")
print("TERMINATING IN 60 SECONDS")
time.sleep(60)