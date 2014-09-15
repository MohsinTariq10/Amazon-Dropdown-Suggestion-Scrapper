import time
from selenium import webdriver
import sys

sting = ""
x =0
for arg in sys.argv:
    if (x == 0):
        x+=1
        continue
    sting += arg
    sting += " "

i = 1
driver = webdriver.Firefox()
driver.get('https://www.amazon.com/')
elem = driver.find_element_by_id("twotabsearchtextbox")
elem.send_keys("laptop")
time.sleep(3)
for i in range (10):
    try:
        print(driver.find_element_by_id("issDiv{}".format(i)).text)
    except:
        break

driver.close()
