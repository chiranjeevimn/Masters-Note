# 1 open the browser
# 2.enter url
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
a=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=a)

# driver.get("https://www.amazon.in/")
# driver.maximize_window()

# Absolute path

# driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys("Mobiles")
# driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input").click()

# Relative Xpath

# driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']").send_keys("Mobiles")
# driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button']").click()

# options - or & and

# driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox' or @name='fil-keywords']").send_keys("Mobiles")
# driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox' or @name='field-keywords']").send_keys("Mobiles")

# driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox' and @class='nav-input nav-progressive-attribute']").send_keys("Mobiles")
# make any changes in the class or id it will not execute.
# driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox' and @class='navinput nav-progressive-attribute']").send_keys("Mobiles")

# contains()

# driver.find_element(By.XPATH,"//*[contains(@id,'twotab')]").send_keys("tshirt")

# starts-with()

# driver.find_element(By.XPATH,"//*[starts-with(@id,'twotab')]").send_keys("tshirt")

# text()

# driver.find_element(By.XPATH,"//*[text()='Amazon miniTV']").click()

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# Self
text_msg=driver.find_element(By.XPATH, "//*[contains(text(),'Zomato')]/self::a").text
print("the self text is",text_msg)

#  parent
text_msg1=driver.find_element(By.XPATH, "//a[contains(text(),'Zomato')]/parent::td").text
print("The parent XPath access text ",text_msg1)

#  ancestor
text_msg3 = driver.find_element(By.XPATH, "//a[contains(text(),'Zomato')]/ancestor::tr").text
print(text_msg3)

# Child
childs = driver.find_elements(By.XPATH, "//a[contains(text(),'Zomato')]/ancestor::tr/child::td")
print("no of child nodes", len(childs))

# Descendent
decen = driver.find_elements(By.XPATH, "//a[contains(text(),'Zomato')]/ancestor::tr/descendant::*")
print("No of decendent", len(decen))

# following
fol = driver.find_elements(By.XPATH, "//a[contains(text(),'Zomato')]/ancestor::tr/following::*")
print("Number of following", len(fol))

# Following siblings
fols = driver.find_elements(By.XPATH,"//a[contains(text(),'Zomato')]/ancestor::tr/following-sibling::*")
print("Number of following siblings", len(fols))

# preceding
pre = driver.find_elements(By.XPATH,"//a[contains(text(),'Zomato')]/ancestor::tr/preceding::*")
print("Number of preceding", len(pre))

# preceding siblings
pres = driver.find_elements(By.XPATH,"//a[contains(text(),'Zomato')]/ancestor::tr/preceding-sibling::*")
print("Number of preceding siblings", len(pres))
time.sleep(10)