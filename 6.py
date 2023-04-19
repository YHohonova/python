first_day = int(input('Введите результат в км. в первый день тренировок:'))
targ_res = int(input('Введите целевой результат в км.:'))
day_num = 1
while first_day < targ_res :
    day_num += 1
    first_day *= 1.1
    print(first_day)
print(f'Ответ: на{day_num}-й день спортсмен достиг результата- не менее {targ_res}км')