
# Python code to split the list two element 
# at a time and insert it into excel.
  
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
df.to_excel('result1.xlsx', index = False)



"""
import pandas as pd

dict1 = {'14017': 'SUITING', '44520': 'SHIRTS', '44522': 'SHIRTS', 'a11515': 'SUITING', 'a11519': 'SEPARATES', 'a21510': 'SUITING', 'a41011': 'SHIRTS', 'a41012': 'SHIRTS', 'a41022': 'SHIRTS', 'a41312': 'SHIRTS', 'a49012': 'POLOS', 'a49022': 'POLOS', 'a59000': 'HEALTH', 'a59100': 'HEALTH', 'a59510': 'KNITWEAR', 'a59513': 'SUITING', 'a59520': 'KNITWEAR', 'a59523': 'SUITING', 'a71514': 'SUITING', 'a71519': 'SEPARATES', 'ac41412': 'SHIRTS', 'ac41511': 'SHIRTS', 'ac42412': 'SHIRTS', 'ac42812': 'SHIRTS', 'ac42912': 'SHIRTS', 'j123ml': 'JACKETS', 'j920l': 'ACTIVEWEAR', 'p608ls': 'POLOS', 'p608ms': 'POLOS', 's119ln': 'SHIRTS', 's231lt': 'SHIRTS', 's231ml': 'SHIRTS', 's505ms': 'SHIRTS', 'zj355': 'WORKWEAR', 'zp902': 'WORKWEAR', 'zt464': 'WORKWEAR', 'zt478': 'WORKWEAR', 'zt566': 'WORKWEAR', 'zw005': 'WORKWEAR', 'zw013': 'WORKWEAR', 'zw350': 'WORKWEAR', '99103-clearance': 'ACCESSORIES', 's266ls-clearance': 'SHIRTS', 's316lt-clearance': 'SHIRTS', 's504lt-clearance': 'SHIRTS', 'k123ls-clearance': 'SHIRTS', 'mv3111b-clearance': 'ACTIVEWEAR', 't968-clearance': 'TEES', '40210-clearance': 'SHIRTS', 'p111ks-clearance': 'POLOS', '99200-clearance': 'ACCESSORIES', 's716lt-clearance': 'SHIRTS', 's416ls-clearance': 'SHIRTS', 't301ks-clearance': 'TEES', 's120ls-clearance': 'SHIRTS', 's313lt-clearance': 'SHIRTS', 'lv3504-clearance': 'KNITWEAR', 's316ll-clearance': 'SHIRTS', 's716ml-clearance': 'SHIRTS', 'zp509-clearance': 'WORKWEAR', 's232ls-clearance': 'SHIRTS', '20211-clearance': 'SUITING', '20113-clearance': 'SUITING', 't29222-clearance': 'TEES', 'h10622-clearance': 'HEALTH', '90111-clearance': 'SUITING', 'f10523-clearance': 'JACKETS', '20116-clearance': 'SUITING', 's306ml-clearance': 'SHIRTS', '10212-clearance': 'SUITING', '20214-clearance': 'SUITING', 's117ll-clearance': 'SHIRTS', 'lb2725-clearance': 'SHIRTS', 's414ll-clearance': 'SHIRTS', 's121ll-clearance': 'SHIRTS', '70211-clearance': 'SUITING', '64014-clearance': 'SUITING', 's306ll-clearance': 'SHIRTS', 'bs29321-clearance': 'SUITING', '10116-clearance': 'SUITING', '41722-clearance': 'SHIRTS', 's122lt-clearance': 'SHIRTS', '42312-clearance': 'SHIRTS', 's121ms-clearance': 'SHIRTS', 'bs243ll-clearance': 'SUITING', 's121ml-clearance': 'SHIRTS', '60114-clearance': 'SUITING', 's316ls-clearance': 'SHIRTS', '14016-clearance': 'SUITING', '10114-clearance': 'SUITING', 'ba95-clearance': 'HOSPITALITY', '14012-clearance': 'SUITING', 'st122k-clearance': 'ACTIVEWEAR', 'p111ls-clearance': 'POLOS', 's306ms-clearance': 'SHIRTS', 'l29122-clearance': 'ACTIVEWEAR', '70212-clearance': 'SUITING', '40512-clearance': 'SHIRTS', '24013-clearance': 'SUITING', '60211-clearance': 'SUITING', 's622ms-clearance': 'SHIRTS', '34011-clearance': 'SUITING', '40220-clearance': 'SHIRTS', 's620ls-clearance': 'SHIRTS', '10119-clearance': 'SUITING', '54011-clearance': 'KNITWEAR', '60213-clearance': 'SUITING', '10112-clearance': 'SUITING', '80211-clearance': 'SUITING', 'lv130ln-clearance': 'KNITWEAR', 's122ls-clearance': 'SHIRTS', 's121lt-clearance': 'SHIRTS', '40120-clearance': 'SHIRTS', '41710-clearance': 'SHIRTS', '99102-clearance': 'ACCESSORIES', 'bs127ll-clearance': 'SUITING', '40212-clearance': 'SHIRTS', 's503lt-clearance': 'SHIRTS', 's262ls-clearance': 'SHIRTS', '50111-clearance': 'KNITWEAR', 's622ml-clearance': 'SHIRTS', 'p606ls-clearance': 'POLOS', 's10422-clearance': 'SHIRTS', 'zc503-clearance': 'WORKWEAR', '99000-clearance': 'ACCESSORIES', 'lb2726-clearance': 'SHIRTS', 's416lt-clearance': 'SHIRTS', 'bs129ls-clearance': 'SUITING', '99104-clearance': 'ACCESSORIES', 't121ks-clearance': 'TEES', 's415ml-clearance': 'SHIRTS', '40410-clearance': 'SHIRTS', 's29422-clearance': 'SHIRTS', 'p10122-clearance': 'POLOS', '10113-clearance': 'SUITING', 'p2100-clearance': 'POLOS', 's261ls-clearance': 'SHIRTS', '41721-clearance': 'SHIRTS', 's29620-clearance': 'SHIRTS', 's622lt-clearance': 'SHIRTS', '40111-clearance': 'SHIRTS', 'p225ls-clearance': 'POLOS', 'h132ml-clearance': 'HEALTH', '60111-clearance': 'SUITING', '99400-clearance': 'ACCESSORIES', '10118-clearance': 'SUITING', '30111-clearance': 'SUITING', 'c412-clearance': 'ACTIVEWEAR', 'h10620-clearance': 'HEALTH', '41712-clearance': 'SHIRTS', '99001-clearance': 'ACCESSORIES', 'p606ms-clearance': 'POLOS', 's415ll-clearance': 'SHIRTS', 'sg302m-clearance': 'ACTIVEWEAR', 's504ml-clearance': 'SHIRTS', 'zc560-clearance': 'WORKWEAR', 'lb2630-clearance': 'SHIRTS', '40114-clearance': 'SHIRTS', 's10421-clearance': 'SHIRTS', 's121ls-clearance': 'SHIRTS', 's415lt-clearance': 'SHIRTS', 'lp10321-clearance': 'KNITWEAR', 's620lt-clearance': 'SHIRTS', 't3110b-clearance': 'TEES', 'lv3125-clearance': 'ACTIVEWEAR', 's122ml-clearance': 'SHIRTS', 't301ls-clearance': 'TEES', 'sg302l-clearance': 'ACTIVEWEAR', 's414ml-clearance': 'SHIRTS', 'zs510-clearance': 'WORKWEAR', '64011-clearance': 'SUITING', '40110-clearance': 'SHIRTS', 'nc10100-clearance': 'ACTIVEWEAR', 'st2010b-clearance': 'ACTIVEWEAR', 's122ms-clearance': 'SHIRTS', '40412-clearance': 'SHIRTS', '40122-clearance': 'SHIRTS', 'tp8815-clearance': 'ACTIVEWEAR', 'mv3111-clearance': 'ACTIVEWEAR', '10211-clearance': 'SUITING', 'p300ls-clearance': 'POLOS', '99101-clearance': 'ACCESSORIES', 's306ls-clearance': 'SHIRTS', 'p225ms-clearance': 'POLOS', 'lb2730-clearance': 'SHIRTS', '24016-clearance': 'SUITING', '40510-clearance': 'SHIRTS', 'h10722-clearance': 'HEALTH', 'lb2625-clearance': 'SHIRTS', 'p2125-clearance': 'POLOS', '40112-clearance': 'SHIRTS', '99100-clearance': 'ACCESSORIES', '30211-clearance': 'SUITING', 's120lt-clearance': 'SHIRTS'}


df = pd.DataFrame(data=dict1, index=[0])

df = (df.T)

print (df)

df.to_excel('tagging.xlsx')

"""
