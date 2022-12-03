from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common import keys
import requests
import urllib3
import urllib


import time
import pandas
driver = webdriver.Chrome()
driver.get("https://senf.ir")
driver.find_element('id',"HyperLink1").click()
wait = WebDriverWait(driver,10)
username1 = wait.until(Ec.element_to_be_clickable((By.ID,'Login1_txtUserName')))
username1.send_keys('09132914263')
password1 = wait.until(Ec.element_to_be_clickable((By.ID,'Login1_txtPassword')))
password1.send_keys('091329142631447')
login=  wait.until(Ec.element_to_be_clickable((By.ID,'Login1_btnEnter'))).click()
time.sleep(3)
driver.get("https://senf.ir/ListCompany/199/%D8%B1%D9%81%D8%B3%D9%86%D8%AC%D8%A7%D9%86")
alltitles = []
alladdress = []
allphones = []
allgroups = []
allsubgroups = []
allmanagers = []
allmobiles = []
allemails =[]
numbers =[]
alldescription = []
for j in range(0,5):
    for i in range(0,20):
        link = wait.until(Ec.element_to_be_clickable((By.ID,'ContentPlaceHolder2_grdProduct_HpCompany_'+str(i))))
        url=link.get_attribute('href')
        driver.execute_script('window.open()')
        driver.switch_to.window(driver.window_handles[1])
        driver.get(url)
        try:
            address = wait.until(Ec.element_to_be_clickable((By.ID,'ContentPlaceHolder2_txtAddress')))
        except:
            address = ''
        alladdress.append(address.text)
        group = wait.until(Ec.element_to_be_clickable((By.ID,'ContentPlaceHolder2_rpParent_lblheaderCheild_2')))
        allgroups.append(group.text)
        subgroup = wait.until(Ec.element_to_be_clickable((By.ID,'ContentPlaceHolder2_rpParent_lblheaderCheild_3')))
        allsubgroups.append(subgroup.text)
        try:
            manager = wait.until(Ec.element_to_be_clickable((By.ID,'ContentPlaceHolder2_LblManager'))).text
        except:
            manager=''
        allmanagers.append(manager)
        title =  wait.until(Ec.element_to_be_clickable((By.ID,'ContentPlaceHolder2_hflink')))
        alltitles.append(title.text)
        numbers.append(j * 10 + i)
        print(j * 10 + i)
        try:
            phone = wait.until(Ec.element_to_be_clickable((By.ID,'ContentPlaceHolder2_ImgTell'))).get_attribute('src')

            # with requests.get(phone,stream=true) as r:
            #     with open('pics/' + str(j * 10 + i) + 'phone.jpg', 'wb') as f:
            #         for data in r.iter_content(1024):
            #             f.write(data)
            urllib.request.urlretrieve(phone,'pics/' + str(j * 10 + i) + 'phone.jpg')
        except:
            phone=''
        allphones.append(phone)
        try:
            mobile=wait.until(Ec.element_to_be_clickable((By.ID,'ContentPlaceHolder2_ImgMobil'))).get_attribute('src')

            # with requests.get(mobile,stream=true) as r:
            #     with open('pics/'+str(j*10+i)+'mobile.jpg','wb') as f:
            #         for data in r.iter_content(1024):
            #             f.write(data)
            urllib.request.urlretrieve(mobile, 'pics/' + str(j * 10 + i) + 'mobile.jpg')
        except:
            mobile=''
        allmobiles.append(mobile)
        try:
            email =wait.until(Ec.element_to_be_clickable((By.ID,'ContentPlaceHolder2_ImgEmail'))).get_attribute('src')
            urllib.request.urlretrieve(email,'pics/'+str(j*10+i)+'email.jpg')
        except:
            email =''
        allemails.append(email)
        try:
            description = wait.until(Ec.element_to_be_clickable((By.ID,'ContentPlaceHolder2_lblDesc'))).text
        except:
            description =''
        alldescription.append(description)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    btn_next =wait.until(Ec.element_to_be_clickable((By.ID,'ContentPlaceHolder2_rptPager_lnkPage_12'))).click()
# for addr in alladdress:
#     print(addr)
job = {'number':numbers, 'title':alltitles,
       'address':alladdress,'group':allgroups,
       'subgroup':allsubgroups,'manager':allmanagers,
       'phone':allphones,'mobile':allmobiles,
       'email':allemails,'description':alldescription}
data = pandas.DataFrame.from_dict(job,orient='index')
data = data.transpose()
writer = pandas.ExcelWriter('jobs.xlsx')
data.to_excel(writer)
writer.save()