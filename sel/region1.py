def isWordPresent(sentence, word):
    # To break the sentence in words
    s = sentence.split(" ")

    for i in s:

        # Comparing the current word
        # with the word to be searched
        if (i == word):
            return True
    return False
import re
def islocal(address,places):
    for place in places:
        if re.search(place,address):
            return True
    return False
import pandas
# import re
from collections import Counter
data = pandas.read_excel(r'D:\rafsangan\rafsanjan2_remove_qmark.xlsx')
data1 = pandas.read_excel(r'D:\rafsangan\rafsanjan23_cover.xlsx')
df=pandas.DataFrame(data,columns=['تلفن','region','آدرس'])
df1=pandas.DataFrame(data1,columns=['phone'])
address=df['آدرس'].to_dict()
oldphones =df['تلفن'].to_dict()
phones=df1['phone'].to_dict()
region =df['region'].to_dict()
# khenaman = ['آب ترش' ,'علی آباد' ,'ارجاس','باب کهکین','چاروک','دوازده امام','ده بالا','ده کربلایی رضا','ده ساردی','ده شهلا','گلوسالار',' حاجی‌آباد',' هنزاف','حسن‌آباد دهنو','کاخ','خالق‌آباد','خنامان','خمرودوئیه','رییس آباد','رضاآباد','روکرد','سعیدآباد','ولی‌آباد','ظهرکوه']
# azadegan = ['ابراهیم‌آباد شور' ,'اسلامیه' ,'عیش‌آباد' ,'فردوسیه' ,'حسین‌آباد علی اکبرخان' ,'جعفرآباد' ,'لطف‌آباد شور' ,'محمودیه بهرامی' ,'مهدی‌آباد معاون' ,'محمدآباد مختار' ,'محی آباد' ,'موسی‌آباد' ,'قایمیه' ,'رضاآباد',' تاج‌آباد' ,'تاج‌آباد کهنه','ابراهیم‌آباد حاجی','دهنو جهانگیرخان','بهروزیه','اکبرآباد هجری',' اکبرآباد برخوردار','عباس‌آباد آغفور']
# kabootarkhan = [ 'کبوترخان', 'عباس‌آباد','عبدالله‌آباد' ,'فرودگاه' ,'حاجی‌آباد' , 'کبوترخان' ,'کریم‌آباد علیا' ,'مزرعه جوادالائمه مزرعه کیوی' ,'محمدآباد میثم' ,'مجتمع صنعتی رفسنجان' ,'ناصریه بالا' ,'نازی‌آباد' ,'قاسم‌آباد' ,'کارخانه سیمان رفسنجان' ,'سعیدآباد شفیع‌پور' ,'توکل‌آباد رنجبر' ,'تلمبه عباس صالحی' ,'تلمبه افراز' ,'تلمبه احمد سلطانی' ,'تلمبه علی عسکری' ,'تلمبه ارسطو ایرانی' ,'تلمبه دانشجو' ,'تلمبه ده پناه' ,'تلمبه همدانی' ,'تلمبه حسن علی محمد' ,'تلمبه حسین غفور' ,'تلمبه مهدیه دق کبوترخان' ,'تلمبه مرتضوی' ,'تلمبه سیدرضا علوی' ,'تلمبه سیدآباد دق کبوترخان' ,'تلمبه سلطانی' ,'وسیل‌آباد']
# daredoran = ['علی‌آباد دره دور' ,'دره دور' ,'دره رنج' ,'دره جوز' ,'داوران' ,'ده تک' ,'سنجدوییه', 'اودرج' ]
# eslamie=['عباس‌آباد معین' ,'احمدآباد رضوی' ,'ده ظهیر' ,'ده نو' ,'دولت‌آباد' ,'امامزاده رضا' ,'اسلام‌آباد' ,'اسماعیل‌آباد' ,'حسن‌آباد' ,'حسن‌آبادنوش‌آباد' ,'همت‌آباد آگاه' ,'هرمزآباد' ,'حسین‌آباد نژادی' ,'جنت‌آباد' ,'کاظم‌آباد' ,'کوثرریز' ,'مخازن نفت' ,'مزرعه رضوی' ,'موتور تاکسیداران' ,'رحیم‌آباد اگاه' ,'رییس‌آباد' ,'سعادت‌آباد' ,'صفی‌آباد' ,'شهرآباد' ,'تلمبه وکیل‌آباد دیانتی' ,'وکیل‌آباد' ,'یوسف‌آباد' ]
# ghasemabad = ['علی‌آباد انقلاب' ,'علی‌آباد مفت‌آباد' ,'عرب آباد' ,'بهارستان' ,'فرخ‌آباد' ,'قاسم‌آباد حاجی' ,'فتح‌آباد',  'همت‌آباد علیا' ,'حسین‌آباد شفیعی' ,'ملک‌آباد' ,'مهدی‌آباد امینیان' ,'مهدی‌آباد سردار' ,'مهدی‌آباد واحد' ,'محمدیه' ,'عباس‌آباد حاجی','نوبهار' ,'زین‌آباد']
# razmavaran = ['علم آباد' ,'دهن‌آباد'  ,'خرم‌آباد' ,'کورگه' ,'لاهیجان' ,'محمودیه' ,'محمدآباد دهنو' ,'ده نو' ,'مظفرآباد' ,'نظم‌آباد' ,'قوام‌آباد' ,'قدرت‌آباد' ,'سعیدآباد'  ,'سجادیه']
# sarcheshmeh =[ 'سرچشمه','عباس‌آباد علیا',  'اکبرآباد', 'بیدزرین سفلی', 'چشمه کبک', 'دره گرم', 'ده پشته', 'ده سیاهان علیا', 'ده سیاهان سفلی', 'دهوییه', 'گروئیه بالا', 'گلیلون', 'گود احمر سفلی', 'حسن‌آباد خانم وکیلی', 'جودعوائی', 'کم زرد', 'خوری' , 'کهن‌ترش', 'لابید سفلی', 'لنگر', 'مانی علیا', 'مغوئیه', 'محمدآباد', 'هنسیج علیا', 'نی‌زار', 'الاغ‌چین' ,'اوراف', 'پاقلعه', 'رضوئیه', 'رودین', 'معدن مس سرچشمه', 'ساردی', 'تلاتوئیه', 'تیربید', 'یوسف‌آباد'  ]
# koshku =['كشكوئيه', 'کشکوئیه','کشکوییه','احمدآباد فلاح' ,'احمدآباد دیفه خشک', 'علی‌آباد سادات' ,'امیرآباد کشاورزان' ,'بهجت‌آباد' ,'دهنه درکال' ,'دیفه‌آقا' ,'احسان‌آباد', 'گل‌آذر'  ,'حسن‌آباد نواب' ,'حسن‌آباد زندی' , 'کریم‌آباد','خالق‌آباد' ,'مهدی‌آباد شرکا' ,'محمدآباد محمدنوقی'  ,'موتور صفائیه' ,'نعمت‌آباد' ,'زیرکوه' ,'نورآباد', 'قاسم‌آباد کشکوئیه'  ,'رحمت‌آباد معین‌زاده' ,'رضاآباد نواب' ,'روستای عباس‌آباد' ,'تلمبه عباس‌آباد' ,'تلمبه احمدآباد' ,'تلمبه علی اسدی' ,'تلمبه علی‌آباد' ,'تلمبه علی‌آباد شرکا','تلمبه دورکی' ,'تلمبه گلستان سرجنگل', 'تلمبه گلشن' ,'تلمبه حجتیه' ,'تلمبه حسین‌آقا' , 'تلمبه کاظم‌آباد' ,'تلمبه منظریه' ,'تلمبه مهدی‌آباد', 'تلمبه محمد اسدی' ,'تلمبه صالحی'   ,'یوسف‌آباد کشکوئیه' , 'زندیه','عباس‌آباد امین']
# raviz = [  'بلک' ,'بندوان' ,'دام بهایی' ,'دره کردی' ,'دستوییه' ,'دهوئیه' ,'اسطاهوییه' ,'فدیج' ,'حوم‌الدین' ,'جلال‌آباد' ,'کهن رزان' ,'خیسوییه' ,'مهاجری' ,'مهجرد' ,'منصورآباد' ,'نیمجردوییه' ,'پاکش' ,'پشتکوه' ,'پورکان' ,'رشوان' ,'رودین کشکوئیه' ,'صدرآباد', 'شادی‌آباد', 'سیراب', 'زهروییه'   ]
# sharifabad=['احمدآباد هرندی' ,'علی‌آباد شهید' ,'بهمن‌آباد' ,'حسین‌آباد' ,'محمودآباد' ,'محمدآباد ساقی' ,'شریف‌آباد' ,'تقی‌آباد' ,'وکیل‌آباد کشکوئیه' ]
# bahreman= ['نوق', 'عباس‌آباد فلاح' ,'احمدآباد فلاح' ,'احمدیه' ,'علی‌آباد' ,'امیرآباد', 'باقرآباد', 'دقوق آباد', 'حاجی‌آباد', 'حسین‌آباد امامی', 'جنت‌آباد نوق', 'جوادیه الهیه', 'کریم‌آباد نوق', 'خالق‌آباد نوق' , 'محمدآباد برخوردار', 'محمدآباد', 'سیدجلال' ,'نجم‌آباد' ,'روامهران' ,'رضاآباد نوق', 'صدرآباد نوق', 'تلمبه همت‌آباد', 'تلمبه حیدرآباد','تلمبه حسن‌آباد', 'تلمبه محمودآباد زینلی', 'تلمبه محمدیه', 'تلمبه روزكوه رو', 'تلمبه صفائیه', 'تلمبه سمیعی', 'یدالله‌آباد', 'یحیی‌آباد', 'زانوق آباد' ,'بهرمان']
# rezvan=[ 'احمدآباد فردوس' ,'چشمه سفید' ,'اسماعیل‌آباد فردوس' ,'فیض‌آباد' ,'حسن‌آباد فردوس' ,'جعفرآباد فردوس' ,'جهان‌آباد' ,'کمال‌آباد' ,'محمودیه فردوس' ,'نعمت‌آباد' ,'رحمت‌آباد' ,'سیدجلال الدین' ,'شمس‌آباد' ,'شجاع‌آباد پایین' ]
# ferdos=[  'صفائیه','صفاییه','فردوس','علی‌آباد فردوس', 'علی‌آباد هراتی', 'ده محمد مرتضوی', 'دولت‌آباد فردوس',  'جنت مرتضوی', 'جوادیه مرتضوی', 'مهدی‌آباد', 'محمدآباد هراتی', 'موتور حسن‌آباد حمیدیه جوانان', 'ناصح‌آباد', 'قائمیه', 'رکن‌آباد', 'تلمبه احمدآباد', 'تلمبه اسدآباد', 'تلمبه باقرآباد', 'تلمبه بوستان', 'تلمبه امامیه', 'تلمبه فاطمیه', 'تلمبه حسن‌آباد', 'تلمبه حسین‌آباد', 'تلمبه حسین‌آباد فهرجی', 'تلمبه کاظم‌آباد', 'تلمبه شاه‌پسند', 'تلمبه تقی‌آباد', 'تلمبه وارسته' ]
# hoseinabad=[  'عباس‌آباد', 'احمدآباد', 'احمدآباد عطائی', 'علی‌آباد حسن', 'امین‌آباد', 'اسدآباد', 'ده حیدر', 'ده رییس', 'فدک', 'گلستان', 'گلشن', 'جلالیه', 'هجری', 'جمشیدآباد', 'خالق‌آباد', 'محمدآباد خواجه', 'نصرت‌آباد', 'قاسم‌آباد', 'قربان‌آباد', 'رضاآباد', 'شریف‌آباد', 'تلمبه حاجی‌آباد', 'تلمبه صدرآباد', 'تلمبه صفاییه', 'تراب' ]
# bayaz=[   'اسدآباد رهنما', 'اشرف‌آباد', 'بیاض', 'بهشت‌آباد', 'فخرآباد', 'گیتی‌آباد', 'حمیدآباد', 'حسن‌آباد', 'همت‌آباد', 'حجت‌آباد', 'حسین‌آباد اسلامی', 'لطف‌آباد', 'مجیدآباد', 'مهدی‌آبادامین', 'مهرآباد', 'محمدآباد', 'سبزدشت', 'صفائیه', 'شفیع‌آباد', 'شام‌آباد', 'توکل‌آباد', 'تلمبه احمدآباد'  ]
# print(phones[8541])
# print(oldphones[8541])
# j=0
for i in oldphones:

    x=str(oldphones[i])
    length=len(x)
    # if re.search("^9",x) or re.search("nan",x):
    # myaddress = address[i]
    # if islocal(str(address[i]),khenaman):
    #     region[i]='خنامان'
    # elif islocal(str(address[i]), azadegan):
    #     region[i] = 'آزادگان'
    # elif islocal(str(address[i]), kabootarkhan):
    #     region[i] = 'کبوترخان'
    # elif islocal(str(address[i]), daredoran):
    #     region[i] = 'دره دران'
    # elif islocal(str(address[i]), eslamie):
    #     region[i] = 'اسلامیه'
    # elif islocal(str(address[i]), ghasemabad):
    #     region[i] = 'قاسم آباد'
    # elif islocal(str(address[i]), razmavaran):
    #     region[i] = 'رزم آوران'
    # elif islocal(str(address[i]), sarcheshmeh):
    #     region[i] = 'سرچشمه'
    # elif islocal(str(address[i]), koshku):
    #     region[i] = 'کشکوئیه'
    # elif islocal(str(address[i]), raviz):
    #     region[i] = 'راویز'
    # elif islocal(str(address[i]), sharifabad):
    #     region[i] = 'شریف آباد'
    # elif islocal(str(address[i]), bahreman):
    #     region[i] = 'بهرمان'
    # elif islocal(str(address[i]), rezvan):
    #     region[i] = 'رضوان'
    # elif islocal(str(address[i]), ferdos):
    #     region[i] = 'فردوس'
    # elif islocal(str(address[i]), hoseinabad):
    #     region[i] = 'حسین آباد انار'
    # elif islocal(str(address[i]), bayaz):
    #     region[i] = 'بیاض'
    # elif islocal(str(address[i]),[ 'رفسنجان' ]):
    #     region[i]='رفسنجان'

    if (length == 7):
        y = x[:3]
        # if (y == '372' or y == '368' or y=='375'):
        #     region[i] = 'بهرمان'
        # if(y=='378' or y=='362' or y=='367'):
        #     region[i]='فردوس'
        # if(y=='364'or y=='376'):
        #     region[i]='رضوان'
        # if(y=='262' or y=='273' or y=='272'):
        #     region[i] = 'کشکوئیه'
        # if(y=='342' or y=='267' or y=='265'):
        #     region[i]='شریف آباد'
        # if(y=='274'):
        #     region[i]='راویز'
        # if(y=='322' and islocal(address[i],['انار'])):
        #     region[i]='انار'
        # if(y=='347' or (y=='342' and  islocal(address[i],bayaz))):
        #     region[i]='بیاض'
        # if(y=='332' or y=='334'):
        #     region[i]='حسین آباد انار'
        if(y=='422' or y=='423' or y=='425' or y=='522' or y=='523' or y=='524' or y=='822' or y=='823' or y=='222'
           or y=='288' or y=='322' or y=='323' or y=='622' or y=='325'):
            region[i]='رفسنجان'
        # if(y=='242' or y=='245' or y=='228'):
        #     region[i]='خنامان'
        # if(y=='237' or y=='238' or y=='227'):
        #     region[i]='آزادگان'
        # if(y=='232' or y=='244'):
        #     region[i]='کبوترخان'
        # if(y=='246' or y=='235' or y=='243'):
        #     region[i]='دره دران'
        # if(y=='225'):
        #     region[i]='اسلامیه'
        # if(y=='223' ):
        #     region[i]='قاسم آباد'
        # if(y=='236'):
        #     region[i]='رزم آوران'
        # if(y=='282' or y=='288'):
        #     region[i]='سرچشمه'




    elif(length == 10):
        y=x[:6]
        # if (y =='392372' or y=='392368' or y=='392375' or (y == '343416' and islocal(address[i],bahreman))):
        #     region[i] = 'بهرمان'
        # if (y == '392378' or y == '392362' or y == '392367' or (y=='343417' and islocal(address[i],ferdos))):
        #     region[i]='فردوس'
        # if((y=='392376'or y=='392364') or (y=='343416' and islocal(address[i],rezvan))
        #      or (y=='343417' and islocal(address[i],rezvan))):
        #     region[i]='رضوان'
        # if (y == '392262' or y == '392273' or y == '392272') or (y=='343439' and islocal(address[i],koshku)):
        #     region[i] = 'کشکوئیه'
        # if (y == '392342' or y == '392267' or y == '392265' or (y=='343418' and islocal(address[i],sharifabad))
        #         or(y=='343436' and islocal(address[i],sharifabad))or (y=='343439' and islocal(address[i],sharifabad))):
        #     region[i] = 'شریف آباد'
        # if(y=='392274' or (y=='343436' and islocal(address[i],raviz))):
        #     region[i]='راویز'
        # if(y=='392322' or y=='343438'):
        #     region[i]='انار'
        # if (y == '392347' or (
        #         y == '392342' and islocal(address[i],bayaz))
        #     or (y=='343418') and islocal(address[i],bayaz)):
        #     region[i] = 'بیاض'
        # if (y == '392332' or y == '392334' or
        #         (y=='343418' and islocal(address[i],hoseinabad)) or
        #    (y=='343439' and islocal(address[i],hoseinabad))):
        #     region[i] = 'حسین آباد انار'
        if (
                y == '391422' or y == '391423' or y == '391425' or y == '391522' or y == '391523' or y == '391524' or y == '391822' or y == '391823' or y == '391222'
                or y == '391288' or y == '391322' or y == '391323' or y == '391622' or y == '391325'
                 or y=='343422' or y=='343423' or y=='343424' or y=='343425' or y=='343426' or y=='343427'
                 or y=='343428' or y=='343429' or y=='343432' or y=='343433' or y=='343434' or y=='343435'):
            region[i] = 'رفسنجان'
        # if(y=='391242' or y=='391228' or y=='391245' or (y=='343419' and islocal(address[i],khenaman) ) or (y=='343421'and islocal(address[i],khenaman))):
        #     region[i]='خنامان'
        # if(y=='391238' or y=='391237' or y=='391227' or (y=='343421' and islocal(address[i],azadegan)) or (y=='343436'and islocal(address[i],azadegan))):
        #     region[i]='آزادگان'
        # if(y=='391244' or y=='391232' or (y=='343419' and islocal(address[i],kabootarkhan))):
        #     region[i]='کبوترخان'
        # if(y=='391235' or y=='391246' or y=='243' or (y=='343419' and islocal(address[i],daredoran)) or (y=='343421' and islocal(address[i],daredoran))or (y=='343437' and islocal(address[i],daredoran))):
        #     region[i]='دره دران'
        # if(y=='391225' or (y=='343421' and islocal(address[i],eslamie))):
        #     region[i]='اسلامیه'
        # if( y=='391223' or (y=='343437' and islocal(address[i],ghasemabad))):
        #     region[i]='قاسم آباد'
        # if(y=='391236' or (y=='343419' and islocal(address[i],razmavaran))):
        #     region[i]='رزم آوران'
        # if(y=='391282' or y=='391288' or y=='343431'):
        #     region[i]='سرچشمه'

    elif(length ==8):
        y=x[:4]
        # if(y=='3416' and islocal(address[i],bahreman)):
        #     region[i] = 'بهرمان'
        # if(y=='3417' and islocal(address[i],ferdos)):
        #     region[i]='فردوس'
        # if(y=='3416' and islocal(address[i],ferdos)):
        #     region[i]='فردوس'
        # if(y=='3417' and islocal(address[i],rezvan) or (y=='3416' and islocal(address[i],rezvan))):
        #     region[i]='رضوان'
        # if(y=='3439' and islocal(address[i],koshku)):
        #     region[i] = 'کشکوئیه'
        # if  (y == '3418' and islocal(address[i],sharifabad)
        #         or (y == '3436' and islocal(address[i],sharifabad)) or (
        #         y == '3439' and islocal(address[i],sharifabad))):
        #     region[i] = 'شریف آباد'
        # if ( y == '3436' and islocal(address[i],raviz)):
        #     region[i] = 'راویز'
        # if(y=='3438'):
        #     region[i]='انار'
        # if(y == '3418' and islocal(address[i],bayaz)):
        #     region[i] = 'بیاض'
        # if(y == '3418' and islocal(address[i],hoseinabad)
        #         or
        # (y == '3439' and islocal(address[i],hoseinabad))):
        #     region[i] = 'حسین آباد انار'
        if (y == '3422' or y == '3423' or y == '3424' or y == '3425' or y == '3426' or y == '3427'
            or y == '3428' or y == '3429' or y == '3432' or y == '3433' or y == '3434' or y == '3435'):
            region[i] = 'رفسنجان'
        # if(y == '3419' and islocal(address[i], khenaman) or (y == '3421' and islocal(address[i], khenaman))):
        #     region[i]='خنامان'
        # if (y=='3421' and islocal(address[i],azadegan)) or (y=='3436'and islocal(address[i],azadegan)):
        #     region[i]='آزادگان'
        # if(y == '3419' and islocal(address[i], kabootarkhan)):
        #     region[i] = 'کبوترخان'
        # if(y == '3419' and islocal(address[i], daredoran) or (y == '3421' and islocal(address[i], daredoran)) or (
        #             y == '3437' and islocal(address[i], daredoran))):
        #     region[i] = 'دره دران'
        # if (y=='3421' and islocal(address[i],eslamie)):
        #     region[i]='اسلامیه'
        # if (y=='3437' and islocal(address[i],ghasemabad)):
        #     region[i]='قاسم آباد'
        # if (y == '3419' and islocal(address[i], razmavaran)):
        #     region[i] = 'رزم آوران'
        # if ( y == '3431'):
        #     region[i] = 'سرچشمه'

# region.count('سرچشمه')
print(region)
print(len(region))
res = Counter(region.values())
print(res)
df2=pandas.DataFrame.from_dict(region,orient='index',columns=['region'])
writer=pandas.ExcelWriter('rafsanjan_region.xlsx')
df2.to_excel(writer)
writer.save()