# 1 open the browser
# 2.enter url
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
a=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=a)

driver.get("https://www.ironspider.ca/forms/checkradio.htm")
driver.maximize_window()

# 1. select specific check box
# driver.find_element(By.XPATH,"//input[@value='red']").click()

# 2. select ALL check box
check=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@name,'color')]")
# print("Number of check box are",len(check))

# with using range

# for i in range (len(check)):
#     check[i].click()
# Without using
# for i in check:
#    i.click();
# time.sleep(3)
# 3. select Multiple check box of my choice
for i in check:
    wee = i.get_attribute('value')
    if wee == 'green' or wee == 'red':
        i.click()

# 4. select 2 ch checkbox from last
# for i in range (len(check)-2, len(check)):
#     check[i].click()
# for i in range (len(check)):
#     if i<2:
#         check[i].click()

# 5. Un-select all the checkboxes
# for i in check:
#     if i.is_selected():
#         i.click();

time.sleep(5)