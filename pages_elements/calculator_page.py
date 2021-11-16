class calculator:
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.button_0_xpath = '//*[text()="0"]'
        self.button_1_xpath = '//*[text()="1"]'
        self.button_2_xpath = '//*[text()="2"]'
        self.button_3_xpath = '//*[text()="3"]'
        self.button_4_xpath = '//*[text()="4"]'
        self.button_5_xpath = '//*[text()="5"]'
        self.button_6_xpath = '//*[text()="6"]'
        self.button_7_xpath = '//*[text()="7"]'
        self.button_8_xpath = '//*[text()="8"]'
        self.button_9_xpath = '//*[text()="9"]'
        self.button_plus_minus_xpath = '//*[text()="+/-"]'
        self.button_AC_xpath = '//*[text()="AC"]'
        self.button_percent_xpath = '//*[text()="%"]'
        self.button_equate_xpath = '//*[text()="="]'
        self.button_plus_xpath = '//*[text()="+"]'
        self.button_minus_xpath = '//*[text()="-"]'
        self.button_multiplication_xpath = '//*[text()="x"]'
        self.button_division_xpath = '//*[text()="÷"]'
        self.result_component_xpath = '//*[@class="component-display"]'


    def click_button_7(self):
        button_7 = self.driver.find_element_by_xpath(self.button_7_xpath)
        button_7.click()
        return self

    def click_button_plus(self):
        button_plus = self.driver.find_element_by_xpath(self.button_plus_xpath)
        button_plus.click()
        return self

    def click_button_8(self):
        button_8 = self.driver.find_element_by_xpath(self.button_8_xpath)
        button_8.click()
        return self

    def click_button_equate(self):
        button_equate = self.driver.find_element_by_xpath(self.button_equate_xpath)
        button_equate.click()
        return self

