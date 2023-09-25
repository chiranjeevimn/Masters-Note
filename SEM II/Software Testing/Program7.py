import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser = Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=ser)

driver.get("https://demoqa.com/select-menu")
driver.maximize_window()

down = driver.find_element(By.XPATH, "//select[@id='oldSelectMenu']")
drop = Select(down)

# 1.Select an option from the dropdown
drop.select_by_visible_text("Purple")  # Most widely used option
time.sleep(3)

# 2. Select by value
drop.select_by_value("7")
time.sleep(2)

# 3. Select By index value
drop.select_by_index(2)
time.sleep(2)

# 4. capture all operation
allop = drop.options
print("total number of option", len(allop))
time.sleep(3)

# 5. print all options
for opt in allop:
    print(opt.text)
time.sleep(2)

# 6. Select without using any built-in function
for opr in allop:
    if opr.text == "Yellow":
        opr.click()
        break
time.sleep(2)
