sum = 0 #функция суммирования
while 0 < 1: #проверяемое условие
    number = int(input("Введите число: ")) #ввод чисел
    if number != 0: #если число не равно нулю
        sum += number #то суммируются введённые числа
    else:
      break #и цикл останавливается
print("Сумма чисел:", sum)