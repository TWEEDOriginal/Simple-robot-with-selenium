from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mywebsitechecker import comment

def main():
    opts = Options()
    opts.add_argument("--disable-extensions")
    opts.add_argument("--headless")
    driver = Firefox(options=opts,executable_path=r'My computers path')
    driver.get('https://tweeds-first-app.herokuapp.com/add_post')
    print(driver.title)
    username = driver.find_element_by_name('username')
    username.clear()
    username.send_keys("")
    password = driver.find_element_by_name('password')
    password.clear()
    password.send_keys("")
    submit = driver.find_element_by_class_name('btn')
    submit.click()
    time.sleep(5)
    comment(driver)
    driver.close()
    driver.quit()  
      

    
if __name__ == '__main__':
    main()      