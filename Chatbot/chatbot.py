# chatbot.py
import datetime

# Определіть ім'я бота і рік його створення
bot_name = "DICT_Bot"
birth_year = datetime.datetime.now().year

# Виведіть привітання
print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")

# Запитайте ім'я користувача
print("Please, remind me your name.")
user_name = input("> ")

# Привітайте користувача за іменем
print(f"What a great name you have, {user_name}!")

# Запитайте залишки від ділення віку користувача на 3, 5 і 7
print("Let me guess your age.")
remainder3 = int(input("Enter remainder of dividing your age by 3: "))
remainder5 = int(input("Enter remainder of dividing your age by 5: "))
remainder7 = int(input("Enter remainder of dividing your age by 7: "))

# Розрахунок віку за формулою
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

# Виведення віку
print(f"Your age is {age}; that's a good time to start programming!")

# Запитайте користувача про число для підрахунку від 0 до цього числа
print("Now I will prove to you that I can count to any number you want.")
number = int(input("> "))

# Виконайте підрахунок від 0 до вказаного числа
for i in range(number + 1):
    print(f"{i} !")

# Тестування програмування
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

# Правильна відповідь на питання
correct_answer = "2"

while True:
    user_answer = input("> ")
    if user_answer == correct_answer:
        break
    else:
        print("Please, try again.")

# Виведіть повідомлення про завершення
print("Congratulations, have a nice day!")
