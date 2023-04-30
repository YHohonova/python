#Задание_2
class DivisionByNull(Exception):
    def __init__(self, txt):
        self.txt = txt

def divide_by_null(divider, denominator) :
    try:
        if denominator == 0:
            raise DivisionByNull('Делить на ноль нельзя')
        print(divider / denominator)
    except DivisionByNull as err:
        print(err)

divide_by_null(100, 0)