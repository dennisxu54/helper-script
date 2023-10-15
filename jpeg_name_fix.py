# Import the os module
import os

### IMPORTANT: Below are commands to check the working directory to see if you are in the correct one

#------------------------------------------------------------------------
# # Get the current working directory
# cwd = os.getcwd()

# # Print the current working directory
# print("Current working directory: {0}".format(cwd))

# # Another print the current working directory
# print("Current working directory: {0}".format(os.getcwd()))

# # Print the type of the returned object
# print("os.getcwd() returns an object of type: {0}".format(type(cwd)))

# # Change the current working directory. Need the "/" instead of "\"
# os.chdir('C:/Work/Honeybee container/honeybee/products/management/data/')

#------------------------------------------------------------------------

print("------------------------------------------------------------------------")
folder_path  = os.chdir('C:/Work/Honeybee container/honeybee/products/management/data/Image')

# Print the folder_path
print("Current working directory: {0}".format(os.getcwd()))

# Print the type of the returned object
print("os.getcwd() returns an object of type: {0}".format(type(os.getcwd())))

slug_list = []

for file in os.listdir(folder_path):
    file_name = file.split('.')[0]
    file_name_list = file_name.split('_')
    rename_item = file_name_list[1]
    if rename_item.lower() == "talent":
        replace_rename_item = "aTalent"
    elif rename_item.lower() == "product":
        replace_rename_item = "bProduct"
    else:
        continue
    slug_list.append(file_name_list[0])
    print("File name before replace: ", file)
    os.rename(file, file.replace(rename_item, replace_rename_item))
    print("File name after replace:  ", file.replace(rename_item, replace_rename_item))
    print("-------------------------------------------")

print(list(set(slug_list)))



    # if len(file_name_list) >= 5:
    #     print("These products have need of colour name fix " + file_name)
    # elif last_part == '01':
    #     continue
    # elif last_part == '02':
    #     continue
    # else:
    #     print("These products have no 01 or 02 " + file_name)


    

