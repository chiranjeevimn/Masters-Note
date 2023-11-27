# 1 open the browser
# 2.enter url
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

a=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=a)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


# id and name are he two locators

# driver.find_element(By.ID ,"small-searchterms").send_keys("Dell laptop")
# driver.find_element(By.NAME, "q").send_keys("Dell")

# Link test and partial link test

# driver.find_element(By.LINK_TEXT, "Register").click()
# driver.find_element(By.LINK_TEXT ,"Log in").click()

# partial link text
# driver.find_element(By.PARTIAL_LINK_TEXT ,"Reg").click()
# driver.find_element(By.PARTIAL_LINK_TEXT ,"Log").click()

# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# s = driver.find_elements(By.CLASS_NAME ,"a-carousel-card")
# print("The number of sliders",len(s))

# links = driver.find_elements(By.TAG_NAME,"a")
# print("The number of Links",len(links))


driver.get("https://www.facebook.com/")
driver.maximize_window()
# 1.tag and id

# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("xyz@gamil.com")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("xyz@gamil.com") #without tagname


# 2. tag and class

# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("xyz@gamil.com")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("xyz@gamil.com") #removing Tag name

# 3. tag and attribute

# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("xyz@gamil.com")
# driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("xyz@gamil.com") #without tagname

# 4.tag class and atribute

driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_pass]").send_keys("abc")  # without tagname


time.sleep(5)