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

