country = input('請輸入你的國家:')
age = int(input('請輸入你的年齡:'))
if country =='台灣':
	if age >= 18:
		print('可以考駕照')
	else:
		print('還不可以考駕照')