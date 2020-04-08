import sys
from PyQt5.QtWidgets import (QTextEdit, QPushButton, QApplication, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt

def strreplace(azstr):
	azstr = azstr.replace("aa", "اعا")
	azstr = azstr.replace("iyi", "یگی")
	azstr = azstr.replace("iy", "ی")
	azstr = azstr.replace("a", "ا")
	azstr = azstr.replace("b", "ب")
	azstr = azstr.replace("c", "ج")
	azstr = azstr.replace("d", "د")
	azstr = azstr.replace("e", "ئ")
	azstr = azstr.replace("f", "ف")
	azstr = azstr.replace("g", "گ")
	azstr = azstr.replace("h", "ه")
	azstr = azstr.replace("j", "ژ")
	azstr = azstr.replace("k", "ک")
	azstr = azstr.replace("i", "ی")
	azstr = azstr.replace("l", "ل")
	azstr = azstr.replace("m", "م")
	azstr = azstr.replace("n", "ن")
	azstr = azstr.replace("o", "و")
	azstr = azstr.replace("p", "پ")
	azstr = azstr.replace("q", "ق")
	azstr = azstr.replace("r", "ر")
	azstr = azstr.replace("s", "س")
	azstr = azstr.replace("t", "ت")
	azstr = azstr.replace("x", "خ")
	azstr = azstr.replace("y", "ی")
	azstr = azstr.replace("v", "و")
	azstr = azstr.replace("u", "و")
	azstr = azstr.replace("z", "ز")
	azstr = azstr.replace("ə", "")
	azstr = azstr.replace("ü", "و")
	azstr = azstr.replace("ö", "ؤ")
	azstr = azstr.replace("ğ", "غ")
	azstr = azstr.replace("ç", "چ")
	azstr = azstr.replace("ş", "ش")
	azstr = azstr.replace("ı", "ی")
	return azstr

def firstconvert(azstr):
    azstr = azstr.replace('ј', 'y')
    azstr = azstr.replace('Ә', 'ə')
    azstr = azstr.replace('ә', 'ə')
    azstr = azstr.replace('Ə', 'ə')
    azstr = azstr.replace('Ö', 'ö')
    azstr = azstr.replace('Ğ', 'ğ')
    azstr = azstr.replace('I', 'ı')
    azstr = azstr.replace('Ç', 'ç')
    azstr = azstr.replace('Ş', 'ş')
    azstr = azstr.replace('Ü', 'ü')
    azstr = azstr.replace('İ', 'i')
    azstr = azstr.replace('?', ' ?')
    azstr = azstr.replace('?', '؟')
    azstr = azstr.replace('!', ' !')
    azstr = azstr.replace('/*', '')
    azstr = azstr.replace('*/', '')
    azstr = azstr.replace(',', ' ,')
    azstr = azstr.replace('(', '( ')
    azstr = azstr.replace(')', ' )')
    azstr = azstr.replace('.', ' . ')
    azstr = azstr.replace(':', ' :')
    azstr = azstr.replace('\'', '`')
    azstr = azstr.replace(' :]', ':]')
    azstr = azstr.replace(';', ' ;')
    azstr = azstr.replace('-', ' - ')
    azstr = azstr.replace('«', '« ')
    azstr = azstr.replace('»', ' »')
    azstr = azstr.replace('<br>', ' &&& ')
    azstr = azstr.replace('<br />', ' &&& ')
    azstr = azstr.replace('\n', ' %% ')
    return azstr

def firstwordconvert(azstr, wordslist):
	for i in range(len(wordslist)):
		substr = azstr[0:len(wordslist[i][0])]
		prestr = azstr[len(wordslist[i][0]):]
		if substr == wordslist[i][0]:
			substr = substr.replace(wordslist[i][0],wordslist[i][1])
		azstr = substr + prestr
	return azstr

def middleconvert(azstr):
	azstr = azstr.replace('ai', 'ائی')
	return azstr

def lastconvert(azstr):
    azstr  = azstr.replace(' %% ', '\n')
    azstr  = azstr.replace('%% ', '\n')
    azstr  = azstr.replace('%%', '\n')
    azstr  = azstr.replace('ؤو', 'ؤ')
    azstr  = azstr.replace('ووو', 'وو')
    azstr  = azstr.replace(' ,', ',')
    azstr  = azstr.replace(' .', '.')
    azstr  = azstr.replace('( ', '(')
    azstr  = azstr.replace(' )', ')')
    azstr  = azstr.replace(' ؟', '؟')
    azstr  = azstr.replace(' !', '!')
    azstr  = azstr.replace(' :', ':')
    azstr  = azstr.replace(' ;', ';')
    azstr  = azstr.replace(' - ', '-')
    azstr  = azstr.replace('« ', '«')
    azstr  = azstr.replace(' »', '»')
    azstr  = azstr.replace('ı', 'I')
    azstr  = azstr.replace('x', 'X')
    azstr  = azstr.replace('v', 'V')
    azstr  = azstr.replace('&&&', '<br>')
    return azstr

def firstcharacter(azstr):
	prefex = [['ələrindəki', 'ه‌لرینده‌کی'],['ələrdəki', 'ه‌لرده‌کی'],['əsindən', 'ه‌سیندن'],['əsinin', 'ه‌سینین'],['əsirdi', 'ه‌سیردی'],['ədiyini', 'ه‌دی‌یینی'],['əyəcək', 'ه‌یه‌جک'],['əsində', 'ه‌سینده'],['əsədə', 'ه‌سه‌ده'],['ələri', 'ه‌لری'],['əlmiş', 'ه‌لمیش'],['ənin', 'ه‌نین'],['əni', 'ه‌نی'],['ənən', 'ه‌نن'],['ənir', 'ه‌نیر'],['əyin', 'ه‌یین'],['əyinə', 'ه‌یینه'],['ədir', 'ه‌دیر'],['ədək', 'ه‌دک'],['ədə', 'ه‌ده'],['əmək', 'ه‌مک'],['əməyə', 'ه‌مگه'],['əmişdi', 'ه‌میشدی'],['əcək', 'ه‌جک'],['ədən', 'ه‌دن'],['əyib', 'ه‌ییب'],['əyən', 'ه‌ین'],['ələr', 'ه‌لر'],['əli', 'ه‌لی'],['əyə', 'ه‌یه'],['ə', 'ه'],['mədi', 'مه‌دی'],['iyin', 'ی‌یین'],['dəki', 'ده‌کی'],['ıya', 'ی‌یا'],['ıyırdı', 'ی‌ییردی'],['ləşir', 'له‌شیر'],['rov', 'روف'],['mədi', 'مه‌دی']]
	for i in range(len(prefex)):
		lastchar = azstr[-len(prefex[i][0]):]
		azstr2 = azstr[0:-len(prefex[i][0])]
		if lastchar == prefex[i][0]:
			lastchar = lastchar.replace(prefex[i][0],prefex[i][1])
		azstr = azstr2 + lastchar
	return azstr

def convertableword(azstr):
	if ':]' in azstr or 'w' in azstr or 'http' in azstr or '[' in azstr or ']' in azstr:
		return 0
	elif azstr == 'ı' or azstr == 'ıı' or azstr == 'ııı' or azstr == 'ıv' or azstr == 'v' or azstr == 'vı' or azstr == 'vıı' or azstr == 'ııı' or azstr == 'vııı' or azstr == 'ıx' or azstr == 'x' or azstr == 'xı' or azstr == 'xıı' or azstr == 'xııı' or azstr == 'xıv' or azstr == 'xv' or azstr == 'xvı' or azstr == 'xvıı' or azstr == 'xııı' or azstr == 'xıx' or azstr == 'xx':
		return 0
	else:
		return 1
	
def vajaqconvert(azstr):
    azstr = azstr.replace('À', 'A')
    azstr = azstr.replace('Á', 'B')
    azstr = azstr.replace('Ú', 'C')
    azstr = azstr.replace('Ä', 'D')
    azstr = azstr.replace('Å', 'E')
    azstr = azstr.replace('Ô', 'F')
    azstr = azstr.replace('Ý', 'G')
    azstr = azstr.replace('Ù', 'H')
    azstr = azstr.replace('È', 'İ')
    azstr = azstr.replace('Û', 'I')
    azstr = azstr.replace('Æ', 'J')
    azstr = azstr.replace('Ê', 'K')
    azstr = azstr.replace('Ë', 'L')
    azstr = azstr.replace('Ì', 'M')
    azstr = azstr.replace('Í', 'N')
    azstr = azstr.replace('Î', 'O')
    azstr = azstr.replace('Ï', 'P')
    azstr = azstr.replace('Ã', 'Q')
    azstr = azstr.replace('Ð', 'R')
    azstr = azstr.replace('Ñ', 'S')
    azstr = azstr.replace('Ò', 'T')
    azstr = azstr.replace('Â', 'V')
    azstr = azstr.replace('Ó', 'U')
    azstr = azstr.replace('Õ', 'X')
    azstr = azstr.replace('É', 'Y')
    azstr = azstr.replace('Ü', 'Ğ')
    azstr = azstr.replace('ß', 'Ə')
    azstr = azstr.replace('Ø', 'Ş')
    azstr = azstr.replace('Õ', 'X')
    azstr = azstr.replace('Ö', 'Ü')
    azstr = azstr.replace('Þ', 'Ö')
    azstr = azstr.replace('Ç', 'Z')
    azstr = azstr.replace('×', 'Ç')
    azstr = azstr.replace('à', 'a')
    azstr = azstr.replace('á', 'b')
    azstr = azstr.replace('ú', 'c')
    azstr = azstr.replace('ä', 'd')
    azstr = azstr.replace('å', 'e')
    azstr = azstr.replace('ô', 'f')
    azstr = azstr.replace('ý', 'g')
    azstr = azstr.replace('ù', 'h')
    azstr = azstr.replace('è', 'i')
    azstr = azstr.replace('æ', 'j')
    azstr = azstr.replace('ê', 'k')
    azstr = azstr.replace('ë', 'l')
    azstr = azstr.replace('ì', 'm')
    azstr = azstr.replace('í', 'n')
    azstr = azstr.replace('î', 'o')
    azstr = azstr.replace('ï', 'p')
    azstr = azstr.replace('ã', 'q')
    azstr = azstr.replace('ð', 'r')
    azstr = azstr.replace('ñ', 's')
    azstr = azstr.replace('ò', 't')
    azstr = azstr.replace('â', 'v')
    azstr = azstr.replace('ó', 'u')
    azstr = azstr.replace('õ', 'x')
    azstr = azstr.replace('é', 'y')
    azstr = azstr.replace('ÿ', 'ə')
    azstr = azstr.replace('ü', 'ğ')
    azstr = azstr.replace('ç', 'z')
    azstr = azstr.replace('ö', 'ü')
    azstr = azstr.replace('ø', 'ş')
    azstr = azstr.replace('÷', 'ç')
    azstr = azstr.replace('û', 'ı')
    azstr = azstr.replace('þ', 'ö')
    return azstr;

def isarabicword(azstr):
	if 'آ' in azstr or 'ا' in azstr or 'ی' in azstr or 'و' in azstr or 'ب' in azstr or 'ه' in azstr or 'ئ' in azstr or 'ک' in azstr or '۱' in azstr:
		return 1
	else:
		return 0

def ispronun(azstr):
	if ']' in azstr:
		return 1
	else:
		return

def clear_text():
	edit1.setText('')
	edit2.setText('')

def convert(azstr):
	azstr = edit1.toPlainText()
	wordslist = [["zülm","ظلم"],["zühur","ظهور"],["zuhur","ظهور"],["ziyan","زیان"],["ziya","ضیا"],["zillət","ذلت"],["zikr","ذکر"],["ziddiyyət","ضدیت"],["ziddiyət","ضدیت"],["zidd","ضد"],["zid","ضید"],["zərurət","ضرورت"],["zəifləmək","ضعیف‌له‌مک"],["zəif","ضعیف"],["zəhmət","زحمت"],["zəfər","ظفر"],["zatən","ذاتاً"],["zat","ذات"],["zalim","ظالم"],["zalım","ظالم"],["zahir","ظاهر"],["zabit","ظابط"],["yiyə","یییه‌"],["yəni","یعنی"],["yəni","یعنی"],["xüsusiyyət","خصوصیت"],["xüsusi","خصوصی"],["xüsusən","خصوصاً"],["xürrəm","خرم"],["xülasə","خلاصه‌"],["xususiyyət","خصوصیت"],["xususi","خصوصی"],["xulasə","خلاصه‌"],["xilas","خلاص"],["xəzinəsidir","خزینه‌سیدیر"],["xəzinə","خزینه‌"],["xəstə","خسته‌"],["xeyli","خیلی"],["xatirə","خاطره‌"],["xatir","خاطر"],["xatır","خاطر"],["xas","خاص"],["xarakter","کاراکتئر"],["xalis","خالص"],["xalıs","خالص"],["vüsət","ووسعت"],["vicdan","ویجدان"],["vəziyyət","وضعیت"],["vəzifə","وظیفه‌"],["vətənə","وطنه‌"],["vətən","وطن"],["vəhşi","وحشی"],["vəhid","وحید"],["vəhdət","وحدت"],["vədə","وعده‌"],["və","و"],["vasitə","واسطه‌"],["varis","واریث"],["vahid","واحد"],["vağvuğ","واغ‌ووغ"],["üzv","عضو"],["üzrə","اوزره"],["üzr","عذر"],["üzr","عذر"],["üsyan","عصیان"],["üsul","اصول"],["ümumiyyət","عمومیت"],["ümumi","عمومی"],["ümumi","عمومی"],["ümumən","عموماً"],["ü","او"],["usul","اصول"],["unix","یونیکس"],["u","او"],["türkiyə","تورکیه‌"],["tövsiyə","توصیه‌"],["tövbə","توبه‌"],["tifil","طیفیل"],["təzyiq","تضییق"],["təzahür","تظاهر"],["təyin","تعیین"],["təxminən","تخمیناً"],["təxəllüs","تخلص"],["təxəllüf","تخلف"],["tətbiq","تطبیق"],["təsvir","تصویر"],["təsir","تأثیر"],["təsərrüfat","تصروفات"],["təsdiq","تصدیق"],["təsbit","تثبیت"],["təsadüf","تصادف"],["tərz","طرز"],["tərif","تعریف"],["tərəf","طرف"],["təravət","طراوت"],["təqribən","تقریباً"],["təqib","تعقیب"],["təpəsi","تپه‌سی"],["təpəli","تپه‌لی"],["təmsil","تمثیل"],["təminat","تأمینات"],["təminat","تأمینات"],["təmin","تعمین"],["tələffüz","تلفوظ"],["tələbə","طلبه‌"],["tələb","طلب"],["təkid","تاکید"],["təhsildar","تحصیلدار"],["təhsil","تحصیل"],["təhrif","تحریف"],["təhqir","تحقیر"],["təhqiqat","تحقیقات"],["təhqiq","تحقیق"],["təhmil","تحمیل"],["təhlil","تحلیل"],["təharət","طهارت"],["təəssüf","تأسف"],["təəcüb","تعجب"],["təəccüb","تعجب"],["tədris","تدریس"],["təcəssüm","تجسم"],["təbir","تعبیر"],["təbiidir","طبیعی‌دیر"],["təbii","طبیعی"],["təbiətin","طبیعتین"],["təbiət","طبیعت"],["təbəqə","طبقه‌"],["təala","تعالی"],["təyin","تعیین"],["təsir","تأثیر"],["tərif","تعریف"],["təmin","تعمین"],["təbir","تعبیر"],["texnik","تئکنیک"],["tayfa","تایفا"],["tarixən","تاریخاً"],["talib","طالب"],["tabe","تابع"],["şüur","شعور"],["şücaət","شجاعت"],["şücaət","شجاعت"],["şüar","شوعار"],["şöbə","شعبه‌"],["şiə","شیعه‌"],["şiddət","شدت"],["şiə","شیعه‌"],["şəxsiyyət","شخصیت"],["şəxsən","شخصاً"],["şəxs","شخص"],["şərt","شرط"],["şəriət","شریعت"],["şəri","شرعی"],["şərh","شرح"],["şərayit","شرایط"],["şərayet","شرایط"],["şərait","شرایط"],["şəkk","شک"],["şeytan","شیطان"],["şer","شعر"],["şer","شعر"],["şair","شاعر"],["sürət","سرعت"],["sürət","سرعت"],["süqut","سوقوط"],["süni","صونعی"],["sültan","سلطان"],["sübüt","ثوبوت"],["sübut","ثبوت"],["surət","صورت"],["sultan","سلطان"],["sufi","صوفی"],["söylənir","سؤیله‌نیر"],["söylə","سؤیله‌"],["söhbət","صحبت"],["sirf","صرف"],["sinif","صینیف"],["sinələrini","سینه‌لرینی"],["silah","سلاح"],["sifir","صیفیر"],["sifət","صفت"],["sırf","صرف"],["sınıf","صینیف"],["sıfir","صیفیر"],["sıfır","صیفیر"],["sətir","سطر"],["səth","سطح"],["sərvətləri","ثروتلری"],["sərvət","ثروت"],["sərhəd","سرحد"],["sərf","صرف"],["sənət","صنعت"],["sənət","صنعت"],["sənduq","صندوق"],["sənaye","صنایع"],["səmimi","صمیمی"],["səməd","صمد"],["səltənət","سلطنت"],["səhnə","صحنه‌"],["səhifələrini","صحیفه‌لرینی"],["səhifə","صحیفه‌"],["səhərin","سحرین"],["səhər","سحر"],["səfəvi","صفوی"],["səf","صف"],["sədr","صدر"],["sədr","صدر"],["səbr","صبر"],["səbir","صبیر"],["seyid","سید"],["sehr","سئحر"],["samit","صامیت"],["salih","صالح"],["saleh","صالح"],["salam","سلام"],["salam","سلام"],["sahilinə","ساحیلینه"],["sahil","ساحیل"],["sahib","صاحب"],["sahə","ساحه‌"],["saf","صاف"],["sadir","صادر"],["sadiq","صادق"],["sabit","ثابت"],["sabir","صابیر"],["sabah","صاباح"],["saat","ساعت"],["rza","رضا"],["ruhaniyyət","روحانیت"],["ruhani","روحانی"],["ruh","روح"],["rizayət","رضایت"],["riza","رضا"],["riyaziyyat","ریاضیات"],["rıza","رضا"],["rəqs","رقص"],["rəiyyət","رعیت"],["rəhm","رحم"],["rəhim","رحیم"],["rədd","رد"],["reyhan","ریحان"],["respublika","رئسپوبلیکا"],["respoblika","رئسپوبلیکا"],["razı","راضی"],["rahat","راحت"],["rabitə","رابطه‌"],["qüvvət","قوت"],["qüvvə","قوه‌"],["quvvət","قوت"],["quvvə","قوه‌"],["qövm","قوم"],["qəzəb","غضب"],["qəzəb","غضب"],["qəzavət","قضاوت"],["qəti","قطعی"],["qəsəbə","قصبه‌"],["qəsdən","قصداً"],["qəsd","قصد"],["qərəz","غرض"],["qərb","غرب"],["qənaət","قناعت"],["qənaət","قناعت"],["qəmgin","غمگین"],["qələbə","غلبه"],["qədir","غدیر"],["qəbilə","قبیله‌"],["qəbahət","قباحت"],["qeyri-müəyyən","غیر معین"],["qeyri","غیری"],["qazi","قاضی"],["qazı","قاضی"],["peyğəmbər","پیغمبر"],["ömür","عؤمور"],["ömr","عمر"],["ömər","عمر"],["ö","اؤ"],["osmanlı","عثمانلی"],["o","او"],["nümayəndə","نماینده‌"],["nüfuz","نفوذ"],["numayəndə","نماینده‌"],["nufuz","نفوذ"],["nöqtə","نقطه‌"],["nöqsan","نقصان"],["nizami","نظامی"],["nitq","نیطق"],["nisbətən","نسبتا"],["nicat","نجات"],["nəzr","نذر"],["nəzəriyyə","نظریه‌"],["nəzər","نظر"],["nəzarət","نظارت"],["nəsihətimə","نصیحتیمه"],["nəsihət","نصیحت"],["nələr","نه‌لر"],["nədən","ندن"],["nemət","نعمت"],["nefrin","نفرین"],["nazir","ناظر"],["nazim","ناظیم"],["naxalis","ناخالص"],["nasir","ناصر"],["narazı","ناراضی"],["narahat","ناراحات"],["naqis","ناقص"],["namizəd","نامیزد"],["naməhrəm","نامحرم"],["müzakirə","موذاکیره‌"],["müvəqqət","موقت"],["müvəffəqiyyət","موفقیت"],["müttəhid","متحد"],["mütləq","موطلق"],["mütəxəssis","متخصص"],["mütəradif","مترادیف"],["müştərək","مشترک"],["müşayiət","موشایعت"],["müsəlman","مسلمان"],["müsəlla","مصلی"],["müsahib","موصاحیب"],["mürtəce","مورتجع"],["müraciət","مراجعت"],["müqəddəs","مقدس"],["müqavimət","مقاومت"],["mühit","موحیط"],["mühəqqiq","محقق"],["mühasirə","محاصره‌"],["müharibədən","محاریبه‌دن"],["müharibə","محاربه‌"],["mühafizə","محافظه‌"],["müəzzin","مؤذن"],["müəyyən","معین"],["müəllim","معلم"],["müəllif","مؤلف"],["müddət","مدت"],["müdafiə","مدافعه‌"],["müavin","موعاوین"],["müasir","معاصر"],["müəllim","معلم"],["mustafa","مصطفی"],["muraciət","مراجعت"],["muqavimət","مقاومت"],["muharibə","محاربه‌"],["muhamməd","محمد"],["mudafiə","مدافعه‌"],["muasir","معاصر"],["mövzu","مؤوضو"],["mövqe","مؤقع"],["mötəbər","معتبر"],["mömün","مؤمن"],["mömin","مؤمن"],["möcüzə","معجزه‌"],["mötəbər","معتبر"],["mömin","مؤمن"],["mosul","موصول"],["mohamməd","محمد"],["misra","میصراع"],["misir","مصر"],["misal","مثال"],["milli","میللی"],["microsoft","مایکروسافت"],["məzlum","مظلوم"],["məzhəb","مذهب"],["məxsus","مخصوص"],["mətbuat","مطبوعات"],["mətbuat","مطبوعات"],["məsul","مسئول"],["məsud","مسعود"],["məsləhət","مصلحت"],["məsələn","مثلاً"],["məsələ","مسئله‌"],["məsəl","مثل"],["məruz","معروض"],["mərhələ","مرحله‌"],["məqsədəuyğun","مقصده اویغون"],["məqsəd","مقصد"],["məntəqə","منطقه‌"],["mənşə","منشأ"],["mənşə","منشأ"],["mənəvi","معنوی"],["mənbə","منبع"],["mənbə","منبع"],["mənalı","معنالی"],["mənafe","منافع"],["məna","معنا"],["məmur","مأمور"],["məlumat","معلومات"],["məlum","معلوم"],["məhz","محض"],["məhv","محو"],["məhsuludur","محصولودور"],["məhsul","محصول"],["məhrəm","محرم"],["məhmud","محمود"],["məhkum","محکوم"],["məhkəmə","محکمه‌"],["məhəmmədəli","محمدعلی"],["məhəmməd","محمد"],["məhəllə","محله‌"],["məhəl","محل"],["məhəbbət","محبت"],["məhdudiyyət","محدودیت"],["məhdud","محدود"],["məclis","مجلیس"],["məbud","معبود"],["məlumat","معلومات"],["məlum","معلوم"],["məbud","معبود"],["meydan","میدان"],["maviyə","معاویه‌"],["mane","مانع"],["mahmud","محمود"],["mahmud","محمود"],["mahmıd","محمود"],["mahal","محل"],["maddi","مادی"],["maarif","معاریف"],["lütfən","لطفاً"],["lizzət","لذت"],["linux","لینوکس"],["ləzzət","لذت"],["ləziz","لذیذ"],["lətafət","لطافت"],["lənət","لعنت"],["layihə","لاییحه‌"],["küçәdә","کوچه‌ده"],["köməy","کمک"],["kazım","کاظیم"],["kamal","کمال"],["kağız","کاغیذ"],["java","جاوا"],["izzət","عزت"],["izah","ایضاح"],["ixlas","اخلاص"],["ittiham","اتهام"],["ittihaf","اتحاف"],["ittifaq","اتفاق"],["ithaf","اتحاف"],["itaət","اطاعت"],["istisna","استثنا"],["istirahət","استراحت"],["istilah","ایصطیلاح"],["istəmir","ایسته‌میر"],["istehsal","ایستحصال"],["istedad","ایستعداد"],["islam","ایسلام"],["islahat","اصلاحات"],["islah","اصلاح"],["isfahan","اصفهان"],["isbat","اثبات"],["isa","عیسی"],["irticai","ارتجاعی"],["irs","ارث"],["iqtisadiyyat","اقتصادیات"],["iqtisad","اقتصاد"],["iqtidar","اقتدار"],["inzibat","اینضیباط"],["inzibat","اینضیباط"],["insan","انسان"],["inhisar","انحصار"],["incəsənət","اینجه‌صنعت"],["imza","ایمضا"],["imran","عمران"],["iltisaqi","التصاقی"],["iltisaqı","التصاقی"],["ihtikar","احتکار"],["ideal","ایده‌آل"],["iddia","ادعا"],["iddəa","ادعا"],["ictimai","اجتماعی"],["ibn","ابن"],["ibarət","عبارت"],["ibadət","عبادت"],["i","ای"],["hüzur","حضور"],["hüseyn","حسین"],["hüquqşünas","حقوقشوناس"],["hüquq","حقوق"],["hükumət","حکومت"],["hükm","حکم"],["hüdud","حدود"],["huquq","حقوق"],["hukumət","حکومت"],["hövzə","حوضه‌"],["hövsələ","حؤصله"],["hörmətli","حؤرمتلی"],["hörmət","حؤرمت"],["hökümət","حکومت"],["hökumət","حکومت"],["hökmran","حؤکمران"],["hökm","حؤکم"],["hiyləgər","حیله‌گر"],["hiylə","حیله‌"],["hissə","حصه‌"],["hiss","حیس"],["himmət","همت"],["himayə","حمایه‌"],["hilə","حیله‌"],["hikmət","حیکمت"],["hikayət","حکایه‌"],["hikayə","حکایه‌"],["hicab","حجاب"],["həyətləri","حیطلری"],["həyət","حه‌یط"],["həyat","حیات"],["həvalə","حواله‌"],["hətta","حتی"],["həsr","حصر"],["həsr","حصر"],["həsən","حسن"],["həsb","حسب"],["hərfi","حرفی"],["hərf","حرف"],["hərf","حرف"],["hərəkət","حرکت"],["hərəkat","حرکات"],["hərb","حرب"],["həqiqi","حقیقی"],["həqiqət","حقیقت"],["həqarət","حقارت"],["həll","حل"],["hələb","حلب"],["hələ","هله‌"],["həl","حل"],["hədiyyəlik","هدیه‌لیک"],["hədiyyə","هدیه‌"],["həddad","حداد"],["hədd","حد"],["həd","حد"],["həbs","حبس"],["heyvanın","حیوانین"],["heyvan","حیوان"],["heyvan","حیوان"],["heysiyyət","حیثیت"],["heysiyyat","حیثیت"],["heyrət","حیرت"],["heykəl","هیکل"],["heydər","حیدر"],["hesab","حساب"],["hekayət","حکایه‌"],["hekayə","حکایه‌"],["hazır","حاضر"],["hasilat","حاصیلات"],["hasil","حاصیل"],["haram","حرام"],["haqq","حاق"],["haq","حاق"],["hal","حال"],["hakimiyyətlə","حاکیمیت‌له"],["hakimiyyət","حاکمیت"],["hakim","حاکم"],["hafiz","حافیظ"],["hadisə","حادثه‌"],["hacı","حاجی"],["güzəşt","گذشت"],["gəlməyərək","گلمه‌یه‌رک"],["gələn","گلن"],["gedən","گئدن"],["gecə","گئجه‌"],["füzuli","فضولی"],["fürsət","فورصت"],["fuzuli","فضولی"],["fransiz","فرانسه‌"],["fitrətən","فطرتاً"],["fitrət","فطرت"],["firib","فریب"],["fəzlan","فضلان"],["fəzilət","فضیلت"],["fəyyaz","فیاض"],["fəth","فتح"],["fətəli","فتحعلی"],["fəsli","فصلی"],["fərz","فرض"],["fərəh","فرح"],["fəqət","فقط"],["fələstin","فلسطین"],["fəaliyyət","فعالیت"],["fəaliyyət","فعالیت"],["fəal","فعال"],["fayl","فایل"],["fatimiyyə","فاطمیه‌"],["fatimə","فاطمه‌"],["fasilə","فاصیله‌"],["faciə","فاجعه‌"],["əziz","عزیز"],["əziyyət","اذیت"],["əzəmət","عظمت"],["əzan","اذان"],["əzab","عذاب"],["əvvəl","اول"],["ətraf","اطراف"],["əsr","عصر"],["əslində","اصلینده‌"],["əsl","اصل"],["əsil","اصیل"],["əsgər","عسگر"],["əsərlərdən","اثرلردن"],["əsəri","اثری"],["əsər","اثر"],["əsasən","اساساً"],["ərz","عرض"],["ərsə","عرصه‌"],["ərəb","عرب"],["ərazi","اراضی"],["ərazı","اراضی"],["əql","عقل"],["ənənə","عنعنه‌"],["əmmə","عمه‌"],["əmin","امین"],["əmi","عمی"],["əməliyyat","عملیات"],["əməl","عمل"],["əllə","ال‌له‌"],["əlin","الین"],["əlimiz","الیمیز"],["əlil","علیل"],["əlifba","الیفبا"],["əli","علی"],["əleyh","علیه"],["əlbəttə","البته‌"],["əlavə","علاوه‌"],["əlaqə","علاقه‌"],["əlamət","علامت"],["əlaəddin","علاالدین"],["əksi","عکسی"],["əksəriyyət","اکثریت"],["əksər","اکثر"],["əks","عکس"],["əhvalat","احوالات"],["əhmədinejat","احمدی‌نژاد"],["əhmədinejad","احمدی‌نژاد"],["əhməd","احمد"],["əhatə","احاطه‌"],["əfzəl","افضل"],["ədu","عدو"],["ədliyyə","عدلیه‌"],["ədalət","عدالت"],["əcəba","عجبا"],["əcaba","عجبا"],["ə","ا"],["eyni","عینی"],["etiraz","اعتراض"],["etiraf","اعتراف"],["etiqad","اعتقاد"],["etibarən","اعتباراً"],["etibar","اعتبار"],["eşq","عشق"],["elmi","علمی"],["elm","علم"],["elan","اعلان"],["ehtiyat","احتیاط"],["ehtiyac","احتیاج"],["ehtimal","احتمال"],["ehtikar","احتکار"],["edam","اعدام"],["etiraz","اعتراض"],["etiraf","اعتراف"],["etibarən","اعتباراً"],["etibar","اعتبار"],["e","ائ"],["dua","دعا"],["dr","دؤکتور"],["diqqət","دقت"],["dəyiş","ده‌ییش"],["dəyərində","ده‌یرینده"],["dəyən","ده‌ین"],["dəvət","دعوت"],["dərəli","دره‌لی"],["dərəcə","درجه‌"],["dəfə","دفعه‌"],["dədə","دده‌"],["çəmənliyi","چمنلیگی"],["cüzi","جزعی"],["cümlə","جمله‌"],["cümə","جومعه‌"],["cidd","جد"],["cərrahi","جراحی"],["cərrahı","جراحی"],["cəmiyyət","جمعیت"],["cəm","جمع"],["cəhənnəm","جهنم"],["cəfər","جعفر"],["cd","سی‌دی"],["camaət","جماعت"],["böhran","بحران"],["biәdәblik","بی‌ادبلیک"],["biədəblik","بی‌ادبلیک"],["bəzi","بعضی"],["bəzən","بعضن"],["bəy","به‌ی"],["bələmi","بلعمی"],["bəhs","بحث"],["bəhreyn","بحرئین"],["bədii","بدیعی"],["bəzi","بعضی"],["belə","بئله‌"],["bağlı","باغلی"],["azərbaycanın","آذربایجانین"],["azərbaycan","آذربایجان"],["azər","آذر"],["azerbaycan","آذربایجان"],["azerbaijan","آذربایجان"],["azan","اذان"],["ayid","عایید"],["aşura","عاشورا"],["amma","اما"],["amil","عامل"],["allah","الله‌"],["alim","عالیم"],["ali","عالی"],["aləm","عالم"],["ailəsi","عائیله‌سی"],["ailənin","عائیله‌نین"],["ailə","عائله‌"],["aid","عایید"],["ağıl","عقل"],["adil","عادیل"],["adi","عادی"],["adət","عادت"],["abihəyat","آبی‌حیات"],["abid","عابد"],["abdullah","عبدالله"],["abdulla","عبدالله"],["abbas","عباس"],["a","آ"],["&","و"]]
	if 'à' in azstr or 'å' in azstr or 'è' in azstr or 'î' in azstr or 'ÿ' in azstr or 'þ' in azstr:
		azstr = vajaqconvert(azstr)
		edit1.setText(azstr)
	azstr = azstr.strip()
	azstr = firstconvert(azstr)
	azstr = azstr.lower()
	azstr = azstr.split()
	for i, s in enumerate(azstr):
		if convertableword(s):
			s = firstwordconvert(s, wordslist)
			s = firstcharacter(s)
			s = middleconvert(s)
			s = strreplace(s)
		azstr[i] = s

	azstr = " ".join(azstr)
	azstr = lastconvert(azstr)
	edit2.setText(azstr)

# Create the Qt Application
app = QApplication(sys.argv)
form = QWidget()
edit1 = QTextEdit()
edit2 = QTextEdit()
edit2.setLayoutDirection(Qt.RightToLeft)
edit2.setAlignment(Qt.AlignRight)
button = QPushButton("Convert")
button.clicked.connect(convert)
clearbutton = QPushButton("Clear")
clearbutton.clicked.connect(clear_text)
layout = QVBoxLayout()
layout.addWidget(edit1)
layout.addWidget(button)
layout.addWidget(clearbutton)
layout.addWidget(edit2)
form.setLayout(layout)
form.resize(800, 600)
form.setWindowTitle("Azj 2 Azb Convert")
form.setStyleSheet("font-family: Tahoma; font-size: 16px;")
form.show()
sys.exit(app.exec_())
