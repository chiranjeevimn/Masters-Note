import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('D:\Drivers\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://bmsitm.gnums.in/Login.aspx")
driver.find_element(By.NAME, "txtUsername").send_keys("chiranjeevichiru724@gmail.com")
driver.find_element(By.ID, "txtPassword").send_keys("Chiru12@")
driver.find_element(By.NAME, "btnLogin").click()

act_title = driver.title
exp_title = "BMS Institute of Technology & Management"
if act_title == exp_title:
    print("Test is passed")
else:
    print("Test failed")
print("\n")

time.sleep(10)
