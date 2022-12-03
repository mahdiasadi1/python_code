import pandas
data = pandas.read_excel(r'D:\rafsangan\rafsanjan23_cover.xlsx')
df=pandas.DataFrame(data,columns=['no','title','phone','mobile','manager','address','email','website','subgroup','group','cover'])
# print (df.head)
subgroup=df['subgroup'].to_dict()
cover=df['cover'].to_dict()
for i in subgroup:
    if subgroup[i] == "آجیل و خشکبار":
        cover[i]="wp-content/uploads/2022/02/nuts.jpg"
    if subgroup[i] == "تایپ و کپی":
        cover[i] ="wp-content/uploads/2022/02/copy.jpg"
    if subgroup[i] == "تاسیسات ساختمان":
        cover[i]="wp-content/uploads/2022/02/003_tasisat.jpg"
    if subgroup[i] == "فروش و لوازم یدکی موتور سیکلت":
        cover[i]="wp-content/uploads/2022/02/004_motor.jpg"
    if subgroup[i] =="آتلیه عکاسی":
        cover[i] = "wp-content/uploads/2022/02/005_akkasi.jpg"
    if subgroup[i] =="موبایل":
        cover[i] = "wp-content/uploads/2022/02/006_mobile.webp"
    if subgroup[i] =="برق صنعتی":
        cover[i] = "wp-content/uploads/2022/02/007_barghsanaati.jpg"
    if subgroup[i] == "تابلو سازی":
        cover[i] = "wp-content/uploads/2022/02/008_tablosazi.jpg"
    if subgroup[i] == "کامپیوتر و قطعات":
        cover[i] = "wp-content/uploads/2022/02/009_computer-accsories.jpg"
    if subgroup[i] == "فراوردهای پروتیینی":
        cover[i] = "wp-content/uploads/2022/02/010_faravardegooshti.jpg"
    if subgroup[i] == "تراشکاری":
        cover[i] = "wp-content/uploads/2022/02/011_trashkari.jpg"
    if subgroup[i] == "آرایشگاه مردانه":
        cover[i] = "wp-content/uploads/2022/02/012_arayeshgah_mardaneh.jpg"
    if subgroup[i] == "آرایشگاه زنانه":
        cover[i] = "wp-content/uploads/2022/02/013_arayshgah_zananeh.jpg"
    if subgroup[i] == "محصولات آرایشی بهداشتی":
            cover[i] = "wp-content/uploads/2022/02/014_lavazem_arayesh_behdashti.jpg"
    if subgroup[i] == "آموزش صنایع دستی":
            cover[i] = "wp-content/uploads/2022/02/015_amoozesh_sanaye_dasti.jpeg"
    if subgroup[i] == "حمل و نقل کالا":
        cover[i] = "wp-content/uploads/2022/02/016_haml_kala.jpg"
    if subgroup[i] == "رانندگان":
        cover[i] = "wp-content/uploads/2022/02/017_driver-job.jpeg"
    if subgroup[i] == "چاپ و خدمات دیجیتال":
        cover[i] = "wp-content/uploads/2022/02/018_digital-printing.jpg"
    if subgroup[i] == "تاسیسات اداری - فکس - پرینتر":
        cover[i] = "wp-content/uploads/2022/02/019_fax.jpg"
    if subgroup[i] == "آجر":
        cover[i] = "wp-content/uploads/2022/02/020_brics.jpg"
    if subgroup[i] == "آهنگری و جوشکاری":
        cover[i] = "wp-content/uploads/2022/02/021_joosh.jpg"
    if subgroup[i] == "ابزار آلات ساختمانی":
        cover[i] = "wp-content/uploads/2022/02/022_abzar_sakhtemani.jpg"
    if subgroup[i] == "برق و الکتریک ساختمان":
        cover[i] = "wp-content/uploads/2022/02/023_lighting.jpg"
    if subgroup[i] == "تاسیسات ساختمان":
        cover[i] = "wp-content/uploads/2022/02/024_tasisat.jpg"
    if subgroup[i] == "تیرچه بلوک":
        cover[i] = "wp-content/uploads/2022/02/025_tirche.jpg"
    if subgroup[i] == "حجاری و تولید مصنوعات سنگی":
        cover[i] = "wp-content/uploads/2022/02/026_hajari.jpg"
    if subgroup[i] == "درب ، پنجره و حفاظ":
        cover[i] = "wp-content/uploads/2022/02/027_hefaz.jpg"
    if subgroup[i] == "درب ضد سرقت":
        cover[i] = "wp-content/uploads/2022/02/028_dar_zed_serghat.jpg"
    if subgroup[i] == "درب و پنجره UPVC":
        cover[i] = "wp-content/uploads/2022/02/029-uPVC-windows.jpg"
    if subgroup[i] == "رنگ ساختمان":
        cover[i] = "wp-content/uploads/2022/02/030-colours.jpg"
    if subgroup[i] == "سنگ های ساختمانی":
        cover[i] = "wp-content/uploads/2022/02/031_sang.png"
    if subgroup[i] == "سنگبری":
        cover[i] = "wp-content/uploads/2022/02/032_sangbori.jpg"
    if subgroup[i] == "شیشه ساختمان":
        cover[i] = "wp-content/uploads/2022/02/033_glass.jpg"
    if subgroup[i] == "عایق کاری ساختمان ، ایزوگام و آسفالت":
        cover[i] = "wp-content/uploads/2022/02/034_ayegh.jpg"
    if subgroup[i] == "فروش مواد اولیه MDF و نئوپان و کابینت":
        cover[i] = "wp-content/uploads/2022/02/035_mdf.jpg"
    if subgroup[i] == "فونداسیون و اسکلت":
        cover[i] = "wp-content/uploads/2022/02/036_fondasion.jpg"
    if subgroup[i] == "لوله و اتصالات":
        cover[i] = "wp-content/uploads/2022/02/037_looleh.jpg"
    if subgroup[i] == "لوله کشی":
        cover[i] = "wp-content/uploads/2022/02/038_looleh.jpg"
    if subgroup[i] == "ماشین آلات ساختمانی":
        cover[i] = "wp-content/uploads/2022/02/039-machine.jpg"
    if subgroup[i] == "مشاورین املاک":
        cover[i] = "wp-content/uploads/2022/02/040_amlak.jpg"
    if subgroup[i] == "مصالح ساختمانی":
        cover[i] = "wp-content/uploads/2022/02/041_masaleh.jpg"
    if subgroup[i] == "موزاییک":
        cover[i] = "wp-content/uploads/2022/02/042_mosaic.jpg"
    if subgroup[i] == "نقاشی ساختمان":
        cover[i] = "wp-content/uploads/2022/02/043_naghashi.jpg"
    if subgroup[i] == "نما سازی ساختمان":
        cover[i] = "wp-content/uploads/2022/02/044-namasazi.jpg"
    if subgroup[i] == "يراق آلات کابینت و چوب":
        cover[i] = "wp-content/uploads/2022/02/045_yaragh.jpg"
    if subgroup[i] == "کابینت":
        cover[i] = "wp-content/uploads/2022/02/046_cabinet.jpg"
    if subgroup[i] == "کاشی و سرامیک":
        cover[i] = "wp-content/uploads/2022/02/047_kashi.jpg"
    if subgroup[i] == "کانال کشی و کانال سازی":
        cover[i] = "wp-content/uploads/2022/02/048_canal.webp"
    if subgroup[i] == "گرمایشی و سرمایشی":
        cover[i] = "wp-content/uploads/2022/02/049_garm.jpg"
    if subgroup[i] == "دفتر اسناد رسمی":
        cover[i] = "wp-content/uploads/2022/02/050-asnad.jpg"
    if subgroup[i] == "تالار پذیرایی و باغ":
        cover[i] = "wp-content/uploads/2022/02/051_wedding-palace.jpg"
    if subgroup[i] == "ظروف کرایه و یکبار مصرف":
        cover[i] = "wp-content/uploads/2022/02/052_yekbarmasraf.jpg"
    if subgroup[i] == "کرایه لوازم مجالس":
        cover[i] = "wp-content/uploads/2022/02/053_keraye.jpg"
    if subgroup[i] == "گل فروشی و گل و گیاه":
        cover[i] = "wp-content/uploads/2022/02/054_gol.jpg"
    if subgroup[i] == "مسافرخانه ها":
        cover[i] = "wp-content/uploads/2022/02/055_hotel.jpg"
    if subgroup[i] == "تعمیر لوازم خانگی":
        cover[i] = "wp-content/uploads/2022/02/056_tamir.jpg"
    if subgroup[i] == "خشکشویی":
        cover[i] = "wp-content/uploads/2022/02/057_khoshkshooi.jpg"
    if subgroup[i] == "سمساری":
        cover[i] = "wp-content/uploads/2022/02/058_semsari.jpeg"
    if subgroup[i] == "قالیشویی":
        cover[i] = "wp-content/uploads/2022/02/059_ghali.jpg"
    if subgroup[i] == "کلید سازی و قفل سازی":
        cover[i] = "wp-content/uploads/2022/02/060_kelid.jpg"
    if subgroup[i] == "آپاراتی و پنچرگیری":
        cover[i] = "wp-content/uploads/2022/02/061_aparati.jpg"
    if subgroup[i] == "اتاق وسایل نقلیه":
        cover[i] = "wp-content/uploads/2022/02/062_otagh.jpg"
    if subgroup[i] == "اسپرتی اتومبیل":
        cover[i] = "wp-content/uploads/2022/02/063_sporti.jpg"
    if subgroup[i] == "اگزوز سازی":
        cover[i] = "wp-content/uploads/2022/02/064_exos.jpg"
    if subgroup[i] == "تسمه و بلبرینگ":
        cover[i] = "wp-content/uploads/2022/02/065_tasmeh.jpg"
    if subgroup[i] == "تعمیر گاه موتور سیکلت":
        cover[i] = "wp-content/uploads/2022/02/066_motor.jpg"
    if subgroup[i] == "تعمیرگاه اتومبیل":
        cover[i] = "wp-content/uploads/2022/02/067_car.jpg"
    if subgroup[i] == "تنظیم موتور":
        cover[i] = "wp-content/uploads/2022/02/068_car-mechanic.jpg"
    if subgroup[i] == "خدمات ترمز و کلاج":
        cover[i] = "wp-content/uploads/2022/02/069_tormoz.jpg"
    if subgroup[i] == "خدمات جانبی و تزیینات خودرو":
        cover[i] = "wp-content/uploads/2022/02/070_carlux.jpg"
    if subgroup[i] == "خدمات رادیاتور":
        cover[i] = "wp-content/uploads/2022/02/071_radiator.jpg"
    if subgroup[i] == "زیروبند ، جلوبندی و آهنگری اتومبیل":
        cover[i] = "wp-content/uploads/2022/02/072_jolo.jpg"
    if subgroup[i] == "سیم پیچی و باطری سازی":
        cover[i] = "wp-content/uploads/2022/02/073_car-electricity.jpg"
    if subgroup[i] == "صافکاری و نقاشی خودرو":
        cover[i] = "wp-content/uploads/2022/02/074_Car-Painting.jpg"
    if subgroup[i] == "فروش و تعویض روغن":
        cover[i] = "wp-content/uploads/2022/02/075_roghan.jpg"
    if subgroup[i] == "فروش و لوازم یدکی موتور سیکلت":
        cover[i] = "wp-content/uploads/2022/02/076_motor.jpg"
    if subgroup[i] == "فروشندگان لاستیک":
        cover[i] = "wp-content/uploads/2022/02/077_lastic.jpg"
    if subgroup[i] == "فروشگاه دوچرخه":
        cover[i] = "wp-content/uploads/2022/02/078_bike.webp"
    if subgroup[i] == "لوازم یدکی خودرو":
        cover[i] = "wp-content/uploads/2022/02/079_lavazem-yadak-khodro.jpg"
    if subgroup[i] == "نمایشگاه ماشین":
        cover[i] = "wp-content/uploads/2022/02/080_car.jpg"
    if subgroup[i] == "کارواش":
        cover[i] = "wp-content/uploads/2022/02/081_carwash.jpg"
    if subgroup[i] == "اسباب بازی":
        cover[i] = "wp-content/uploads/2022/02/082_toy.jpg"
    if subgroup[i] == "خرازی فروشان":
        cover[i] = "wp-content/uploads/2022/02/083_kharazi.jpg"
    if subgroup[i] == "سیسمونی":
        cover[i] = "wp-content/uploads/2022/02/084_sismooni.jpg"
    if subgroup[i] == "خیاطی":
        cover[i] = "wp-content/uploads/2022/02/085_khayati.jpg"
    if subgroup[i] == "خیاطی مردانه":
        cover[i] = "wp-content/uploads/2022/02/086_man_tailor.jpg"
    if subgroup[i] == "خیاطی زنانه":
        cover[i] = "wp-content/uploads/2022/02/087_woman-tailor.jpg"
    if subgroup[i] == "آکواریوم":
        cover[i] = "wp-content/uploads/2022/02/088_aquarium.jpg"
    if subgroup[i] == "خوراک دام":
        cover[i] = "wp-content/uploads/2022/02/089_dam.jpg"
    if subgroup[i] == "دامپزشکی":
        cover[i] = "wp-content/uploads/2022/02/090_Veterinary.jpg"
    if subgroup[i] == "لوازم کشاورزی و سموم":
        cover[i] = "wp-content/uploads/2022/02/091_somum.jpg"
    if subgroup[i] == "فروشندگان دخانیات":
        cover[i] = "wp-content/uploads/2022/02/092_tobacco.jpg"
    if subgroup[i] == "تزیینات داخلی":
        cover[i] = "wp-content/uploads/2022/02/093_decoration.jpg"
    if subgroup[i] == "فرش و تابلو فرش":
        cover[i] = "wp-content/uploads/2022/02/094_carpet.jpg"
    if subgroup[i] == "مبلمان خانگی":
        cover[i] = "wp-content/uploads/2022/02/095_moble.jpeg"
    if subgroup[i] == "موکت":
        cover[i] = "wp-content/uploads/2022/02/096_mooket.jpg"
    if subgroup[i] == "پرده فروشی":
        cover[i] = "wp-content/uploads/2022/02/097_pardeh.jpg"
    if subgroup[i] == "چوب و مصنوعات":
        cover[i] = "wp-content/uploads/2022/02/098_wood.jpg"
    if subgroup[i] == "کالای خواب":
        cover[i] = "wp-content/uploads/2022/02/099_khab.jpg"
    if subgroup[i] == "کف پوش و کاغذ دیواری":
        cover[i] = "wp-content/uploads/2022/02/100_kafpoosh.jpg"
    if subgroup[i] == "آزمایشگاه طلا":
        cover[i] = "wp-content/uploads/2022/02/101_Gold.jpg"
    if subgroup[i] == "طلا سازی":
        cover[i] = "wp-content/uploads/2022/02/102_Making_gold.jpg"
    if subgroup[i] == "فروش طلا و جواهر و نقره":
        cover[i] = "wp-content/uploads/2022/02/103_tala.jpg"
    if subgroup[i] == "ساعت":
        cover[i] = "wp-content/uploads/2022/02/104_watch.jpg"
    if subgroup[i] == "عینک":
        cover[i] = "wp-content/uploads/2022/02/105_glass.jpg"
    if subgroup[i] == "آهن آلات و ضایعات":
        cover[i] = "wp-content/uploads/2022/02/106_ahanalat.jpg"
    if subgroup[i] == "ابزار و یراق":
        cover[i] = "wp-content/uploads/2022/02/107_construction-tools.webp"
    if subgroup[i] == "بسته بندی کالا":
        cover[i] = "wp-content/uploads/2022/02/108_bastebandi.png"
    if subgroup[i] == "تجهیزات آزمایشگاهی":
        cover[i] = "wp-content/uploads/2022/02/109_laborator.jpg"
    if subgroup[i] == "تولید و تعمیر انواع پمپ":
        cover[i] = "wp-content/uploads/2022/02/110_pump.jpg"
    if subgroup[i] == "جرثقیل و لیفتراک":
        cover[i] = "wp-content/uploads/2022/02/111_jaresaghil.jpg"
    if subgroup[i] == "خدمات برش ، پرسکاری ، CNC":
        cover[i] = "wp-content/uploads/2022/02/112_laser-cutting.jpg"
    if subgroup[i] == "سیم پیچی و الكتروموتور":
        cover[i] = "wp-content/uploads/2022/02/113_winding.jpg"
    if subgroup[i] == "صنایع فلزی":
        cover[i] = "wp-content/uploads/2022/02/114_felez.jpg"
    if subgroup[i] == "صنایع مخابرات":
        cover[i] = "wp-content/uploads/2022/02/115_mokhaberat.jpg"
    if subgroup[i] == "صنعت چوب":
        cover[i] = "wp-content/uploads/2022/02/116_wood.jpg"
    if subgroup[i] == "فایبرگلاس":
        cover[i] = "wp-content/uploads/2022/02/117_Fiberglass.jpg"
    if subgroup[i] == "فروش و تعمیر ماشین آلات کشاورزی":
        cover[i] = "wp-content/uploads/2022/02/118_keshavarzi.jpg"
    if subgroup[i] == "قالب سازی":
        cover[i] = "wp-content/uploads/2022/02/119_ghaleb.jpg"
    if subgroup[i] == "لوازم یدکی ماشین آلات":
        cover[i] = "wp-content/uploads/2022/02/120_alat.jpg"
    if subgroup[i] == "ماشین آلات صنعتی":
        cover[i] = "wp-content/uploads/2022/02/121.jpg"
    if subgroup[i] == "مخزن و تانکرسازی":
        cover[i] = "wp-content/uploads/2022/02/122_makhzan.jpg"
    if subgroup[i] == "کارتن سازی":
        cover[i] = "wp-content/uploads/2022/02/123_karton.jpg"
    if subgroup[i] == "بیمارستان":
        cover[i] = "wp-content/uploads/2022/02/124_hospital.jpeg"
    if subgroup[i] == "جراحان استخوان و مفاصل":
        cover[i] = "wp-content/uploads/2022/02/125_orthoped.jpg"
    if subgroup[i] == "جراحان مغز واعصاب":
        cover[i] = "wp-content/uploads/2022/02/126_brain.jpeg"
    if subgroup[i] == "جراحان عمومی":
        cover[i] = "wp-content/uploads/2022/02/127_jarrahi.jpg"
    if subgroup[i] == "داروخانه":
        cover[i] = "wp-content/uploads/2022/02/128_pharmacy.jpg"
    if subgroup[i] == "سایر خدمات پزشکی":
        cover[i] = "wp-content/uploads/2022/02/129.jpg"
    if subgroup[i] == "عطاری و داروهای گیاهی":
        cover[i] = "wp-content/uploads/2022/02/130_attari.jpg"
    if subgroup[i] == "پزشكان عمومی":
        cover[i] = "wp-content/uploads/2022/02/131_omumi.jpeg"
    if subgroup[i] == "پزشکان متخصص آسیب شناسی بالینی":
        cover[i] = "wp-content/uploads/2022/02/132_pathology.jpg"
    if subgroup[i] == "پزشکان متخصص آسیب شناسی و تشریحی":
        cover[i] = "wp-content/uploads/2022/02/132_pathology.jpg"
    if subgroup[i] == "پزشکان متخصص ارتودانتيکس":
        cover[i] = "wp-content/uploads/2022/02/134_Ortho.jpg"
    if subgroup[i] == "پزشکان متخصص ارتوپد":
        cover[i] = "wp-content/uploads/2022/02/135_orthoped.jpeg"
    if subgroup[i] == "پزشکان متخصص اطفال":
        cover[i] = "wp-content/uploads/2022/02/136_infant.jpg"
    if subgroup[i] == "پزشکان متخصص انگل شناسی":
        cover[i] = "wp-content/uploads/2022/02/137_angal.jpg"
    if subgroup[i] == "پزشکان متخصص ایمونولژی":
        cover[i] = "wp-content/uploads/2022/02/138_Immunology.jpg"
    if subgroup[i] == "پزشکان متخصص بیهوشی":
        cover[i] = "wp-content/uploads/2022/02/139_bihushi.jpg"
    if subgroup[i] == "پزشکان متخصص بیوشیمی":
        cover[i] = "wp-content/uploads/2022/02/140_biochemi.png"
    if subgroup[i] == "پزشکان متخصص تغذیه":
        cover[i] = "wp-content/uploads/2022/02/141_taghzie.jpg"
    if subgroup[i] == "پزشکان متخصص داخلی":
        cover[i] = "wp-content/uploads/2022/02/dakheli.webp"
    if subgroup[i] == "پزشکان متخصص داروسازی":
        cover[i] = "wp-content/uploads/2022/02/142_daroosaz.jpg"
    if subgroup[i] == "پزشکان متخصص درمان ریشه":
        cover[i] = "wp-content/uploads/2022/02/143_root.jpg"
    if subgroup[i] == "پزشکان متخصص دندان - دندانپزشكان":
        cover[i] = "wp-content/uploads/2022/02/144_tooth.jpeg"
    if subgroup[i] == "پزشکان متخصص رادیوتراپی":
        cover[i] = "wp-content/uploads/2022/02/145_radio.jpg"
    if subgroup[i] == "پزشکان متخصص روان پزشکی":
        cover[i] = "wp-content/uploads/2022/02/146_ravan.jpg"
    if subgroup[i] == "پزشکان متخصص زنان و زایمان":
        cover[i] = "wp-content/uploads/2022/02/147_zanan.jpg"
    if subgroup[i] == "پزشکان متخصص طب اورژانس":
        cover[i] = "wp-content/uploads/2022/02/148_emergency.jpg"
    if subgroup[i] == "پزشکان متخصص عفونی و گرمسیری":
        cover[i] = "wp-content/uploads/2022/02/149_garmsiri.jpg"
    if subgroup[i] == "پزشکان متخصص علوم آزمایشگاهی":
        cover[i] = "wp-content/uploads/2022/02/150_lab.jpg"
    if subgroup[i] == "پزشکان متخصص فیزیوتراپی و توانبخشی":
        cover[i] = "wp-content/uploads/2022/02/151_Physiotherapy.jpg"
    if subgroup[i] == "پزشکان متخصص پزشكی فیزیكی وتوانبخشی":
        cover[i] = "wp-content/uploads/2022/02/151_Physiotherapy.jpg"
    if subgroup[i] == "پزشکان متخصص قلب و عروق":
        cover[i] = "wp-content/uploads/2022/02/152_heart.jpg"
    if subgroup[i] == "پزشکان متخصص مغز و اعصاب":
        cover[i] = "wp-content/uploads/2022/02/153_brain.jpg"
    if subgroup[i] == "پزشکان متخصص فیزیوتراپی و توانبخشی":
        cover[i] = "wp-content/uploads/2022/02/154_phisio.jpg"
    if subgroup[i] == "پزشکان متخصص پزشکی قانونی":
        cover[i] = "wp-content/uploads/2022/02/155_forensic.jpeg"
    if subgroup[i] == "پزشکان متخصص پوست":
        cover[i] = "wp-content/uploads/2022/02/156_skin.jpg"
    if subgroup[i] == "پزشکان متخصص چشم - چشم پزشكان":
        cover[i] = "wp-content/uploads/2022/02/157_eye.jpg"
    if subgroup[i] == "پزشکان متخصص کاردرمانی":
        cover[i] = "wp-content/uploads/2022/02/158_occupational-therapy.jpg"
    if subgroup[i] == "پزشکان متخصص گفتار درمانی":
        cover[i] = "wp-content/uploads/2022/02/159_goftar.jpg"
    if subgroup[i] == "پزشکان متخصص گوش و حلق وبینی":
        cover[i] = "wp-content/uploads/2022/02/160_ent.jpg"
    if subgroup[i] == "کلینیک ها":
        cover[i] = "wp-content/uploads/2022/02/161_clinicPhoto.png"
    if subgroup[i] == "مراکز پزشکی":
        cover[i] = "wp-content/uploads/2022/02/207_hospital.jpg"
    if subgroup[i] == "تهیه غذا و کیترینگ":
        cover[i] = "wp-content/uploads/2022/02/162_Catering.jpg"
    if subgroup[i] == "رستوران":
        cover[i] = "wp-content/uploads/2022/02/163_restaurant.jpg"
    if subgroup[i] == "فست فود":
        cover[i] = "wp-content/uploads/2022/02/164_fastfood.jpg"
    if subgroup[i] == "کبابی و جگرکی":
        cover[i] = "wp-content/uploads/2022/02/165_kebabi.jpg"
    if subgroup[i] == "فروشگاه لوازم خانگی":
        cover[i] = "wp-content/uploads/2022/02/166_homeappliance.jpg"
    if subgroup[i] == "فروشگاه لوازم صوتی و تصویری":
        cover[i] = "wp-content/uploads/2022/02/167_audio.png"
    if subgroup[i] == "لوازم آشپزخانه":
        cover[i] = "wp-content/uploads/2022/02/168_kitchen.jpg"
    if subgroup[i] == "پلاسکو":
        cover[i] = "wp-content/uploads/2022/02/169_plasco.jpg"
    if subgroup[i] == "آب میوه فروشی و بستنی":
        cover[i] = "wp-content/uploads/2022/02/170_icecream.jpg"
    if subgroup[i] == "آجیل و خشکبار":
        cover[i] = "wp-content/uploads/2022/02/171_agil.jpg"
    if subgroup[i] == "بنکداران":
        cover[i] = "wp-content/uploads/2022/02/172_bonak.jpg"
    if subgroup[i] == "سوپر مواد غذایی و خواربار":
        cover[i] = "wp-content/uploads/2022/02/173_super.jpg"
    if subgroup[i] == "فراورده های لبنی":
        cover[i] = "wp-content/uploads/2022/02/174_labani.jpg"
    if subgroup[i] == "فراوردهای پروتیینی":
        cover[i] = "wp-content/uploads/2022/02/175_sosis.jpg"
    if subgroup[i] == "قنادی و شیرینی سرا":
        cover[i] = "wp-content/uploads/2022/02/176_candy.jpg"
    if subgroup[i] == "لوازم قنادی":
        cover[i] = "wp-content/uploads/2022/02/177_candy_asset.jpg"
    if subgroup[i] == "مرغ و ماهی":
        cover[i] = "wp-content/uploads/2022/02/178_morgh.jpg"
    if subgroup[i] == "میوه و تره بار":
        cover[i] = "wp-content/uploads/2022/02/179_fruit.jpg"
    if subgroup[i] == "نانوایی و سایر فراوردهای آردی":
        cover[i] = "wp-content/uploads/2022/02/180_Breads.jpg"
    if subgroup[i] == "گوشت فروشی":
        cover[i] = "wp-content/uploads/2022/02/181_goosht.jpg"
    if subgroup[i] == "تایپ و کپی":
        cover[i] = "wp-content/uploads/2022/02/182_type.jpg"
    if subgroup[i] == "صحافی":
        cover[i] = "wp-content/uploads/2022/02/183_bookbinding.jpg"
    if subgroup[i] == "لوازم تحریر":
        cover[i] = "wp-content/uploads/2022/02/184_tahrir.jpg"
    if subgroup[i] == "مهر و پلاک":
        cover[i] = "wp-content/uploads/2022/02/185_Mohr.jpg"
    if subgroup[i] == "کتاب و مجله":
        cover[i] = "wp-content/uploads/2022/02/186_bookstores.jpg"
    if subgroup[i] == "تابلو نویسی":
        cover[i] = "wp-content/uploads/2022/02/008_tablosazi.jpg"
    if subgroup[i] == "صنایع دستی":
        cover[i] = "wp-content/uploads/2022/02/187_handicraft.jpg"
    if subgroup[i] == "لوازم ورزشی":
        cover[i] = "wp-content/uploads/2022/02/188_sport.jpg"
    if subgroup[i] == "جوراب":
        cover[i] = "wp-content/uploads/2022/02/189_socks.jpg"
    if subgroup[i] == "شال و روسری":
        cover[i] = "wp-content/uploads/2022/02/190_roosari.jpg"
    if subgroup[i] == "فروش و کرایه لباس عروس":
        cover[i] = "wp-content/uploads/2022/02/191_broom.jpg"
    if subgroup[i] == "مانتو فروشی":
        cover[i] = "wp-content/uploads/2022/02/192_mantue.jpg"
    if subgroup[i] == "محصولات چرمی":
        cover[i] = "wp-content/uploads/2022/02/193_charm.jpg"
    if subgroup[i] == "پارچه سرا":
        cover[i] = "wp-content/uploads/2022/02/194_parche.jpg"
    if subgroup[i] == "پوشاک بچه گانه":
        cover[i] = "wp-content/uploads/2022/02/195_kids.jpg"
    if subgroup[i] == "پوشاک مردانه":
        cover[i] = "wp-content/uploads/2022/02/196_men.jpg"
    if subgroup[i] == "پوشاک زنانه":
        cover[i] = "wp-content/uploads/2022/02/197_women.jpeg"
    if subgroup[i] == "کیف و کفش و چمدان":
        cover[i] = "wp-content/uploads/2022/02/198_suitcase.jpg"
    if subgroup[i] == "تلفن":
        cover[i] = "wp-content/uploads/2022/02/199_phones.jpeg"
    if subgroup[i] == "خدمات اینترنت":
        cover[i] = "wp-content/uploads/2022/02/200_isp.jpg"
    if subgroup[i] == "فروشندگان نرم افزار و CD":
        cover[i] = "wp-content/uploads/2022/02/201_cd.jpeg"
    if subgroup[i] == "لوارم جانبی کامپیوتر":
        cover[i] = "wp-content/uploads/2022/02/202_computer.jpg"
    if subgroup[i] == "ویدیو کلوپ":
        cover[i] = "wp-content/uploads/2022/02/201_cd.jpeg"
    if subgroup[i] == "کافی نت و گیم نت":
        cover[i] = "wp-content/uploads/2022/02/203_gamenet.jpg"
    if subgroup[i] == "کامپیوتر و قطعات":
        cover[i] = "wp-content/uploads/2022/02/205_computer-parts.jpg"
    if subgroup[i] == "پزشکان متخصص كلیه ومجاری ادرار":
        cover[i] = "wp-content/uploads/2022/02/206_kidney.jpg.jpg"
    if subgroup[i] == "باسکول":
        cover[i] = "wp-content/uploads/2022/02/208_bascool.jpg"
    if subgroup[i] == "تاکسی تلفنی":
        cover[i] = "wp-content/uploads/2022/02/209_taxi.jpg"
    if subgroup[i] == "استودیو فیلمسازی":
        cover[i] = "wp-content/uploads/2022/02/210_studio.jpeg"
    if subgroup[i] == "وانت تلفنی":
        cover[i] = "wp-content/uploads/2022/02/211_vanetbar.jpg"


print(cover)
df1=pandas.DataFrame.from_dict(cover,orient='index',columns=['cover'])
writer=pandas.ExcelWriter('cover.xlsx')
df1.to_excel(writer)
writer.save()
