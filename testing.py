
from datetime import datetime
# from pytz import timezone
import zoneinfo

format = '%Y-%m-%d %H:%M:%S %Z%z'
auckland_timezone = zoneinfo.ZoneInfo('Pacific/Auckland')
print(auckland_timezone)
local_datetime = datetime.now().astimezone(auckland_timezone)
# local_datetime = datetime.replace(tzinfo=datetime.timezone.utc)
# local_datetime = local_datetime.replace(tzinfo=datetime.timezone.utc)
log_time = local_datetime.strftime(format)
print(log_time)

# auckland_timezone = timezone('Pacific/Auckland')
# print(auckland_timezone)
# local_datetime = auckland_timezone.localize(datetime.now())
# log_time = local_datetime.strftime(format)
# print(log_time)

# sizes = ["XXS", "XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL", "6XL", "7XL", "2", "4", "6", "8", "10", "12", "14", "16", 
#       "18", "20", "22", "24", "26", "28", "30", "72", "77", "82", "87", "92", "97", "102", "107", "112", "117", "122", "127", "132", "137", "142"]

# list1 = []

# random_list = ["10", "12", "20", "22", "24", "26", "8", "6", "14"]

# for x in range(len(random_list)):
#     list1.insert(sizes.index(random_list[x]), random_list[x])
# print(list1)



# if "H" in sizes:
#     number = sizes.index("H")


