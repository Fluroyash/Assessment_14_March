from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time
a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

driver.get("https://www.naukri.com")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Register").click()
time.sleep(3)
driver.find_element(By.ID, "name").send_keys("Yash Raj Singh Rathore")
time.sleep(3)
driver.find_element(By.ID, "email").send_keys("yashraj123@gmail.com")
time.sleep(3)
driver.find_element(By.ID, "password").send_keys("Test@1234")
time.sleep(5)
driver.quit()
