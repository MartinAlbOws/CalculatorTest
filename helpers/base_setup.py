import os
import unittest
from selenium import webdriver
from config import config_path as cp


class BaseTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        config = cp.config_path()
        if os.name == 'nt':
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            self.driver = webdriver.Chrome(options=options, executable_path=(config.get('chromedriver_path', 'path')))
            self.driver.get('https://ahfarmer.github.io/calculator/')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

