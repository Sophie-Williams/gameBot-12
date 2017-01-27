#!/usr/bin/env python
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
global wait

def main():
	Username = "AuuxL"
	Password = "appleman"
	login(Username, Password)

def findButton(name,driver):

	buttons = driver.find_elements_by_css_selector("button")

	for button in buttons:
		if button.text.strip() == name:
			button.click()


def findBattle(username, driver):
	time.sleep(2)
	driver.find_element_by_name('search').click()
	print("Battle started")


def login(Username, Password):
	driver = webdriver.Chrome('/home/auuxl/Downloads/chromedriver')
	driver.get("http://pokemonshowdown.com")
	driver.find_element_by_css_selector('.mainbutton').click()
	time.sleep(2)
	currentUrl = driver.current_url
	driver.get(currentUrl)
	time.sleep(2)

	findButton("Choose name", driver);
	time.sleep(2)
	driver.find_element_by_name("username").send_keys(Username);
	driver.find_element_by_name("username").send_keys(Keys.RETURN);
	time.sleep(2)
	driver.find_element_by_name("password").send_keys(Password);
	driver.find_element_by_name("password").send_keys(Keys.RETURN);

	time.sleep(2)
	findButton("Choose name", driver);

	time.sleep(2)

	findBattle("Shaun", driver);

	selenium.stop



if __name__ == '__main__':
	main()
