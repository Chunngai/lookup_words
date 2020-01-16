#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def lookup_words():
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 3)

    global url
    driver.get(url)
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "html")))

    while True:
        word = input("input the word to be checked: ")

        if word == '#':
            break

        url = f"https://dict.hjenglish.com/w/{word}"
        driver.get(url)
        wait.until(ec.presence_of_element_located((By.TAG_NAME, "html")))

        with open("eng_words.txt", 'a') as f:
            f.write(word + '\n')


if __name__ == '__main__':
    url = "https://dict.hjenglish.com"

    lookup_words()
