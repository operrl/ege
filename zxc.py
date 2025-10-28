from math import *
from turtle import *
from random import *

#screensize(30000,30000)
#tracer(0)

f = open("27_B_21599.txt")

m = 50
eps = 1.5
data = []
clasters = []

for i in f:
    data.append(tuple(map(float, i.replace(',', '.').split())))  
print(len(data))

def dbscan(point, eps):
    claster = [] #какой то кластер для одной конкректной точки
    for i in data: # i = какая то точка
        if dist(point, i) < eps: #если дистанция меньше погрешности
            claster.append(i) #то мы добавляем его в какой то кластер для точки
    if len(claster) != 0: #если от точки есть кластер (т.е список кластер не пустой)
        for i in claster: #то мы смотрим точки которые у нас есть
            data.remove(i) #и удаляем их из даты(все точки)
        claster1 = [dbscan(i, eps) for i in claster] #смотрим какие кластеры у нас есть от тех точек что мы нашли
        claster += sum(claster1, []) #добавляем их в общий кластер 
    return claster

while data: #разбиение на кластеры
    clasterr = dbscan(data[0], eps) # создается какой то кластер из общей даты 
    clasters.append(clasterr) #добавляем его в список всех кластеров

def center(claster):
    center_point = []
    for point in claster:
        d = 0
        for point1 in claster:
            d += dist(point, point1)
        center_point.append((d, point))
    return min(center_point)[1]   

px = 0
py = 0

for claster in clasters:
    px += center(claster)[0]
    py += center(claster)[1]
    
'''for size in clasters:
    if len(size) == 1:
        for zopa in clasters:
           if len(zopa) == 32:
                zopa += size
                clasters.remove(size)'''

#penup() 

#for claster in clasters: #отрисовочка
#    rgb = (random(), random(), random())
#    for i in claster:
#        goto(i[0]*m, i[1]*m)
#        dot(10, rgb)

print(px/len(clasters)*10000, py/len(clasters)*10000)

#update()
#exitonclick()
