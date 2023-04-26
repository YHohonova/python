#задание_1
def div(s1, s2):
  try:
      s1, s2 = int(s1), int(s2)
      res = s1 / s2
  except ValueError :
      return 'Not a number'
  except ZeroDivisionError :
      return 'Can`t divide by zero'
  return res
a = input('Num 1: ')
b = input('Num 2: ')
print(div(a, b))
#задание_2
def info (name, surn, birth, city, email, tel):
    return f'Name: {name}, Surname: {surn}, Birthday: {birth}, City: {city}, Email: {email}, Telephone: {tel}'
print(info(name = input('Name :'), surn = input('Surname:'), birth = input('birthday:'), city = input('City:'), email = input('email:'), tel = input('telephone:')))
#задание_3
def exc_min(a, b, c):
    li = [a, b, c]
    try:
        li.remove(min(li))
        return sum (li)
    except TypeError :
        return 'Not a number'
print(exc_min(9, 12, 3))
#задание_4
def my_func(x, y):
    try:
        res = x**y
        return res
    except TypeError :
        return'Not a number'
print(my_func(5, -1))
#задание_5
def summ():
    res = 0
    while True:
        li = input('Введите числа через пробел, для выхода - stop').split()
        for num in li:
            if num.lower() == 'stop' :
                return res
            else:
                try:
                    res += int(num)
                except ValueError :
                    return'Для выхода - stop'
        print('Summa = ', res)
print(summ())
