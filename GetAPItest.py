import requests
from requests.auth import HTTPBasicAuth
import json

url = 'https://barkcommerce.atlassian.net/rest/agile/1.0/board/46/issue'

newHeaders = {'Accept': 'application/json'}

response = requests.get(url, headers=newHeaders, auth=HTTPBasicAuth('leonardo.lemos@mktsystems.com', 'sUPaTQvL6hvg0lp11h1zAE65'))

x = response.json()
NameTest = ["CreateMenuWithSameName", "EmptyScreenMenuItemDetail", "PermissionGroupDefaultNotChecked", "SearchPromotionGroup"]

def teste123():
    for y in NameTest:
        for api_array in range(len(x['issues'])):
            if y in x['issues'][api_array]['fields']['summary']:
                if x['issues'][api_array]['fields']['status']['statusCategory']['key'] == "done":
                    print(x['issues'][api_array]['fields']['status']['statusCategory']['key'])                    
                    pass        
                else:
                    NameTest.remove(y)
                    print('teste removido da lista')   
# if existent == True and isOk == True:
#     lista.append(y)    
# if existent == False:
#     lista.append(y)          
# elif existent == True and isOk == False:
#     print('task em andamento')
#     continue

teste123()
print(NameTest)

i = 1 + 2