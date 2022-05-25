# Import the os module
import os

# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))

# Print the type of the returned object
print("os.getcwd() returns an object of type: {0}".format(type(cwd)))

#------------------------------------------------------------------------

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))

# Change the current working directory. Need the "/" instead of "\"
os.chdir('C:/Work/Honeybee container/honeybee/products/management/data/reshoot colour')

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))

#------------------------------------------------------------------------
print("------------------------------------------------------------------------")
folder_path  = os.chdir('C:/Work/Honeybee container/honeybee/products/management/data/reshoot colour')

list1 = []

for file in os.listdir(folder_path):
    file_name = file.split('.')[0].lower()
    file_name_list = file_name.split('_')
    last_part = file_name_list[-1]
    """
    if len(file_name_list) >= 5:
        print("These products have need of colour name fix " + file_name)
    elif last_part == '01':
        continue
    elif last_part == '02':
        continue
    else:
        print("These products have no 01 or 02 " + file_name)
    """
    list1.append(file_name_list[0])

print((list1))
    

