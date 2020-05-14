from selenium import webdriver
import urllib.request
import lxml.html
url = "https://mail.ntu.edu.tw/owa/auth/logon.aspx?replaceCurrent=1&url=https%3a%2f%2fmail.ntu.edu.tw%2fowa%2f" # NTU Mail
driver = webdriver.Chrome()
driver.get(url)
account = driver.find_element_by_name("username")
account.send_keys("[your_account]") # account
password = driver.find_element_by_name("password")
password.send_keys("[your_password]")  # password
btn = driver.find_elements_by_class_name("signinbutton")[0]
btn.click()
#driver.close()
