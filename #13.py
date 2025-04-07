#решение при помощи апиадресса 
from ipaddress import *

def ip_to_bin(ip): #функция перевода(в названии написано лол)
    res = ''
    ip = str(ip).split('.')
    for i in ip:
        res += bin(int(i))[2:].zfill(8)

    return res

net = ip_network('192.168.32.160/255.255.255.240', 0) #создает сеть, то есть какие могут быть адреса у устойств в этой сети

count = 0

for ip in net:
    if ip_to_bin(ip).count('1') % 2 == 0: 
        count += 1
        print(ip)
        print(ip_to_bin(ip))

print(count)
