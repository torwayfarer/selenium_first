import selenium
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://www.tinkoff.ru/login/?redirectTo=%2Fevents%2Ffeed%2F')
id_box = driver.find_element_by_name("login")
code=input('Enter your login: ')
id_box.send_keys(code)
paw_box=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[3]/div/div[2]/div/div[2]/div/div/div/div[1]/form/div[1]/div/div[1]/div/div/label/div[1]/input')
password_box=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[3]/div/div[2]/div/div[2]/div/div/div/div[1]/form/div[1]/div/div[2]/div/div/label/div[1]/input")
code=input('Enter your password: ')
password_box.send_keys(code)
login_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[3]/div/div[2]/div/div[2]/div/div/div/div[1]/form/div[2]/div/div/span/button')
login_button.click()
code=input('Enter your code: ')
id_box=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div/div/form/div/div/div/label/div[1]/input")
id_box.send_keys(code)
time.sleep(10)
#driver.back()
for i in range(100):
	if i != 0:
		driver.back()
	else:
		payment = driver.find_element_by_link_text('Платежи')
		payment.click()
		time.sleep(10)
		xx=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/span/a')
		xx.click()
	time.sleep(10)
	money_box=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div/div/div/div[1]/form/div[2]/div/div/div/div/div/div[2]/div/div/label/div/input')
	for j in range(5):
		money_box.send_keys(Keys.BACK_SPACE)
	money_box.send_keys('0.33')
	time.sleep(8)
	final=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div/div/div/div[1]/form/div[4]/div/div[1]/div/div/button')
	final.click()
	time.sleep(5)




