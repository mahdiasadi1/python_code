from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
# import time
driver = webdriver.Chrome()
# driver.implicitly_wait(5)
driver.get("http://google.com")
btn1 =WebDriverWait(driver,10).until(Ec.element_to_be_clickable((By.NAME,'q')))

# btn1= driver.find_element('name','q')
btn1.send_keys('python')
# time.sleep(5)
btn2 = WebDriverWait(driver,10).until(Ec.element_to_be_clickable((By.NAME,'btnK')))
# btn2 = driver.find_element('name','btnK')
btn2.click()
# btn3 = driver.find_element('xpath','//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a').click()
# btn3 = driver.find_element('xpath','//a[@href="https://www.python.org/"]').click()
btn3 = driver.find_element_by_css_selector('a[href="https://www.python.org/"]').click()
# btn3 = driver.find_element_by_css_selector('#rso > div:nth-child(1) > div > div > div > div > div > div.yuRUbf > a').click()


# driver.close()