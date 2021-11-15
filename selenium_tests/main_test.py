import unittest
from base_setup import BaseTestClass
from calculator_page import calculator


class MainTests(BaseTestClass):


    def test_cal(self):
        expected_text = "15"
        cal = calculator(driver=self.driver)
        button_7 = self.driver.find_element_by_xpath(cal.button_7)
        button_7.click()
        button_plus = self.driver.find_element_by_xpath(cal.button_plus)
        button_plus.click()
        button_8 = self.driver.find_element_by_xpath(cal.button_8)
        button_8.click()
        button_equate = self.driver.find_element_by_xpath(cal.button_equate)
        button_equate.click()
        actual_text_content = self.driver.find_element_by_xpath(cal.result_component).text
        assert expected_text == actual_text_content
        print(f'Sum found by xpath is {actual_text_content} that same than expected was {expected_text}')


if __name__ == '__main__':
    unittest.main()