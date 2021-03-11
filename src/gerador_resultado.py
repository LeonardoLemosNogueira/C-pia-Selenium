import pandas as pd
import json
from threading import Thread
import queue
import smtplib
import requests
from requests.auth import HTTPBasicAuth
import config_var

que = queue.Queue()
threads_list = list()
ResultList = []

thread1 = Thread(target=lambda q, arg1: q.put(config_var.tests[0](arg1)), args=(que, 1))
thread2 = Thread(target=lambda q, arg1: q.put(config_var.tests[1](arg1)), args=(que, 2))
thread3 = Thread(target=lambda q, arg1: q.put(config_var.tests[2](arg1)), args=(que, 3))
thread4 = Thread(target=lambda q, arg1: q.put(config_var.tests[3](arg1)), args=(que, 4))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

threads_list.append(thread1)
threads_list.append(thread2)
threads_list.append(thread3)
threads_list.append(thread4)

for t in threads_list:
    t.join()

while not que.empty():
    resultado = que.get()
    ResultList.append(resultado)
    print(resultado.Id, resultado.TestAnswer, resultado.Nome)

Testes = []
TestAnswer = []
Id = []
Nome = []
TestesList = []

for i in range(len(ResultList)):
    
    Id.append(ResultList[i].Id)
    Nome.append(ResultList[i].Nome)
    if ResultList[i].TestAnswer == False:
        ResultList[i].TestAnswer = 'Teste reprovado.'
        TestAnswer.append(ResultList[i].TestAnswer)
    elif ResultList[i].TestAnswer == True:
        ResultList[i].TestAnswer = 'Teste aprovado.'
        TestAnswer.append(ResultList[i].TestAnswer)
    else:
        TestAnswer.append(ResultList[i].TestAnswer)
    TestesList.append([ResultList[i].Id, ResultList[i].Nome, ResultList[i].TestAnswer])

print(Nome)

Testes = {'Id': Id, 'Nome do teste': Nome, 'Resultado': TestAnswer}

df = pd.DataFrame(Testes, columns=['Id', 'Nome do teste', 'Resultado'])

server = smtplib.SMTP(config_var.smtp, config_var.smtpdoor)
server.starttls()
server.login(config_var.email_from, config_var.email_senha)

SUBJECT = "Testes Selenium"

msg = """
Subject: {}\n\n{}
""".format(SUBJECT, df)

server.sendmail(config_var.email_from, config_var.email_to, msg)
print("Email enviado com sucesso.")
server.quit()

url = 'https://barkcommerce.atlassian.net/rest/agile/1.0/board/46/issue'

newHeaders = {'Accept': 'application/json'}

response = requests.get(url, headers=newHeaders, auth=HTTPBasicAuth(config_var.auth_username, config_var.auth_password))

apiJSON = response.json()

disapproved = []

for z in range(len(ResultList)):
    if ResultList[z].TestAnswer == 'Teste reprovado.' or ResultList[z].TestAnswer == 'Teste falhou.':
        for api_array in range(len(apiJSON['issues'])):
            if ResultList[z].Nome in apiJSON['issues'][api_array]['fields']['summary']:
                if apiJSON['issues'][api_array]['fields']['status']['statusCategory']['key'] == "done":
                    print(apiJSON['issues'][api_array]['fields']['status']['statusCategory']['key'])
                    pass
                else:
                    disapproved.append(ResultList[z].Nome)

for element in disapproved:
    if element in Nome:
        Nome.remove(element)

print(Nome)

url = 'https://barkcommerce.atlassian.net/rest/api/3/issue'

newHeaders = {'Content-type': 'application/json', 'Accept': 'application/json'}

for p in Nome:
    obj_issue = {
        "update": {},
        "fields": {
            "summary": "O teste " + p + " foi reprovado.",
            "issuetype": {
                "id": "10193"
            },
            "project": {
                "id": "10049"
            },
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "text": "O teste " + p + " foi reprovado.",
                                "type": "text"
                            }
                        ]
                    }
                ]
            },
            "customfield_10000": "agora",
            "labels": [
                "bugfix",
                "blitz_test"
            ]
        }
    }
    apiJSON = requests.post(url, data=json.dumps(obj_issue), headers=newHeaders,
                            auth=HTTPBasicAuth(config_var.auth_username, config_var.auth_password))
    print(apiJSON)

if Nome != []:
    raise Exception("Existem testes reprovados!")