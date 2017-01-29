#!/usr/bin/env python
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
global wait
global driver

def main():
	Username = "X"
	Password = "X"
	driver = login(Username, Password);
	homepage(driver);
	selenium.stop


def findButton(name,driver):

	buttons = driver.find_elements_by_css_selector("button")

	for button in buttons:
		if button.text.strip() == name:
			button.click()

def battle(driver):
	print("Which starter pokemon would you like to choose")
	starter = int(raw_input("0-5 to pick"))


def findRandomBattle(driver):
	while(true):
		battle = int(raw_input("Would you like to battle? 1 for another battle, 0 to exit"))
		if battle == 1:
			driver.find_element_by_name('search').click()
			time.sleep(2)
			print("Battle started")
			time.sleep(2)
			battle(driver);
		if battle == 0:
			break

def gotoLobby(driver):
	time.sleep(2)
	driver.find_element_by_xpath("//a[@href='/lobby']").click();
	lobby();

def loadTeam(driver):
	'''print("Enter the name of the file your team is stored in")
	team = raw_input("Enter input: ")'''
	time.sleep(2)
	teamConfig = open("team.txt", "r")

	driver.find_element_by_name('joinRoom').click()
	time.sleep(2)
	driver.find_element_by_name('newTop').click()
	time.sleep(2)
	driver.find_element_by_name('import').click()
	time.sleep(2)
	
	textboxes = driver.find_elements_by_class_name('textbox')
	for textbox in textboxes:
		if textbox.text == None:
			textbox.send_keys(teamConfig.read())
			break

	teamConfig.close()

	driver.find_element_by_name('saveImport').click()

	time.sleep(5)

	driver.find_element_by_css_selector('.select.formatselect.teambuilderformatselect').click()
	time.sleep(2)
	driver.find_element_by_name('selectFormat').click()
	sleep(2)
	driver.find_element_by_css_selector('.button.disabled').click()
	time.sleep(2)

	buttons = driver.find_elements_by_class_name('home')

	for home in buttons:
		if home.text.strip() == "Home":
			home.click()
			break


def lobby():
	return 0

def homepage(driver):
	print("Would you like to import teams? Keep the text file in the same directory as this file. (1 for yes, 0 for no")
	shouldLoadTeam = int(raw_input("Enter your answer: "))
	if shouldLoadTeam == 1:
		loadTeam(driver);

	time.sleep(2)
	text = 0
	while text != 1 or text != 2:
		print("Do you want to random battle (1) or go to the lobby (2) ?")
		text = int(raw_input("Enter your answer: "))
		time.sleep(1)

		if text == 1:
			findRandomBattle(driver);
			break;
		elif text == 2:
			gotoLobby(driver)
			break;

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
	return driver


if __name__ == '__main__':
	main()
