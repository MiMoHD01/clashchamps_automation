from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


WINDOW_SIZE = "1920,1080"

# Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)

# Get the response and print title
driver.get("https://www.clashchamps.com/looking-for-players-clan-sign-up/")
print(driver.title)
wait = WebDriverWait(driver, 10)
sign_in = "(/html/body/div[1]/div/div[4]/div[2]/div/div[1]/div/article/div/div/div/section/div/div[1]/div/div/div[5]/div/div/span/a)[1]"
wait.until(EC.element_to_be_clickable(By.XPATH, sign_in))
driver.find_element(By.XPATH, sign_in).click
WebDriverWait(driver, 10)
print(driver.title)
driver.close()
