"""
Created by Caleb Mingo
2/14/2022

The purpose of this program was originally to generate a specified amount of email with randomly generated names and passwords
and store these usernames and passwords into a text file for future use.
Due to "I am not a robot" I could not finish this project (probably a good thing for humanity lol).
With chrome version 97 and a chrome driver installed, this programs enters in user information on yandex.com and inputs information 
onto the website in an automated fashion.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random
import time
import sys

#11 first and last names
first_name_list = ["john", "sara", "nadia", "caleb", "jim", "hannah", "jeff", "jacob", "sheila", "mohammad", "syeda"]
last_name_list = ["henderson", "smith", "bateman", "shah", "little", "cunningham", "price", "scott", "grande", "pilgrim", "goggins"]
#11 options for first and second part of passwords
password_first_part_list = ["shadow", "silent", "zealous", "poisonous", "greedy", "lightning", "terminal", "dark", "blazing", "deadly", "wrathful"]
password_second_part_list = ["Watcher", "Challenger", "King", "Jester", "Ninja", "Samurai", "Knight", "Fighter", "Killer", "Hero", "Zealot"]

#Insert directory for webdriver here
s = Service('/Users/calebmingo/Downloads/chromedriver')
driver = webdriver.Chrome(service=s)

#Resize driver
driver.set_window_size(1080,720)

driver.get('https://passport.yandex.com/registration/mail?from=mail&require_hint=1&origin=hostroot_homer_reg_com&retpath=https%3A%2F%2Fmail.yandex.com%2F&backpath=https%3A%2F%2Fmail.yandex.com%3Fnoretpath%3D1')
time.sleep(2)
last_name = last_name_list[random.randint(0, 10)]
first_name = first_name_list[random.randint(0, 10)]
identifier = random.randint(1000, 9999)

password = password_first_part_list[random.randint(0, 10)] + password_second_part_list[random.randint(0,10)] + str(identifier)
username = first_name + last_name + str(identifier)

#records email address and password into a text file
email_database_text = 'email_collection.txt'
sys.stdout = open(email_database_text, "a")
print(username)
print(password)
#email_database_text.close()

#Send first name in
first_name_entry = driver.find_element(By.ID, "firstname")
first_name_entry.send_keys(first_name)

#enter in last name
last_name_entry = driver.find_element(By.ID, "usernamereg-lastName")
last_name_entry.send_keys(last_name)

#enter in email
email_entry = driver.find_element(By.ID, "email")
email_entry.send_keys(username)

#enter in password
password_entry = driver.find_element(By.ID, "email")
password_entry.send_keys(password)

