from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com/")
driver.execute_script('window.open()')
driver.switch_to.window(driver.window_handles[1])
# driver.get()
#open tab
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
# You can use (Keys.CONTROL + 't') on other OSs
time.sleep(3)
# Load a page
driver.get('http://stackoverflow.com/')
# Make the tests...

# close the tab
# (Keys.CONTROL + 'w') on other OSs.
driver.close()


driver.close()