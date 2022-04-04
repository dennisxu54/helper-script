import openpyxl
from csv import reader


list1 = []

# open file in read mode
with open('biz_collection_au_full.csv', 'r', encoding="utf8") as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        list1.append(row[0])

unique_set = set(list1)
unique_list = list(unique_set)
print(unique_list)



# # load excel with its path
# wrkbk = openpyxl.load_workbook("biz_collection_au_full.csv")

# sh = wrkbk.active
    
# list1 = []
  
# # iterate through excel and display data
# for i in range(2, sh.max_row+1):
#     print("\n")
#     print("Row ", i, " data :")
#     cell_obj = sh.cell(row=i, column=1)
#     # slash_index = cell_obj.value.index('/')
#     # product_code = cell_obj.value[:slash_index].strip()
#     # list1.append(product_code)
#     # print(cell_obj.value.split()[0])
#     print(cell_obj.value)

# # unique_set = set(list1)
# # unique_list = list(unique_set)
# # print(unique_list)
