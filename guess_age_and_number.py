# Програма яка відгадує цифру, яку ви загадали та Вашу кількість років

# Підключаємо наступні необхідні змінні для Colorama (змінює колір тексту та фону)
from colorama import init
from colorama import Fore, Back, Style
init()


print( Fore.CYAN )      # Змінюємо колір літер за допомогою Colorama
print("\n\n\t\t\t\t***Добро Пожаловать***\n\tСейчас я попытаюсь угадать Ваш возраст а также число, которые Вы загадаетеn\n\n")

#number = int(input("Загадайте, пожалуйста, число от 1 до 9: "))                # Вводимо число

# Перевірка на корректність вибору числа (число в межах від 1 до 9)
is_True = True
while is_True:
        print( Back.YELLOW, Fore.BLACK )        # Змінюємо колір літер та фону за допомогою Colorama
        number = int(input( "1) Загадайте, пожалуйста, число от 1 до 9: " ))
        if number <= 0 or number > 9:
                print( Back.RESET , Fore.RED )  # Скидуємо колір фону та встановлюємо колір літер
                print("\t !!! Вы введли не корректную цифру. Попробуйте, пожалуйста, еще раз")
        else:
                is_True = False

# Перший розрахунок:
first_result = ((number * 2) + 5) * 50
#print("first_result: ", first_result)


'''
Функція яка приймає параметром перший розрахунок, 
та в залежності від того, чи було цього року у Вас 
день народження проводить наступні розрахунки
Та повертає результат цих обрахунків
'''
def This_Year(first):
        is_Year = True
        while is_Year:
                print( Back.YELLOW, Fore.BLACK )
                this_year = input("2) У Вас было день рождения в этом году? (да / нет) ")

                if this_year ==  "да" or this_year == "ДА" or this_year == "Да":
                        first += 1770
                        is_Year = False
                elif this_year == "нет" or this_year == "НЕТ" or this_year == "Нет":
                        first += 1769
                        is_Year = False
                else:
                        print( Back.RESET , Fore.RED )
                        print("\t !!! Некорректный ответ, попробуйте снова.")
        return first

'''Викликаэмо дану функцію, в якості агрументу 
перший розрахунок, результат записуємо в змінную second_result
'''
second_result = This_Year(first_result)

#print("Після перевірки на день народження: ", second_result)


'''Функція, яка запитує Ваш рік народження, 
та в разулжності від відповіді проводить розрахунки.
'''
def Your_Birth_Year(second):
        is_Birth = True
        while is_Birth:
                print( Back.YELLOW, Fore.BLACK )
                birth_year = int(input("3) В каком году Вы родились? "))

                if birth_year >= 1920 and birth_year <= 2020:
                        second -= birth_year
                        is_Birth = False
                else:
                        print( Back.RESET , Fore.RED )
                        print("\t !!! Некорректный ответ, попробуйте снова.")
        return second


final_result = str(Your_Birth_Year(second_result))

print( Back.RESET , Fore.MAGENTA )
print("\n\n\t******Ваш результат: ****** ")
print("\nВаш возраст:  ",final_result[1], final_result[2], sep = "")
print("Ваше число: ", final_result[0], end = "\n\n")

input()
#print("\n>>>Первая цифра - это число, которые Вы загадали; \n>>>Последующие цифры - это количество Ваших лет\n\n")