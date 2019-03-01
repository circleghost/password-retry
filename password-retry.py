password = 'a123456'
i = 0
while True:
	pas = input('請輸入密碼：')
	i = i + 1
	if pas == password:
		print('登入成功')
		break
	elif i >= 3:
		break
	else:
		print('密碼輸入錯誤！還有', 3 - i, '次機會')