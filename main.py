# all_sec = 5000
# hours = all_sec // 3600
# print(hours)
# minutes = (all_sec - hours * 3600)//60
# print(minutes)
# seconds = (all_sec - (hours * 3600) - (minutes*60))
# print(seconds)
# print(f"{all_sec} секунд, це {hours} година, {minutes} хвилини та {seconds} секунд.")
# print(f"годин: {hours}, хвилин: {minutes} секунд:{seconds}")
# print(type(seconds))
# print(f"години менше секунд: {bool(hours < seconds)}")
# printa = 1
# print(f"змінна printa {bool(printa)}")
# age1 = 18
# age2 = 20
# print(f"{age1} більше {age2}: {bool({age1} > {age2})}")
# a = float(input("Введіть сторону квадрата a: "))
# p = a * 4
# print(f"Периметр квадрата: {p}")
# a = 15.0
# b = 2
# print(a//b)
# my_list = list()
# my_list = ["Natali",2,3]
# print(f"початковий список індекс 2 або -1: {my_list[-1]}")
# my_list.append(5)
# print(f"список з додаванням елементу в кінець: {my_list}")
# my_list[-1] = 6
# print(f"список зі зміною елементу 3 чи -1: {my_list}")
# print(f"видалення 0: {my_list.pop(0)}")
# print(f"видалення 0 список : {my_list}")
# my_list_2 = ["Nata", "Lebed"]
# my_list.extend(my_list_2)
# print(f"список після розширення списку: {my_list}")
# my_list.insert(0, 1)
# print(f"список після вставлення елементу '1' на 0 позицію: {my_list}")
# # my_list.clear()
# # print(f"список очищений: {my_list}")
# print(f"індекс '3': {my_list.index(3)}")
# print((f"кількість '2': {my_list.count(2)}"))

# print(f"довжина списку: {len(my_list)}")
# while True:
#     user_input = input()
#     print(user_input)
#     if user_input == "0":
#         break
# a = 0
# while a < 6:
#     a = a + 1
#     if a % 2:
#         continue
#     print(a)

# for i in range(1, 10):
#     if i % 2 == 0:
#         print(f'{i} є парним числом.')
#     else:
#         print(f'{i} є непарним числом.')

# while True:
#     number = input("number = ")
#     number = int(number)
#     while True:
#         print(number)
#         number = number - 1
#         if number < 0:
#             break


# is_next = None
# num = int(input("Enter the number of points: "))
# if num >= 83:
#     is_next = True
#     print("кандидат проходить до наступного туру")
# else:
#     is_next = False
#     print("кандидат не проходить до наступного туру")


# work_experience = int(input("Enter your full work experience in years: "))

# if work_experience > 1 and work_experience <= 5:
#     developer_type = "Middle"
# elif work_experience <= 1:
#     developer_type = "Junior"
# else:
#     developer_type = "Senior"
# print(f"Категорія розробника {developer_type}")


# num = int(input("Enter a number: "))

# if num > 0:
#     if num % 2 == 1:
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"
# print(result)

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# while num >= 1:
#     sum += num
#     num = num - 1
# print(sum)

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for char in message:
#     if char == search:
#         result += 1
# print(result)


# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = int(pool / quantity)
# except ZeroDivisionError:
#     print('Divide by zero completed!')
# else:
#     print(f"розмір пакету SMS для розсилки {chunk}")

# def greeting():
#     print("Hello world!")
# greeting()

# username = input("Enter your name: ")
# def invite_to_event(username):
#     return(f"Dear {username}, we have the honour to invite you to our event")
# invite_to_event(username)
# print(f"Dear {username}, we have the honour to invite you to our event")

# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal
#         price * (1 - discount)    
#     apply_discount()
#     return(apply_discount)

# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#     # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник  
#             codes[ch] = ord(ch)  
#     return codes

# result = string_to_codes("Hello world!")
# print(result)
        
# result1 = string_to_codes("Natali") # букву а додає в словник один раз, дублі видаляє
# print(result1)

# def discount_price(price, discount):
    
#     def apply_discount():
#         nonlocal price
#         price = price * (1 - discount)
#     apply_discount()
           
#     return price


# def multiply(numbers_one, number_two, number_three=None):
#     print(number_three, end=' ')
#     if number_three is None:
#         return numbers_one * number_two
#     else:
#         return numbers_one * number_two * number_three


# print(multiply(2, 3))
# print(multiply(2, 3, 5))

# def get_fullname(first_name, last_name, middle_name):
#     if middle_name == None:
#         return f"{first_name} {last_name}"
#     else:
#         return f"{first_name} {middle_name} {last_name}"
    
# def get_fullname(first_name, middle_name, last_name):
#     if (len(middle_name)) == 0:
#         return f'{first_name} {last_name}'
#     else:
#         return f'{first_name} {middle_name} {last_name}'

# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     else:
#         total_spaces = length - len(string)
#         space_left = total_spaces // 2
#         space_right = total_spaces - space_left
#         return " " * space_left + string   

# def first(size, *args):
#     return size + len(args)

# def second(size, **kwargs):
#     return size + len(kwargs)

# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)


# def number_of_groups(n, k):
    
#     return factorial(n) // (factorial(n-k) * factorial(k))  

# def factorial(n):
#     if n == 0: # базовий випадок
#         return 1
#     else:
#         return n * factorial(n-1) # рекурсивний випадок

# print(factorial(5)) # виведе 120

# def fibonacci(n):
#     if n <= 1: # базовий випадок
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок

# print(fibonacci(10)) # виведе 55


# def say_hello():
# 		# тіло функції
#     print(f'Привіт, {name}!')
#     print(f'Привіт, my {name1}!')

# # Кінець функції say_hello()

# # виклик функції
# name = input("Введіть ім'я: ")
# name1 = input("Як вас звати: ")
# say_hello()

# def add_numbers(num1: int, num2: int) -> int:
#     sum = num1 + num2
#     return sum

# result = add_numbers(5, 10)
# print(result)  # Виведе: 15

# def is_even(num: int) -> bool:
#     return num % 2 == 0

# check_even = is_even(5)
# print(check_even)  # Виведе: True

# def print_all_args(*args):
#     for arg in args:
#         print(arg)

# print_all_args(1, 'hello', True)

# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ": ", result)
#         return result

# print(factorial(5))


# text = "First sentence. Second sentence. Third sentence."
# sentensces = text.split(". ")
# print(sentensces)

# import re
# text = "First sentence. Second sentence! Third sentence?"
# sentensces = re.split("[.!?]", text)
# print(sentensces)


# import re
# text = "First sentence.\nSecond sentence!\nThird sentence?"
# # sentensces = re.split("[.!?]", text)
# print(text)
# sentensces = text.split("\n")
# print(sentensces)
# text_new = " ".join(sentensces)
# print(text_new)


# numbers = [1, 2, 3, 4, 5]
# header = '|{:^15}|{:^15}|{:^15}|'.format('int', 'int^2','int^3')
# separator = '-'*len(header)
# body = ''
# for num in numbers:
#     body +='|{:^15}|{:^15}|{:^15}|\n'.format(num, num**2, num**3)    
# print(separator, header, separator, body, separator, sep='\n')

# trans_map = {ord('Н'):'N', ord('п'):'h'}
# ukr_name = 'Наташа привіт'
# lat_name = ukr_name.translate(trans_map)
# print(lat_name)

# text = 'Hello world'
# indx = text.find('world')
# print(indx)

from datetime import datetime 
def get_days():
    user_input = input('Введіть дату в форматі dd.mm: ')
    user_date = datetime.strptime(user_input, '%d.%m')
    print(user_input, type(user_input))
    print(user_date, type(user_date))
    current_day = datetime.now()
    print(current_day)
    user_date = user_date.replace(year=current_day.year)
    print(user_date)
    delta_days = user_date - current_day
    target_date = datetime.strftime(user_date, '%d-%B-%Y')
    
    if delta_days.days > 0:
        print(f'{delta_days.days} days left before {target_date}')
    else:
        user_date = user_date.replace(year=user_date.year + 1)
        delta_days = user_date - current_day
        target_date = datetime.strftime(user_date, '%d-%B-%Y')
        print(f'{delta_days.days} days left before {target_date}')
get_days()
