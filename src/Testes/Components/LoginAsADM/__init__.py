from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys


class Componentes:
    def Login(driver):
        driver.get("https://qa.mktsystems.com/KonduzaBackoffice/Login")
        time.sleep(15)
        h1 = driver.find_element_by_name('account-key')
        h1.click()
        h1.send_keys("users")
        h2 = driver.find_element_by_id('Input_UsernameVal')
        h2.click()
        h2.send_keys("leonardo.lemos@mktsystems.com")
        h3 = driver.find_element_by_id('Input_PasswordVal')
        h3.click()
        h3.send_keys("123456" + Keys.RETURN)