import time
import allure
from allure_commons.types import AttachmentType
from config import config_path as cp



class ScreenshotListener():
  def make_screenshot(driver, producer):
      config = cp.config_path()
      path = config.get('local_path', 'path')
      screenshot_path = f"C:/{path}/Home-Assignment/screenshots/{producer}_exception{time.time()}.png"
      driver.set_window_size(1920, 1080)
      driver.get_screenshot_as_file(screenshot_path)
      allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
      print(f"Screenshot saved as {screenshot_path}")

