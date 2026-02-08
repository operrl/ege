from re import *
f = open("24_21908.txt").read()

reg = r'[1-9ABCD][0-9ABCD]+'

max_len = 0
for i in finditer(reg, f): #нашли число какое то большое
    num = i.group() #делаем из него строку
    string = '' #делаем строку
    for k in num: #
        if k != '0':
            string += k
        if k == '0':
            string += k
            if int(string, 14) % 2 == 0 and len(string) > max_len:
                max_len = len(string)
            string = '' 
    if int(num, 14) % 2 == 0 and len(num) > max_len:
        max_len = len(num)


print(max_len)

#49987099860548
