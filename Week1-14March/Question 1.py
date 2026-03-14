from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time

a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(5)

# email
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("Ram")
time.sleep(3)


driver.find_element(By.CSS_SELECTOR, "input[name='pass']").send_keys("Test@123")
time.sleep(3)


driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Log in"]').click()
time.sleep(5)

driver.quit()

