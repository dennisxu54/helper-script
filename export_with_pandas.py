# Python code to split the list two element at a time and insert it into excel.
  
# Importing pandas as pd
import pandas as pd
  
# List initialization
list1 = ['10211-clearance', 'a41012', 'a21510', '14012-clearance', 'a49022', 'a41022', '40512-clearance', '40112-clearance', 'ac41412', 'a59513', '40120-clearance', '40114-clearance', '70212-clearance', '41712-clearance', '99102-clearance', '30211-clearance', '60111-clearance', '41722-clearance', '60211-clearance', '40122-clearance', '64014-clearance', '40510-clearance', 'a71514', '40110-clearance', 'ac42912', '99000', 'a59100', '99104-clearance', '44522', '99400-clearance', '10119-clearance', '20211-clearance', '60114-clearance', '99001-clearance', '60111', 'a11519', '40212-clearance', '20113-clearance', '41710-clearance', 'a41312', '41721-clearance', 'ac42412', '10114-clearance', 'a41011', 
'42312-clearance', '99200', '40220-clearance', '99101-clearance', 'ac42812', '20214-clearance', '64011-clearance', '10112-clearance', '44520', '99200-clearance', '10212-clearance', 'a71519', '40111-clearance', 'a49012', 'a59000', '10113-clearance', '24013-clearance', '30111-clearance', 'a11515', 
'60213-clearance', '80211-clearance', '10118-clearance', '14016-clearance', 'a59523', '20116-clearance', 'ac41511', '99103-clearance', '24016-clearance', '99101', '99100-clearance', '40412-clearance', 'a59520', 'a59510', '10116-clearance', '40410-clearance', '99000-clearance', '34011-clearance', 
'70211-clearance', '40210-clearance', '64011']


df = pd.DataFrame()
  
# Creating two columns
df['proper slugs'] = list1
  
# Converting to excel
df.to_excel('Slugs.xlsx', index = False)