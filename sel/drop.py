import pandas
from collections import Counter
data = pandas.read_excel(r'D:\rafsangan\rafsanjan27_region_rafsanjan.xlsx')
# print(data)
df2 = data[data.region.notnull()]
df2.to_excel('remove.xlsx')