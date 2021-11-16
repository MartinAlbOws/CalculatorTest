import unittest
from base_setup import BaseTestClass
from calculator_page import calculator
from wrapper import screenshot_decorator


class MainTests(BaseTestClass):

    @screenshot_decorator
    def test_cal(self):
        expected_text = "15"
        cal = calculator(driver=self.driver)
        cal.click_button_7()
        cal.click_button_plus()
        cal.click_button_8()
        cal.click_button_equate()
        actual_text_content = self.driver.find_element_by_xpath(cal.result_component_xpath).text
        assert expected_text == actual_text_content
        print(f'Sum found by xpath is {actual_text_content} that same than expected was {expected_text}')


if __name__ == '__main__':
    unittest.main()