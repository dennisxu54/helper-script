# import module
import openpyxl
import math
  
# load excel with its path
wrkbk = openpyxl.load_workbook("Sept 2023 Biz Collection_Biz Corporates USA Price List .xlsx", data_only=True)

# Make sure the sheet name is same as on the excel
sh = wrkbk["CAN"]

list1 = []
myDict = {}
  
# iterate through excel and display data
for i in range(3, 280):
    print("\n")
    print("Row ", i, " data :")
    category_name = [" ", "Style", "STYLE", "WORKS PANTS & SHORTS", "ENGINEERED OUTERWEAR", "OVERALLS", "FIRE ARMOUR", "POLOS", "TEES", 
                     "SHIRTS", "BIZ SEPARATES", "KNITWEAR", "HOODIES & FLEECE", "ACTIVEWEAR", "JACKETS", "HOSPITALITY", "HEALTH & BEAUTY",
                     "HEALTHWEAR", "CASUALWEAR", "TOPS", "SEPARATES", 'PAGE']
      
    # Make sure this is the correct column i.e. the unique identifier
    cell_product_slug = sh.cell(row=i, column=4).value
    if (cell_product_slug == None or (cell_product_slug in category_name)):
        continue
    print(cell_product_slug)
    pro_slug = str(cell_product_slug).strip()
    pro_slug = pro_slug.lower()

    price1 = sh.cell(row=i, column=8).value
    price2 = sh.cell(row=i, column=9).value
    price3 = sh.cell(row=i, column=10).value
    price4 = sh.cell(row=i, column=11).value
    # price5 = sh.cell(row=i, column=12).value
    # price6 = sh.cell(row=i, column=13).value
    
    # This is so that there are no duplicates in the end list
    new_list_value = [pro_slug, price1, price2, price3, price4]
    if new_list_value in list1:
        continue
    else:
        list1.append(new_list_value)

# Below code is there to quickly eliminate duplicates from list if not using the above method
# unique_list = list(dict.fromkeys(list1))
# print(unique_list)
print(list1)
