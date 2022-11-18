from selenium import webdriver
import time
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})

browser = webdriver.Chrome()
browser.get("https://monkeytype.com")
html = browser.page_source
time.sleep(2)

soup = BeautifulSoup(html,features="html.parser")
a = soup.find("div", id="words")
b = soup.find_all("div",class_="word")
print(len(list(b)))
for classes in list(a.children):
    print("Classes:",classes)
# if len(a)==0:
#     print("failed")

time.sleep(30)