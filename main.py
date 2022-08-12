
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import itertools
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://vilaweb.cat/paraulogic/')

letters = driver.find_element(by=By.CLASS_NAME, value='container-hexgrid').text.split('\n')
letters = [ x for x in letters if len(x) == 1 ]

keyletter = driver.find_element(by=By.ID, value='center-letter').text

input_word = driver.find_element(by=By.ID, value='test-word')

btn_submit = driver.find_element(by=By.ID, value='submit-button')

words = pd.read_csv('catala.csv')
words = words["'en"].astype(str).str.upper()

# clean catalan dict
possible_words = []
for word in words:
    if len(word) > 2:
        wrong_word = False
        for x in word:
            if not x in letters:
                wrong_word = True
                break
    if wrong_word:
        continue
    else:
        possible_words.append(word)

# check words
for word in possible_words:
    if keyletter in word:
        driver.switch_to.active_element.send_keys(word)
        btn_submit.click()

# don't close
while True:
    pass