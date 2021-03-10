from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.common.by import By
from ..Components import LoginAsADM
from ..ObjDefinition import Resultado

class EmptyScreenMenuItemDetail:
    def Testar(Id):
        try:
            sleeptime = 30
            resultado = Resultado()
            DRIVER_PATH = 'chromedriver.exe'
            options = Options()
            #Set False if you want to view this test ⬇️ and call this function at the end of the algorithm
            options.headless = True
            options.add_argument("--window-size=1920,1200")
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')

            # if you use WINDOWS comment line 22 and uncomment line 20
            # driver = webdriver.Chrome(DRIVER_PATH, options=options)
            
            driver = webdriver.Chrome(options=options)

            LoginAsADM.Componentes.Login(driver)
            sleep(sleeptime)
            driver.get("https://qa.mktsystems.com/KonduzaContent/MenuItemList?Kin=1086324300")
            sleep(sleeptime)
            h2 = driver.find_element_by_class_name('btn-primary')
            h2.click()
            sleep(sleeptime)
            driver.execute_script("window.history.go(-1)")
            sleep(sleeptime)
            result = driver.find_elements_by_id('l2-0-b7-b1-Input')
            resultado.Nome = "EmptyScreenMenuItemDetail"
            if result == 1:
                print('Teste aprovado.')
                resultado.Id = Id
                resultado.TestAnswer = True
                return resultado
            else:
                print('Teste reprovado.')
                resultado.Id = Id
                resultado.TestAnswer = False
                return resultado
        except:
            resultado.Id = Id
            resultado.TestAnswer = "Teste falhou."
            resultado.Nome = "EmptyScreenMenuItemDetail"
            return resultado  