import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# 1.mouse hovering operations

driver.get("https://www.toolsqa.com")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@class='navbar__tutorial-menu--text']").click()
fet=driver.find_element(By.XPATH, "//span[normalize-space()='DevOps Tools']")

act=ActionChains(driver)
act.move_to_element(fet).perform()
time.sleep(2)

# 2.right click operation
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button=driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
act=ActionChains(driver)
act.context_click(button).perform()
time.sleep(2)

# Scroll operations
# a.Specific No. of Pixels
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.execute_script("window.scrollBy(0,3000)","")
value=driver.execute_script("return window.pageYOffset;")
print("No.of pixel Moved :",value)
time.sleep(2)

# b.Scroll to the specific element
flag=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value=driver.execute_script("return window.pageYOffset;")
print("No.of pixel Moved :",value)
time.sleep(3)

# c.Scroll To the End of the  page

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("No.of pixel Moved :",value)
time.sleep(2)

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("No.of pixel Moved :",value)
time.sleep(2)

# 1.keyboard operation
driver.get("https://text-compare.com/")
driver.maximize_window()

inputbox1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
inputbox2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

inputbox1.send_keys("This is a ST Class")
act = ActionChains(driver)
time.sleep(1)

# # select the text
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()

# Alternative
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(1)
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
time.sleep(1)

# Press tab key
act.send_keys(Keys.TAB).perform()
time.sleep(1)

# paste
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(3)
