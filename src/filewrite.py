import EmptyScreenMenuItemDetail
import CreateMenuWithSameName
import PermissionGroupDefaultNotChecked
import SearchPromotionGroup

def escreveArquivo(numero, result):
    f = open('arquivoresult.csv', "a")
    f.writelines(1,"EmptyScreenMenuItemDetail", EmptyScreenMenuItemDetail.result)
    f.writelines(2,"CreateMenuWithSameName", CreateMenuWithSameName.result)
    f.writelines(3, "PermissionGroupNotChecked", PermissionGroupDefaultNotChecked.result)
    f.writelines(4, "SearchPromotionGroup", SearchPromotionGroup.result)
    f.close()