import os

def save_screenshot(driver, name, save_location):
  # Make sure the path exists.
  path = os.path.abspath(save_location)
  if not os.path.exists(path):
    os.makedirs(path)
  full_path = '%s/%s' % (path, name)
  driver.save_screenshot(full_path)
  return full_path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Firefox()
driver.get('http://www.app2b.cn/')
driver.set_window_size(width_needed, height_needed)
screenshot = take_screenshot(driver, 'app2b_firefox.png', 'screenshots')
print "Screenshot saved to: %s" % screenshot
driver.quit()

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--window-size=320,480")
chrome_options.add_argument("--user-agent='Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'")
driver2 = webdriver.Chrome(chrome_options=chrome_options)
driver2.get('http://www.app2b.cn/')
screenshot = save_screenshot(driver2, 'app2b_chrome.png', 'screenshots')
print "Screenshot saved to: %s" % screenshot
driver2.quit()
