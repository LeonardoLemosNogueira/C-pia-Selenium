#ARQUIVO CRIADO EXCLUISIVAMENTE PARA CONFIGURAÇÃ DE VARIÁVEIS.
from Testes.TestesMenu import CreateMenuWithSameName
from Testes.TestesPermissao import PermissionGroupDefaultNotChecked, SearchPromotionGroup
from Testes.TestesScreen import EmptyScreenMenuItemDetail

#A VARIAVEL tests É UM ARRAY COM TODOS OS TESTES.
tests = [EmptyScreenMenuItemDetail.EmptyScreenMenuItemDetail.Testar, CreateMenuWithSameName.CreateMenuWithSameName.Testar , PermissionGroupDefaultNotChecked.PermissionGroupDefaultNotChecked.Testar, SearchPromotionGroup.SearchPromotionGroup.Testar]
# Para executar um teste específico basta adicionar sua classe e seu método no array da linha abaixo, descomentar a linha e comentar a variável da linha 8.
# tests = [EmptyScreenMenuItemDetail.EmptyScreenMenuItemDetail.Testar] 

#VARIÁVEIS DE EMAIL.

email_from = "skylucacius4@hotmail.com"
email_senha = "mkt_teste!99"
email_to = "leolnogueira@hotmail.com"
emailType = "hotmail" # EXEMPLO: gmail

if emailType == "gmail":
    smtp = "smtp-gmail.com"
    smtpdoor = 465
elif emailType == "hotmail":
    smtp = "smtp-mail.outlook.com"
    smtpdoor = 587

#VARIÁVEIS PARA API.

auth_username = 'leonardo.lemos@mktsystems.com'
auth_password = 'sUPaTQvL6hvg0lp11h1zAE65'