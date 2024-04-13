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

    


