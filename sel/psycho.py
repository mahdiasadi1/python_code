from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
# driver=webdriver.chrome()
driver = webdriver.Chrome()

driver.get("http://google.com")
wait=WebDriverWait(driver,50)
btn1=wait.until(Ec.element_to_be_clickable((By.NAME,'q')))
btn1.send_keys("تست روانشناسی"+Keys.ENTER)
btn2 = wait.until(Ec.element_to_be_clickable((By.XPATH,'//a[@href="https://esanj.ir/tag/psychology-test"]'))).click()
btn3 = wait.until(Ec.element_to_be_clickable((By.CSS_SELECTOR,"#first-test > div > div.col-lg-9.col-md-9.col-sm-9 > h3 > a"))).click()
btn4 = wait.until(Ec.element_to_be_clickable((By.CSS_SELECTOR,'body > section.container-fluid.container-fluid-detilsPage > div > div:nth-child(6) > div.col-md-4.sidebar > a.bubbly-button.button.startTest'))).click()
btn5 = wait.until(Ec.element_to_be_clickable((By.NAME,'sex')))
drop1 = Select(btn5)
drop1.select_by_value("male")
btn6 = wait.until(Ec.element_to_be_clickable((By.NAME,'year_birth')))
drop2 = Select(btn6).select_by_value("1360")
btn7 = wait.until(Ec.element_to_be_clickable((By.XPATH,"/html/body/section[2]/div/div/div/div/div[1]/div/form/button"))).click()
i=1
while i<=88:
   if i%2==0:
       btn8 = wait.until(Ec.element_to_be_clickable((By.CSS_SELECTOR,'label[for="answer-2"]'))).click()
   else:
       btn8 = wait.until(Ec.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="answer-1"]'))).click()
   i+=1
   btn9 = wait.until(Ec.element_to_be_clickable((By.CSS_SELECTOR,'body > div > div > div.box-footer > button.b-btn.btn-d-next.display-none'))).click
btn10 = wait.until(Ec.element_to_be_clickable((By.XPATH,'/html/body/div/div/div[4]/button[4]'))).click()










