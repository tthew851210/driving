country = input('請輸入國籍')
age = input('請輸入年齡')
age = int(age)
if country == '台灣':
    if age >= 18:
        print('你可以開車')
    else: 
        print('你不能開車')
