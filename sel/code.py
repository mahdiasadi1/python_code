import pandas
from collections import Counter
data = pandas.read_excel(r'D:\rafsangan\rafsanjan28_remove_other_region.xlsx')
df=pandas.DataFrame(data,columns=['phone'])
# phones=df.to_dict()
phones=df['phone'].to_dict()

for i in phones:
    x = str(phones[i])
    length = len(x)
    # print(phones[i])
    if (length==8):
        df.loc[i]="009834"+x
    elif(length==10):
        df.loc[i]="0098"+x

writer=pandas.ExcelWriter('international_phones.xlsx')
df.to_excel(writer)
writer.save()