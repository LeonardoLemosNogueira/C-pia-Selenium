import pandas as pd
import json
from threading import Thread
import queue
import EmptyScreenMenuItemDetail
import CreateMenuWithSameName
import PermissionGroupDefaultNotChecked
import SearchPromotionGroup
import smtplib
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth

ArrayTest = [[3, 'Teste reprovado', 'PermissionGroupNotChecked'], [4, 'Teste reprovado', 'SearchPromotionGroup'], [1, 'Teste reprovado', 'EmptyScreenMenuItemDetail'], [2, 'Teste reprovado', 'CreateMenuWithSameName']]

url = 'https://barkcommerce.atlassian.net/rest/api/3/issue'

newHeaders = {'Content-type': 'application/json', 'Accept': 'application/json'}

for resultado in ArrayTest:
    if resultado[1] == 'Teste reprovado':
        NameTest = resultado[2]
        myobj = {
            "update": {},
            "fields": {
                "summary": "O teste " + NameTest + " falhou.",
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
                        "text": "Order entry fails when selecting supplier.",
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
    x =  requests.post(url, data=json.dumps(myobj), headers=newHeaders, auth=HTTPBasicAuth('leonardo.lemos@mktsystems.com', 'sUPaTQvL6hvg0lp11h1zAE65'))
    print (x)