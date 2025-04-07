from itertools import *
count = 0 
for i in permutations('01234567'): #вместо пермутатионс если факториал, продукт если в степени
    if i[0] != '0': #сюда любое условие
        for l in range(1, len(i) - 1):
            if int(i[l]) % 2 == int(i[l - 1]) % 2: #доп.условие(не всегда есть)
                break
        else:
            count += 1

print(count)
