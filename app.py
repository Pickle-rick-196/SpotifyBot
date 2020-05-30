#importing packages
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

Options = Options()
Options.headless = True

class bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://open.spotify.com/'
        self.bot = webdriver.Chrome("E:/chromedriver.exe", options = Options)
        self.play()


    def play(self):
        self.bot.get(self.base_url)
        time.sleep(3)
        self.bot.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[1]/header/div[4]/button[2]').click()
        time.sleep(7)
        self.bot.find_element_by_xpath('//*[@id="login-username"]').send_keys(self.username)
        self.bot.find_element_by_xpath('//*[@id="login-password"]').send_keys(self.password)
        self.bot.find_element_by_xpath('//*[@id="login-password"]').send_keys(Keys.RETURN)
        time.sleep(7)
        self.bot.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[2]/nav/div[2]/div/div/div[2]/a').click()
        time.sleep(4)
        self.bot.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/button').click()
        time.sleep(100)

if __name__ == "__main__":
    BOT = bot("mickey123anime@gmail.com","9829096397")
