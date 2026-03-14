from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time
a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)


driver.get("https://www.myntra.com/")
driver.maximize_window()
time.sleep(3)
search_box = driver.find_element(By.CLASS_NAME, "desktop-searchBar")
search_box.send_keys("shoes")
time.sleep(3)
driver.quit()