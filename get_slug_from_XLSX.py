# import module
import openpyxl
import math
  
# load excel with its path
wrkbk = openpyxl.load_workbook("2022 Biz Collection_NZ Pricelist Reseller_01-2022.xlsx", data_only=True)

# Make sure the sheet name is same as on the excel
sh = wrkbk["Sheet1"]

list1 = []
myDict = {}
  
# iterate through excel and display data
for i in range(3, 737):
    print("\n")
    print("Row ", i, " data :")
      
    cell_product_slug = sh.cell(row=i, column=2).value
    if cell_product_slug == " " or cell_product_slug == None or cell_product_slug == "Style" or cell_product_slug == "STYLE":
        continue
    if cell_product_slug == "WORKS PANTS & SHORTS" or cell_product_slug == "ENGINEERED OUTERWEAR" or cell_product_slug == "OVERALLS" or cell_product_slug == "FIRE ARMOUR":
        continue
    if cell_product_slug == "POLOS" or cell_product_slug == "TEES" or cell_product_slug == "SHIRTS" or cell_product_slug == "BIZ SEPARATES" or cell_product_slug == "KNITWEAR":
        continue
    if cell_product_slug == "HOODIES & FLEECE" or cell_product_slug == "ACTIVEWEAR" or cell_product_slug == "JACKETS" or cell_product_slug == "HOSPITALITY" or cell_product_slug == "HEALTH & BEAUTY":
        continue
    if cell_product_slug == "HEALTHWEAR" or cell_product_slug == "CASUALWEAR" or cell_product_slug == "TOPS" or cell_product_slug == "SEPARATES":
        continue
    print(cell_product_slug)
    pro_slug = cell_product_slug.strip()
    pro_slug = pro_slug.lower()
    #key = pro_slug[0].lower()
    #key = str(cell_product_slug).lower() 
    #key = str(cell_product_slug)

    cell_tier_price1 = sh.cell(row=i, column=7).value
    #cell_tier_price2 = sh.cell(row=i, column=7).value
    #cell_tier_price3 = sh.cell(row=i, column=8).value
    """
    cell_tier_price1 = cell_tier_price1.lower()
    cell_tier_price2 = sh.cell(row=i, column=8).value
    cell_tier_price3 = sh.cell(row=i, column=9).value
    
    if cell_tier_price == None:
        continue
    if type(cell_tier_price) == float:
        pass
    else:
        cell_tier_price = float(cell_tier_price[1:])
    """
    #value = [cell_tier_price, cell_tier_price*2]
    #print(value)
    """
    if cell_tier_price1:
        features = cell_tier_price1.split(";")
    else:
        features = ""
    """
    
    new_list_value = [pro_slug, cell_tier_price1]
    list1.append(new_list_value)

#if you do want a unique list with no duplicates, remember to remove square brackets from above
#unique_list = list(dict.fromkeys(list1))
#print(unique_list)
print(list1)

