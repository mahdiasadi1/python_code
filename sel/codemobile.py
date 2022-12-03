import pandas
from collections import Counter
data = pandas.read_excel(r'D:\rafsangan\rafsanjan28_remove_other_region.xlsx')
df=pandas.DataFrame(data,columns=['mobile'])
# phones=df.to_dict()
mobiles=df['mobile'].to_dict()
# print(str(int(mobiles[0])))
print(df[df['mobile'].isnull()])
df['mobile'] = pandas.to_numeric(df['mobile'], errors='coerce')
df = df.dropna(subset=['mobile'])
df['mobile'] = df['mobile'].astype(int)
print(df['mobile'])

for i in mobiles:
        if( str(int(mobiles[i]))):
            x=str(int(mobiles[i]))
            length = len(x)
            if (length==10):
                df.loc[i]="0098" + x


writer=pandas.ExcelWriter('international_mobile.xlsx')
df.to_excel(writer)
writer.save()