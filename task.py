#Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.

import random
k = 5
sp = []
for i in range(k):
    sp.append(random.randint(1,k))
print (sp)
sort_sp=sorted(sp)
print (sort_sp)
#--------------------------------------------------------------------------------------------------
#Найти НОК двух чисел


number_1=int (input())
number_2=int (input())
def multiplier_number(number_1,number_2):
    for i in  range(number_1*number_2):
        i+=1
        if (i%number_1 == 0) and(i%number_2==0) :
            break
    return i
print(multiplier_number(number_1,number_2))
#-----------------------------------------------------------------------------------------------------------
#Вычислить число Пи c заданной точностью d
#Пример: при d = 0.001,  c= 3.141.
#C= π*d = 2*π*r.
d=0.001
c=3.141
pi=round(c,2)
print(pi)
#-----------------------------------------------------------------------------------
#Составить список простых множителей натурального числа N
number=int (input())
multiplier_list = []

i = 2
while i < number:
    while number % i == 0:
        multiplier_list.append(i)
        number //= i
    i  += 1
if number > 1:
    multiplier_list.append(number)
print(multiplier_list)
#-------------------------------------------------------------------------------------
#5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 
with open ('file.txt','w') as data:
    list = ['23','27','1','78','5','4','43','12','3']
    data = open('file.txt','w')
    data.writelines(list)
    data.close()
    path='file.txt'
    data = open(path,'r')
    for line in data:
        print(line)
data.close()
i=0
while i <len(list):
    if int(list[i])%2==0:
     list.remove(list[i])
    i+=1
print (list)
