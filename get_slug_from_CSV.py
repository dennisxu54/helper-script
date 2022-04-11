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
