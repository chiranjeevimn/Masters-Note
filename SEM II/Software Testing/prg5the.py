import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

a = Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=a)

driver.get("https://jqueryui.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Datepicker']").click()

driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
year="2025"
month="August"
date="15"


while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mon==month and yr==year:
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody//tr//td//a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break
time.sleep(3)

driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
year="2022"
month="July"
date="17"


while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mon==month and yr==year:
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody//tr//td//a")
time.sleep(3)
for ele in dates:
    if ele.text==date:
        ele.click()
        break


driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='dob']").click()

date_pick = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
date_pick.select_by_visible_text("Feb")

# For selecting a date
date_pick_y = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
date_pick_y.select_by_visible_text("2002")
time.sleep(2)
# To select all the dates
dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody//tr//td//a")

for date in dates:
    if date.text=="17":
        date.click()
        break

time.sleep(3)

time.sleep(5)