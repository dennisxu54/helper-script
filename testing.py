
from datetime import datetime
# from pytz import timezone
import zoneinfo

# format = '%Y-%m-%d %H:%M:%S %Z%z'
# auckland_timezone = zoneinfo.ZoneInfo('Pacific/Auckland')
# print(auckland_timezone)
# local_datetime = datetime.now().astimezone(auckland_timezone)
# # local_datetime = datetime.replace(tzinfo=datetime.timezone.utc)
# # local_datetime = local_datetime.replace(tzinfo=datetime.timezone.utc)
# log_time = local_datetime.strftime(format)
# print(log_time)

# auckland_timezone = timezone('Pacific/Auckland')
# print(auckland_timezone)
# local_datetime = auckland_timezone.localize(datetime.now())
# log_time = local_datetime.strftime(format)
# print(log_time)

# sizes = ["XXS", "XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL", "6XL", "7XL", "2", "4", "6", "8", "10", "12", "14", "16", 
#       "18", "20", "22", "24", "26", "28", "30", "72", "77", "82", "87", "92", "97", "102", "107", "112", "117", "122", "127", "132", "137", "142"]

# list1 = ['']

# list2 = []

# print(len(list2))


# first_element = list1[0] if list1 else ''
# for single_tag in first_element.split(","):
#     print("first element", single_tag)

# second_element = list2[0] if list2 else ''
# for single_tag in second_element.split(","):
#     print("second element", single_tag)



# print(first_element)
# print(second_element)
# print(bool(first_element))
# print(bool(second_element))
# print(bool(list2))
# print(bool(list1))
# print(bool(''))


some_json = {
    "customer_no": "TESTWEB",
    "price": "11.5",
    "currency": "NZD",
    "items": [
        {
            "sku": "9401042681867",
            "formattedItemNo": "ZH731   /Z38/10",
            "size": "10",
            "eta": [
                {
                    "eta": "Pending ETA",
                    "quantity": 0
                }
            ],
            "stock": [
                {
                    "location": "AUK",
                    "qtyAvailable": 223.0
                }
            ]
        }
    ]
}
quantity = 300
stock_level = some_json['items'][0]['stock']
stock_amount = 0

for item in stock_level:
    stock_warehouse = item['qtyAvailable']
    stock_amount += stock_warehouse

backorder_amount = stock_amount - quantity

if backorder_amount > 0:
    backorder_quantity = 0
else:
    backorder_quantity = backorder_amount * -1

print(backorder_quantity)