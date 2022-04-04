# import module
import openpyxl
import math
  
# load excel with its path
wrkbk = openpyxl.load_workbook("Biz Collection - Sizing.xlsx", data_only=True)

sh = wrkbk["Sheet1"]

list1 = []
myDict = {}
  
# iterate through excel and display data
for i in range(2, 920):
    print("\n")
    print("Row ", i, " data :")
      
    cell_product_slug = sh.cell(row=i, column=2).value
    if cell_product_slug == " " or cell_product_slug == None or cell_product_slug == "-":
        continue
    print(cell_product_slug)
    #pro_slug = cell_product_slug.split(" ", 1)
    #key = pro_slug[0].lower()
    #key = str(cell_product_slug).lower() 
    key = str(cell_product_slug)
    if "Lemgth" in key:
        key = key.replace("Lemgth", "Length")
    if "lenght" in key:
        key = key.replace("lenght", "Length")
    if "Lenghth" in key:
        key = key.replace("Lenghth", "Length")
    if "length" in key:
        key = key.replace("length", "Length")
    if "Legth" in key:
        key = key.replace("Legth", "Length")
    if "Lenth" in key:
        key = key.replace("Lenth", "Length")
    if "SLeeve" in key:
        key = key.replace("SLeeve", "Sleeve")
    if "CENtre" in key:
        key = key.replace("CENtre", "Centre")
    if "  " in key:
        key = key.replace("  ", " ")
    if "form" in key:
        key = key.replace("form", "From")
    if "from" in key:
        key = key.replace("from", "From")
    if "fro" in key:
        key = key.replace("fro", "From")
    if "From From" in key:
        key = key.replace("From From", "From")
    if "HSP(CM)" in key:
        key = key.replace("HSP(CM)", "HSP (CM)")
    if "CNB" in key:
        key = key.replace("CNB", "CBN")
    if "\n" in key:
        key = key.replace("\n", "")
    if "back" in key:
        key = key.replace("back", "Back")
    if " ( CM)" in key:
        key = key.replace(" ( CM)", " (CM)")
    if "(CM)" not in key:
        key = key + " (CM)"
    if "  (CM)" in key:
        key = key.replace("  (CM)", " (CM)")
    if "FromHSP" in key:
        key = key.replace("FromHSP", "From HSP")
    if "FromLSP" in key:
        key = key.replace("FromLSP", "From LSP")
    if "Bdoy" in key:
        key = key.replace("Bdoy", "Body")
    if "1/2" in key:
        key = key.replace("1/2", "½")


    #cell_tier_price1 = sh.cell(row=i, column=8).value
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

    new_list_value = key

    list1.append(new_list_value)

    
    """
    if key in myDict:
        continue
    else:
        myDict[key] = value
    """

#if you do want a unique list with no duplicates, remember to remove square brackets from above
unique_list = list(dict.fromkeys(list1))
print(unique_list)

