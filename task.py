#Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
#Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя
list = [1, 5, 2, 3, 4, 6, 1, 7]
print (f'{list}\n')
sort=sorted(list)
print (f'{sort}\n')
list_2 = str(sort[:6])
print(list_2)
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
