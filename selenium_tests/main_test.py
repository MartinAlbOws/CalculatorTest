import unittest
from base_setup import BaseTestClass
from calculator_page import calculator


class MainTests(BaseTestClass):


    def test_cal(self):
        expected_text = "15"
        cal = calculator(driver=self.driver)
        cal.button_7()
        cal.button_plus()
        cal.button_8()
        cal.button_equate()
        actual_text_content = self.driver.find_element_by_xpath(cal.result_component_xpath).text
        assert expected_text == actual_text_content
        print(f'Sum found by xpath is {actual_text_content} that same than expected was {expected_text}')


if __name__ == '__main__':
    unittest.main()