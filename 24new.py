from re import *

f = open("24_24895.txt").read()

num = r"([1-9][0-9]*)+([+=][1-9][0-9]+){39}"
mx = 0
for i in finditer(rf"(?=({num}))", f):
    pass