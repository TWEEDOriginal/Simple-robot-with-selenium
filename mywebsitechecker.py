from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def comment(browser):
    driver = browser
    print(driver.title)
    blog_link = driver.find_element_by_link_text('Blogs')
    blog_link.click()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "post-thumbnail"))
        )
        element.click()
        time.sleep(5)
        new_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "usercomment"))
        )
        new_element.send_keys('Selenium Rocks')
        button = driver.find_element_by_class_name('btn-secondary')
        driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()
        driver.refresh()
        #driver.back()
        #driver.forward()
    except:
        driver.close()
        driver.quit()  

    
if __name__ == '__main__':
    comment(browserr)      