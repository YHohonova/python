#Задание_3
class MyOwnExc(Exception):
    def __init__(self, txt):
        self.txt = txt

num_lst = []
while True:
    try:
        elem = input('Введите число или stop для завершения: ')
        if elem =='stop':
            break
        elif elem.isdigit():
            num_lst.append(int(elem))
        else:
            raise MyOwnExc('Вы ввели не число, повторите ввод')
    except MyOwnExc as e:
        print(e.txt)

print(num_lst )        