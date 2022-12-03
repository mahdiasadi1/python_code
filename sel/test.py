def isWordPresent(sentence, word):
    # To break the sentence in words
    s = sentence.split(" ")

    for i in s:

        # Comparing the current word
        # with the word to be searched
        if (i == word):
            return True
    return False

data = pandas.read_excel(r'D:\rafsangan\rafsanjan2_remove_qmark.xlsx')
data1 = pandas.read_excel(r'D:\rafsangan\rafsanjan23_cover.xlsx')
df=pandas.DataFrame(data,columns=['تلفن','آدرس'])
df1=pandas.DataFrame(data1,columns=['phone'])
address=df['آدرس'].to_dict()
oldphones =df['تلفن'].to_dict()
phones=df1['phone'].to_dict()
region ={}