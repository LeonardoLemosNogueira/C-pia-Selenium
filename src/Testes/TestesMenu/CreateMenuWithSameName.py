from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from ..Components import LoginAsADM
from ..ObjDefinition import Resultado

class CreateMenuWithSameName:
    def Testar(Id):
        try:
            sleeptime = 30
            resultado = Resultado()
            DRIVER_PATH = 'chromedriver.exe'
            options = Options()
            #Set False if you want to view this test ⬇️ and call this function at the end of the algorithm
            options.headless = True
            options.add_argument("--window-size=1930,1300")
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')

            # if you use WINDOWS comment line 22 and uncomment line 20
            # driver = webdriver.Chrome(DRIVER_PATH, options=options)
            
            driver = webdriver.Chrome(options=options)

            UserName = datetime.now()
            LoginAsADM.Componentes.Login(driver)
            sleep(sleeptime)
            driver.get("https://qa.mktsystems.com/KonduzaContent/MenuDetail?Kin=0")
            sleep(sleeptime)
            input_name = driver.find_element_by_id('Input_Name')
            input_name.click()
            input_name.send_keys(UserName.strftime('%d/%m/%Y %H:%M') +  Keys.RETURN)
            driver.get("https://qa.mktsystems.com/KonduzaContent/MenuDetail?Kin=0")
            sleep(sleeptime)
            input_name = driver.find_element_by_id('Input_Name')
            input_name.click()
            input_name.send_keys(UserName.strftime('%d/%m/%Y %H:%M') +  Keys.RETURN)
            driver.get("https://qa.mktsystems.com/KonduzaContent/MenuList")
            sleep(sleeptime)
            h7 = driver.find_element_by_id('Input_TextVar')
            h7.click()
            h7.send_keys(UserName.strftime('%d/%m/%Y %H:%M') +  Keys.RETURN)
            sleep(sleeptime)
            result = driver.find_elements_by_class_name('table-row')
            resultado = Resultado()
            resultado.Nome = "CreateMenuWithSameName"
            if len(result) == 1:
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
            resultado.Nome = "CreateMenuWithSameName"
            return resultado