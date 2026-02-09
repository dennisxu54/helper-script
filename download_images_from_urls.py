# Import the os module
import os
import requests

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
# folder_path  = os.chdir('C:/Work/Honeybee container/honeybee/products/management/data/WIP/Images/Biz Care/Part 2')
output_dir = "images"
os.makedirs(output_dir, exist_ok=True)

# Print the folder_path
print("Current working directory: {0}".format(os.getcwd()))

# Print the type of the returned object
print("os.getcwd() returns an object of type: {0}".format(type(os.getcwd())))

slug_list = ['https://cdn.fashionbizapps.nz/honeybee/images/44210_bProduct_Black_02_PsTm8lU.jpg']
for url in slug_list:
    filename = url.split("/")[-1]
    filepath = os.path.join(output_dir, filename)

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    with open(filepath, "wb") as f:
        f.write(response.content)

    print(f"Downloaded {filename}")
