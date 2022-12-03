from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as Ec
drive = webdriver.Chrome()
drive.get("https://quotes.toscrape.com/scroll")
drive.maximize_window()
initheight = drive.execute_script("return document.body.scrollHeight")
drive.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)
maxh = drive.execute_script("return document.body.scrollHeight")
print(str(maxh), ' ' ,str(initheight))
while maxh > initheight:
    initheight = maxh
    drive.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    maxh = drive.execute_script("return document.body.scrollHeight")

# print(str(maxh), ' ' ,str(initheight))
alltexts =[]
texts = drive.find_elements_by_css_selector('span.text')
for text in texts:
    alltexts.append(text.text)
for t in alltexts:
    print(t)



