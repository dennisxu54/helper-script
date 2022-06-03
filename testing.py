sizes = ["XXS", "XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL", "6XL", "7XL", "2", "4", "6", "8", "10", "12", "14", "16", 
      "18", "20", "22", "24", "26", "28", "30", "72", "77", "82", "87", "92", "97", "102", "107", "112", "117", "122", "127", "132", "137", "142"]

list1 = []

random_list = ["20", "72", "XXS"]

for x in range(len(random_list)):
    list1.insert(sizes.index(random_list[x]), random_list[x])
print(list1)



if "H" in sizes:
    number = sizes.index("H")


