from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService


service = ChromeService(executable_path=r"C:\\webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

driver.implicitly_wait(5)
search_box = driver.find_element("name", "q")

search_box.send_keys('dogs')

search_box.submit()

input("press enter to leave")
driver.quit()
