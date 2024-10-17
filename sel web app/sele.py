from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def run_selenium_test():
    driver = webdriver.Chrome()  # Make sure chromedriver is installed
    driver.get('https://www.google.com')
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('Selenium' + Keys.RETURN)
    print("Test Completed: Google search for 'Selenium' was executed successfully.")
    driver.quit()

if __name__ == '__main__':
    run_selenium_test()
