from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time
a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

driver.get("https://www.youtube.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.NAME,"search_query").send_keys("melody hits")
time.sleep(5)
driver.quit()
