# modules

import pyfiglet
import termcolor

# end modules

# Tool name by pyfiglet

TL_NAME_text = pyfiglet.figlet_format("Numbers To Text")
TL_NAME = termcolor.colored(TL_NAME_text, 'green')

print(TL_NAME) 
print(termcolor.colored('Created by izox\ntwitter : @izox0\n', 'blue'))

# end print tool name

lang = input("Chose a language [ar/en] : ")

if (lang == 'en' or lang == 'En' or lang == 'EN'):
	num_text_en = [
		'One',
		'Two',
		'Three',
		'Four',
		'Five',
		'Six',
		'Seven',
		'Eight',
		'Nine',
		'Ten',
		'Eleven',
		'Twelve',
		'Thirteen', 
		'Fourteen',
		'Fifteen',
		'Sixteen',
		'Seventeen',
		'Eighteen',
		'Nineteen',
		'Twenty', #20
		'Twenty-one', #21
		'Twenty-two', #22
		'Twenty-three', #23
		'Twenty-four',
		'Twenty-five',
		'Twenty-six',
		'Twenty-seven',
		'Twenty-eight',
		'Twenty-nine',
		'Thirty',
		'Thirty-one',
		'Thirty-two',
		'Thirty-three',
		'Thirty-four',
		'Thirty-five', 
		'Thirty-six',
		'Thirty-seven',
		'Thirty-eight',
		'Thirty-nine',
		'Forty',
		'Forty-one',
		'Forty-two',
		'Forty-three',
		'Forty-four',
		'Forty-five',
		'Forty-six',
		'Forty-seven',
		'Forty-eight',
		'Forty-nine',
		'Fifty'
	]
	
# 	print(num_text_en)

	try:
		num_en_check = int(input("enter number (1-50) : "))
	except ValueError:
		print(termcolor.colored("\nyou have to write a number, Try again \n", 'red'))
		num_en_check = 10000000000000000000000
	finally:
		num_en = num_en_check

	if (num_en == 1):
		print(termcolor.colored("\n"+num_text_en[0]+"\n", 'blue'))
		# 1
	if (num_en == 2):
		print(termcolor.colored("\n"+num_text_en[1]+"\n", 'blue'))
		# 2
	if (num_en == 3):
		print(termcolor.colored("\n"+num_text_en[2]+"\n", 'blue'))
		# 3
	if (num_en == 4):
		print(termcolor.colored("\n"+num_text_en[3]+"\n", 'blue'))
		# 4
	if (num_en == 5):
		print(termcolor.colored("\n"+num_text_en[4]+"\n", 'blue'))
		# 5
	if (num_en == 6):
		print(termcolor.colored("\n"+num_text_en[5]+"\n", 'blue'))
		# 6
	if (num_en == 7):
		print(termcolor.colored("\n"+num_text_en[6]+"\n", 'blue'))
		# 7
	if (num_en == 8):
		print(termcolor.colored("\n"+num_text_en[7]+"\n", 'blue'))
		# 8
	if (num_en == 9):
		print(termcolor.colored("\n"+num_text_en[8]+"\n", 'blue'))
		# 9
	if (num_en == 10):
		print(termcolor.colored("\n"+num_text_en[9]+"\n", 'blue'))
		# 10

	if (num_en == 11):
		print(termcolor.colored("\n"+num_text_en[10]+"\n", 'blue'))
		# 1
	if (num_en == 12):
		print(termcolor.colored("\n"+num_text_en[11]+"\n", 'blue'))
		# 2
	if (num_en == 13):
		print(termcolor.colored("\n"+num_text_en[12]+"\n", 'blue'))
		# 3
	if (num_en == 14):
		print(termcolor.colored("\n"+num_text_en[13]+"\n", 'blue'))
		# 4
	if (num_en == 15):
		print(termcolor.colored("\n"+num_text_en[14]+"\n", 'blue'))
		# 5
	if (num_en == 16):
		print(termcolor.colored("\n"+num_text_en[15]+"\n", 'blue'))
		# 6
	if (num_en == 17):
		print(termcolor.colored("\n"+num_text_en[16]+"\n", 'blue'))
		# 7
	if (num_en == 18):
		print(termcolor.colored("\n"+num_text_en[17]+"\n", 'blue'))
		# 8
	if (num_en == 19):
		print(termcolor.colored("\n"+num_text_en[18]+"\n", 'blue'))
		# 9
	if (num_en == 20):
		print(termcolor.colored("\n"+num_text_en[19]+"\n", 'blue'))
		# 10
	if (num_en == 21):
		print(termcolor.colored("\n"+num_text_en[20]+"\n", 'blue'))
		# 1
	if (num_en == 22):
		print(termcolor.colored("\n"+num_text_en[21]+"\n", 'blue'))
		# 2
	if (num_en == 23):
		print(termcolor.colored("\n"+num_text_en[22]+"\n", 'blue'))
		# 3
	if (num_en == 24):
		print(termcolor.colored("\n"+num_text_en[23]+"\n", 'blue'))
		# 4
	if (num_en == 25):
		print(termcolor.colored("\n"+num_text_en[24]+"\n", 'blue'))
		# 5
	if (num_en == 26):
		print(termcolor.colored("\n"+num_text_en[25]+"\n", 'blue'))
		# 6
	if (num_en == 27):
		print(termcolor.colored("\n"+num_text_en[26]+"\n", 'blue'))
		# 7
	if (num_en == 28):
		print(termcolor.colored("\n"+num_text_en[27]+"\n", 'blue'))
		# 8
	if (num_en == 29):
		print(termcolor.colored("\n"+num_text_en[28]+"\n", 'blue'))
		# 9
	if (num_en == 30):
		print(termcolor.colored("\n"+num_text_en[29]+"\n", 'blue'))
		# 10

	if (num_en == 31):
		print(termcolor.colored("\n"+num_text_en[30]+"\n", 'blue'))
		# 1
	if (num_en == 32):
		print(termcolor.colored("\n"+num_text_en[31]+"\n", 'blue'))
		# 2
	if (num_en == 33):
		print(termcolor.colored("\n"+num_text_en[32]+"\n", 'blue'))
		# 3
	if (num_en == 34):
		print(termcolor.colored("\n"+num_text_en[33]+"\n", 'blue'))
		# 4
	if (num_en == 35):
		print(termcolor.colored("\n"+num_text_en[34]+"\n", 'blue'))
		# 5
	if (num_en == 36):
		print(termcolor.colored("\n"+num_text_en[35]+"\n", 'blue'))
		# 6
	if (num_en == 37):
		print(termcolor.colored("\n"+num_text_en[36]+"\n", 'blue'))
		# 7
	if (num_en == 38):
		print(termcolor.colored("\n"+num_text_en[37]+"\n", 'blue'))
		# 8
	if (num_en == 39):
		print(termcolor.colored("\n"+num_text_en[38]+"\n", 'blue'))
		# 9
	if (num_en == 40):
		print(termcolor.colored("\n"+num_text_en[39]+"\n", 'blue'))
		# 10

	if (num_en == 41):
		print(termcolor.colored("\n"+num_text_en[40]+"\n", 'blue'))
		# 1
	if (num_en == 42):
		print(termcolor.colored("\n"+num_text_en[41]+"\n", 'blue'))
		# 2
	if (num_en == 43):
		print(termcolor.colored("\n"+num_text_en[42]+"\n", 'blue'))
		# 3
	if (num_en == 44):
		print(termcolor.colored("\n"+num_text_en[43]+"\n", 'blue'))
		# 4
	if (num_en == 45):
		print(termcolor.colored("\n"+num_text_en[44]+"\n", 'blue'))
		# 5
	if (num_en == 46):
		print(termcolor.colored("\n"+num_text_en[45]+"\n", 'blue'))
		# 6
	if (num_en == 47):
		print(termcolor.colored("\n"+num_text_en[46]+"\n", 'blue'))
		# 7
	if (num_en == 48):
		print(termcolor.colored("\n"+num_text_en[47]+"\n", 'blue'))
		# 8
	if (num_en= 49):
		print(termcolor.colored("\n"+num_text_en[48]+"\n", 'blue'))
		# 9
	if (num_en == 50):
		print(termcolor.colored("\n"+num_text_en[49]+"\n", 'blue'))
		# 10
	
elif lang == 'ar' or lang == 'Ar' or lang == 'AR':
	num_text_ar = [
		'واحد',
		"اثنين",
		"ثلاثة",
		"اربعة",
		"خمسة",
		"ستة",
		"سبعة",
		"ثمانية",
		"تسعة",
		"عشرة",
		"احدى عشر",
		"اثنى عشر",
		"ثلاثة عشر",
		"اربعة عشر",
		"خمسة عشر",
		"ستة عشر",
		"سبعة عشر",
		"ثمانية عشر",
		"تسعة عشر",
		"عشرين",
		"واحد وعشرين",
		"اثنين وعشرين",
		"ثلاثة وعشرين",
		"اربعة وعشرين",
		"خمسة وعشرين",
		"ستة وعشرين",
		"سبعة وعشرين",
		"ثمانية وعشرين",
		"تسعة وعشرين",
		"ثلاثين",
		"واحد وثلاثين",
		"اثنين وثلاثين",
		"ثلاثة وثلاثين",
		"اربعة وثلاثين",
		"خمسة وثلاثين",
		"ستة وثلاثين",
		"سبعة وثلاثين",
		"ثمانية وثلاثين",
		"تسعة وثلاثين",
		"اربعين",
		"واحد واربعين",
		"اثنين واربعين",
		"ثلاثة واربعين",
		"اربعة واربعين",
		"خمسة واربعين",
		"ستة واربعين",
		"سبعة واربعين",
		"ثمانية واربعين",
		"تسعة واربعين",
		"خمسين",
		"واحد وخمسين",
		"اثنين وخمسين",
		"ثلاثة وخمسين",
		"اربعة وخمسين",
		"خمسة وخمسين",
		"ستة وخمسين",
		"سبعة وخمسين",
		"ثمانية وخمسين",
		"تسعة وخمسين",
		"ستين",
		"واحد وستين",
		"اثنين وستين",
		"ثلاثة وستين",
		"اربعة وستين",
		"خمسة وستين",
		"ستة وستين",
		"سبعة وستين",
		"ثمانية وستين",
		"تسعة وستين",
		"سبعين",
		"واحد وسبعين",
		"اثنين واسبعين",
		"ثلاثة وسبعين",
		"اربعة وسبعين",
		"خمسة وسبعين",
		"ستة وسبعين",
		"سبعة وسبعين",
		"ثمانية وسبعين",
		"تسعة وسبعين",
		"ثمانين",
		"واحد وثمانين",
		"اثنين وثمانين",
		"ثلاثة وثمانين",
		"اربعة وثمانين",
		"خمسة وثمانين",
		"ستة وثمانين",
		"سبعة وثمانين",
		"ثمانية وثمانين",
		"تسعة وثمانين",
		"تسعين",
		"واحد وتسعين",
		"اثنين وتسعين",
		"ثلاثة وتسعين",
		"اربعة وتسعين",
		"خمسة وتسعين",
		"ستة وتسعين",
		"سبعة وتسعين",
		"ثمانية وتسعين",
		"تسعة وتسعين",
		"مئة"
	]
	try:
		num_ar_check = int(input("ادخل الرقم (1-100) : "))
	except ValueError:
		print(termcolor.colored("\nyou have to write a number, Try again \n", 'red'))
		num_ar_check = 10000000000000000000000
	finally:
		num_ar = num_ar_check

	if (num_ar == 1):
		print(termcolor.colored("\n"+num_text_ar[0]+"\n", 'blue'))
		# 1
	if (num_ar == 2):
		print(termcolor.colored("\n"+num_text_ar[1]+"\n", 'blue'))
		# 2
	if (num_ar == 3):
		print(termcolor.colored("\n"+num_text_ar[2]+"\n", 'blue'))
		# 3
	if (num_ar == 4):
		print(termcolor.colored("\n"+num_text_ar[3]+"\n", 'blue'))
		# 4
	if (num_ar == 5):
		print(termcolor.colored("\n"+num_text_ar[4]+"\n", 'blue'))
		# 5
	if (num_ar == 6):
		print(termcolor.colored("\n"+num_text_ar[5]+"\n", 'blue'))
		# 6
	if (num_ar == 7):
		print(termcolor.colored("\n"+num_text_ar[6]+"\n", 'blue'))
		# 7
	if (num_ar == 8):
		print(termcolor.colored("\n"+num_text_ar[7]+"\n", 'blue'))
		# 8
	if (num_ar == 9):
		print(termcolor.colored("\n"+num_text_ar[8]+"\n", 'blue'))
		# 9
	if (num_ar == 10):
		print(termcolor.colored("\n"+num_text_ar[9]+"\n", 'blue'))
		# 10

	if (num_ar == 11):
		print(termcolor.colored("\n"+num_text_ar[10]+"\n", 'blue'))
		# 1
	if (num_ar == 12):
		print(termcolor.colored("\n"+num_text_ar[11]+"\n", 'blue'))
		# 2
	if (num_ar == 13):
		print(termcolor.colored("\n"+num_text_ar[12]+"\n", 'blue'))
		# 3
	if (num_ar == 14):
		print(termcolor.colored("\n"+num_text_ar[13]+"\n", 'blue'))
		# 4
	if (num_ar == 15):
		print(termcolor.colored("\n"+num_text_ar[14]+"\n", 'blue'))
		# 5
	if (num_ar == 16):
		print(termcolor.colored("\n"+num_text_ar[15]+"\n", 'blue'))
		# 6
	if (num_ar == 17):
		print(termcolor.colored("\n"+num_text_ar[16]+"\n", 'blue'))
		# 7
	if (num_ar == 18):
		print(termcolor.colored("\n"+num_text_ar[17]+"\n", 'blue'))
		# 8
	if (num_ar == 19):
		print(termcolor.colored("\n"+num_text_ar[18]+"\n", 'blue'))
		# 9
	if (num_ar == 20):
		print(termcolor.colored("\n"+num_text_ar[19]+"\n", 'blue'))
		# 10
	if (num_ar == 21):
		print(termcolor.colored("\n"+num_text_ar[20]+"\n", 'blue'))
		# 1
	if (num_ar == 22):
		print(termcolor.colored("\n"+num_text_ar[21]+"\n", 'blue'))
		# 2
	if (num_ar == 23):
		print(termcolor.colored("\n"+num_text_ar[22]+"\n", 'blue'))
		# 3
	if (num_ar == 24):
		print(termcolor.colored("\n"+num_text_ar[23]+"\n", 'blue'))
		# 4
	if (num_ar == 25):
		print(termcolor.colored("\n"+num_text_ar[24]+"\n", 'blue'))
		# 5
	if (num_ar == 26):
		print(termcolor.colored("\n"+num_text_ar[25]+"\n", 'blue'))
		# 6
	if (num_ar == 27):
		print(termcolor.colored("\n"+num_text_ar[26]+"\n", 'blue'))
		# 7
	if (num_ar == 28):
		print(termcolor.colored("\n"+num_text_ar[27]+"\n", 'blue'))
		# 8
	if (num_ar == 29):
		print(termcolor.colored("\n"+num_text_ar[28]+"\n", 'blue'))
		# 9
	if (num_ar == 30):
		print(termcolor.colored("\n"+num_text_ar[29]+"\n", 'blue'))
		# 10

	if (num_ar == 31):
		print(termcolor.colored("\n"+num_text_ar[30]+"\n", 'blue'))
		# 1
	if (num_ar == 32):
		print(termcolor.colored("\n"+num_text_ar[31]+"\n", 'blue'))
		# 2
	if (num_ar == 33):
		print(termcolor.colored("\n"+num_text_ar[32]+"\n", 'blue'))
		# 3
	if (num_ar == 34):
		print(termcolor.colored("\n"+num_text_ar[33]+"\n", 'blue'))
		# 4
	if (num_ar == 35):
		print(termcolor.colored("\n"+num_text_ar[34]+"\n", 'blue'))
		# 5
	if (num_ar == 36):
		print(termcolor.colored("\n"+num_text_ar[35]+"\n", 'blue'))
		# 6
	if (num_ar == 37):
		print(termcolor.colored("\n"+num_text_ar[36]+"\n", 'blue'))
		# 7
	if (num_ar == 38):
		print(termcolor.colored("\n"+num_text_ar[37]+"\n", 'blue'))
		# 8
	if (num_ar == 39):
		print(termcolor.colored("\n"+num_text_ar[38]+"\n", 'blue'))
		# 9
	if (num_ar == 40):
		print(termcolor.colored("\n"+num_text_ar[39]+"\n", 'blue'))
		# 10

	if (num_ar == 41):
		print(termcolor.colored("\n"+num_text_ar[40]+"\n", 'blue'))
		# 1
	if (num_ar == 42):
		print(termcolor.colored("\n"+num_text_ar[41]+"\n", 'blue'))
		# 2
	if (num_ar == 43):
		print(termcolor.colored("\n"+num_text_ar[42]+"\n", 'blue'))
		# 3
	if (num_ar == 44):
		print(termcolor.colored("\n"+num_text_ar[43]+"\n", 'blue'))
		# 4
	if (num_ar == 45):
		print(termcolor.colored("\n"+num_text_ar[44]+"\n", 'blue'))
		# 5
	if (num_ar == 46):
		print(termcolor.colored("\n"+num_text_ar[45]+"\n", 'blue'))
		# 6
	if (num_ar == 47):
		print(termcolor.colored("\n"+num_text_ar[46]+"\n", 'blue'))
		# 7
	if (num_ar == 48):
		print(termcolor.colored("\n"+num_text_ar[47]+"\n", 'blue'))
		# 8
	if (num_ar == 49):
		print(termcolor.colored("\n"+num_text_ar[48]+"\n", 'blue'))
		# 9
	if (num_ar == 50):
		print(termcolor.colored("\n"+num_text_ar[49]+"\n", 'blue'))
		# 10

	if (num_ar == 51):
		print(termcolor.colored("\n"+num_text_ar[50]+"\n", 'blue'))
		# 1
	if (num_ar == 52):
		print(termcolor.colored("\n"+num_text_ar[51]+"\n", 'blue'))
		# 2
	if (num_ar == 53):
		print(termcolor.colored("\n"+num_text_ar[52]+"\n", 'blue'))
		# 3
	if (num_ar == 54):
		print(termcolor.colored("\n"+num_text_ar[53]+"\n", 'blue'))
		# 4
	if (num_ar == 55):
		print(termcolor.colored("\n"+num_text_ar[4]+"\n", 'blue'))
		# 5
	if (num_ar == 56):
		print(termcolor.colored("\n"+num_text_ar[55]+"\n", 'blue'))
		# 6
	if (num_ar == 57):
		print(termcolor.colored("\n"+num_text_ar[56]+"\n", 'blue'))
		# 7
	if (num_ar == 58):
		print(termcolor.colored("\n"+num_text_ar[57]+"\n", 'blue'))
		# 8
	if (num_ar == 59):
		print(termcolor.colored("\n"+num_text_ar[58]+"\n", 'blue'))
		# 9
	if (num_ar == 60):
		print(termcolor.colored("\n"+num_text_ar[59]+"\n", 'blue'))
		# 10

	if (num_ar == 61):
		print(termcolor.colored("\n"+num_text_ar[60]+"\n", 'blue'))
		# 1
	if (num_ar == 62):
		print(termcolor.colored("\n"+num_text_ar[61]+"\n", 'blue'))
		# 2
	if (num_ar == 63):
		print(termcolor.colored("\n"+num_text_ar[62]+"\n", 'blue'))
		# 3
	if (num_ar == 64):
		print(termcolor.colored("\n"+num_text_ar[63]+"\n", 'blue'))
		# 4
	if (num_ar == 65):
		print(termcolor.colored("\n"+num_text_ar[64]+"\n", 'blue'))
		# 5
	if (num_ar == 66):
		print(termcolor.colored("\n"+num_text_ar[65]+"\n", 'blue'))
		# 6
	if (num_ar == 67):
		print(termcolor.colored("\n"+num_text_ar[66]+"\n", 'blue'))
		# 7
	if (num_ar == 68):
		print(termcolor.colored("\n"+num_text_ar[67]+"\n", 'blue'))
		# 8
	if (num_ar == 69):
		print(termcolor.colored("\n"+num_text_ar[68]+"\n", 'blue'))
		# 9
	if (num_ar == 70):
		print(termcolor.colored("\n"+num_text_ar[69]+"\n", 'blue'))
		# 10

	if (num_ar == 71):
		print(termcolor.colored("\n"+num_text_ar[70]+"\n", 'blue'))
		# 1
	if (num_ar == 72):
		print(termcolor.colored("\n"+num_text_ar[71]+"\n", 'blue'))
		# 2
	if (num_ar == 73):
		print(termcolor.colored("\n"+num_text_ar[72]+"\n", 'blue'))
		# 3
	if (num_ar == 74):
		print(termcolor.colored("\n"+num_text_ar[73]+"\n", 'blue'))
		# 4
	if (num_ar == 75):
		print(termcolor.colored("\n"+num_text_ar[74]+"\n", 'blue'))
		# 5
	if (num_ar == 76):
		print(termcolor.colored("\n"+num_text_ar[75]+"\n", 'blue'))
		# 6
	if (num_ar == 77):
		print(termcolor.colored("\n"+num_text_ar[76]+"\n", 'blue'))
		# 7
	if (num_ar == 78):
		print(termcolor.colored("\n"+num_text_ar[77]+"\n", 'blue'))
		# 8
	if (num_ar == 79):
		print(termcolor.colored("\n"+num_text_ar[78]+"\n", 'blue'))
		# 9
	if (num_ar == 80):
		print(termcolor.colored("\n"+num_text_ar[79]+"\n", 'blue'))
		# 10

	if (num_ar == 81):
		print(termcolor.colored("\n"+num_text_ar[80]+"\n", 'blue'))
		# 1
	if (num_ar == 82):
		print(termcolor.colored("\n"+num_text_ar[81]+"\n", 'blue'))
		# 2
	if (num_ar == 83):
		print(termcolor.colored("\n"+num_text_ar[82]+"\n", 'blue'))
		# 3
	if (num_ar == 84):
		print(termcolor.colored("\n"+num_text_ar[83]+"\n", 'blue'))
		# 4
	if (num_ar == 85):
		print(termcolor.colored("\n"+num_text_ar[84]+"\n", 'blue'))
		# 5
	if (num_ar == 86):
		print(termcolor.colored("\n"+num_text_ar[85]+"\n", 'blue'))
		# 6
	if (num_ar == 87):
		print(termcolor.colored("\n"+num_text_ar[86]+"\n", 'blue'))
		# 7
	if (num_ar == 88):
		print(termcolor.colored("\n"+num_text_ar[87]+"\n", 'blue'))
		# 8
	if (num_ar == 89):
		print(termcolor.colored("\n"+num_text_ar[88]+"\n", 'blue'))
		# 9
	if (num_ar == 90):
		print(termcolor.colored("\n"+num_text_ar[89]+"\n", 'blue'))
		# 10

	if (num_ar == 91):
		print(termcolor.colored("\n"+num_text_ar[90]+"\n", 'blue'))
		# 1
	if (num_ar == 92):
		print(termcolor.colored("\n"+num_text_ar[91]+"\n", 'blue'))
		# 2
	if (num_ar == 93):
		print(termcolor.colored("\n"+num_text_ar[92]+"\n", 'blue'))
		# 3
	if (num_ar == 94):
		print(termcolor.colored("\n"+num_text_ar[93]+"\n", 'blue'))
		# 4
	if (num_ar == 95):
		print(termcolor.colored("\n"+num_text_ar[94]+"\n", 'blue'))
		# 5
	if (num_ar == 96):
		print(termcolor.colored("\n"+num_text_ar[95]+"\n", 'blue'))
		# 6
	if (num_ar == 97):
		print(termcolor.colored("\n"+num_text_ar[96]+"\n", 'blue'))
		# 7
	if (num_ar == 98):
		print(termcolor.colored("\n"+num_text_ar[97]+"\n", 'blue'))
		# 8
	if (num_ar == 99):
		print(termcolor.colored("\n"+num_text_ar[98]+"\n", 'blue'))
		# 9
	if (num_ar == 100):
		print(termcolor.colored("\n"+num_text_ar[99]+"\n", 'blue'))
		# END


	

else:
	print(termcolor.colored(f'\nThis language [ {lang} ] is not suportted at the moment', 'red'))
