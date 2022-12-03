import pandas
def convert_code(x):
# x=input('input your number? ')
    if x.isnumeric() :
        if len(x) == 7:
            y=x[:3]
            z=x[3:]
            # print(y)
            # print(z)
            if y=='322':
               y='3432'
            elif y == '323':
                y='3433'
            elif y=='422':
                y = '3422'
            elif y== '822':
                y = '3428'
            elif y =='522':
                y = '3425'
            elif y=='523':
                y = '3426'
            return y+z
        return ('input just 7 digit number' )
    return ('please input number')
# code=input('input your number? ')
# final=convert_code(code)
# print(final)
data = pandas.read_excel(r'C:\Users\asadi\Downloads\rafsanjan.xlsx')
df=pandas.DataFrame(data,columns=['تلفن'])
phones=df.to_dict()
# print(phones)
phone=phones['تلفن']
for i in phone:
    print(phone[i])
    x=str(phone[i])
    # print(type(x))

    if x.isnumeric():
        if len(x)==7:
            c=convert_code(x)
            df.loc[i]=c

print (df)
writer=pandas.ExcelWriter('phones.xlsx')
df.to_excel(writer)
writer.save()
