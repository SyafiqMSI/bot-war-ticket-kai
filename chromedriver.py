from seleimp import *

PATH = "/chromedriver/chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--start-maximized") 
chrome_options.add_argument("--disable-infobars") 
chrome_options.add_argument("webdriver.chrome.driver=" + PATH)

driver = webdriver.Chrome(options=chrome_options)
