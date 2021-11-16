from helpers.screenshot_listener import ScreenshotListener as sl
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def screenshot_decorator(test_fun):
   def wrapper(self):
       try:
           return test_fun(self)
       except AssertionError as ex:
           sl.make_screenshot(self.driver, 'assert')
           raise ex
       except TimeoutException as ex:
           sl.make_screenshot(self.driver, 'timeout')
           raise ex
       except NoSuchElementException as ex:
           sl.make_screenshot(self.driver, 'not found')
           raise ex

   return wrapper