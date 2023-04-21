#задание_1
li = [12, 8.0, True, [4, 7], (12, 'st'), 'hello', {'Olga' : 1234}]
for el in li :
     print(f'{el} имеет тип :{type(el)}')
#задание_2
ls = input('Enter list : '). split()
ls [: -1: 2], ls[1 :: 2] = ls[1 :: 2], ls[: -1 : 2]
print(ls)
#задание_4
st = input('Введите строку чеерз пробел :'). split()
for i, word in enumerate (st, 1) :
    print(i, word[: 10])
#задание_5
li = [7, 5, 3, 3, 2]
num = int(input('Введите число :')) #4
i = 0
for el in li :
    if num <= el :
        i += 1
li. insert(i, num)
print(li)
