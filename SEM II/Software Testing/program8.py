import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests as requests

ser = Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=ser)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# Click on a link
driver.find_element(By.LINK_TEXT, "Digital downloads").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()
links = driver.find_elements(By.TAG_NAME, "a")
print("total links", len(links))
time.sleep(2)

total = driver.find_elements(By.XPATH, "//a")
print("total links", len(total))

# print all the link names
for i in total:
    print(i.text)


# Broken link
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

tot = driver.find_elements(By.TAG_NAME, "a")
count = 0
for link in tot:
    url = link.get_attribute("href")
    try:
        response = requests.head(url)
    except:
        var = None
    if response.status_code>=400:
        print(url, " is a broken")
        count += 1
    else:
        print(url,"url is Broken")
print("tot no. of broken links: ",count)
time.sleep(3)