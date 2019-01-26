# Основы языка Python. Домашнее задание 1

# Сложность: Easy
# Задача 1
perem_celoe = int(float(input('Введите целое число: ', )))
perem_drob = float(input("Введите дробное число: ", ))
perem_strok = input("Введите слово: ", )
print('Целое число: ', perem_celoe, type(perem_celoe))
print("Дробное число: ", perem_drob, type(perem_drob))
print('Слово: ', perem_strok, type(perem_strok))
print()
print()

# Задача 2
perem = float(input("Введите число: ", ))
print('Прибавим 2, получим: ', perem + 2)
print()
print()

# Задача 3
vozrast = float(input("Введите ваш возраст: ", ))
if vozrast > 18:
    print('Доступ разрешен.')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')
print()
print()

# Сложность: Medium
# Задача 1
chislo = int(input("Введите целое число большее нуля и меньшее 10: ", ))
while chislo <= 0 or chislo >= 10:
    chislo = int(input("Введено неверное число. Введите целое число большее нуля и меньшее 10: ", ))
print("Ваше число в квадрате равно: ", chislo ** 2)
print()
print()

#Задача 2
a = int(input('Введите число а: ', ))
b = int(input('Введите число b: ', ))
print("Меняем значения а и b местами")
print("Теперь а =",a+b-a)
print("Теперь b =",a+b-b)
print()
print()

# Сложность: Hard

print("Добро пожаловать в медицинскую программу!")
name = input("Введите ваше имя: ", )
surname = input("Введите вашу фамилию: ", )
vozrast = int(input("Введите ваш возраст, полных лет: ", ))
ves = float(input("Введите ваш вес, кг: ", ))
if vozrast > 0 and vozrast <= 30 and ves >= 50 and ves <= 120:
    print("{} {}, ".format(name.title(), surname.title()), vozrast, 'лет, вес ', ves, 'кг - хорошее состояние.')
elif vozrast > 30 and vozrast <= 40 and (ves < 50 or ves > 120):
    print("{} {}, ".format(name.title(), surname.title()), vozrast, 'лет, вес ', ves, 'кг - следует заняться собой.')
elif vozrast > 40 and ves >= 50 and ves <= 120:
    print("{} {}, ".format(name.title(), surname.title()), vozrast, 'лет, вес ', ves, 'кг - следует заняться собой.')
elif vozrast > 40 and (ves < 50 or ves > 120):
    print("{} {}, ".format(name.title(), surname.title()), vozrast, 'лет, вес ', ves, 'кг - следует обратиться к врачу!')
elif vozrast <= 0 or ves <= 0:
    print('Тебя не существует')
else:
    print("Необходимы дополнительные данные, купите платную версию")

print('Я добавил этот код в репозиторий на Github')
print('Я добавил еще код в репозиторий на Github')

