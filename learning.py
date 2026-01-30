# Программа принимает на вход натуральное число N. 
# Ваша задача: вывести на экране все числа от N до 1 
# в сторону уменьшения, каждое число в отдельной строке

# stroka = "Программа принимает на вход натуральное число N."

# counter = 0
# for probel in stroka:
#     if probel == ' ':
#         counter += 1
# print(counter)

# number = 0

# while number < 11:
#     print(number)
#     number +=1


# def spisok_fruit(list):
#     for item in list:
#         print(item)


# spisok = ['apple', 'pineapple', 'orange']
# spisok_fruit(spisok)


# def spisok_nbnum(x,y):
#     if x > y:
#         return print(x)
#     else:
#         return print(y)

# x = 5
# y = 7
# spisok_nbnum(x,y)

# x = 10

# def add_to_x(y):
#     x = 5
#     x = x + y
#     print(f'x внутри функции: {x}')


# add_to_x(3)

# print(f'x за пределами функции {x}')


# n = int(input("введите число: "))
# # result = n % 2 == 0
# # print("Число четное: ", result)


# if n % 2 == 0:
#     print("Число четное: ", n)


# def make_adder(n):
#     return lambda x: x + n


# plus_3 = make_adder(3)
# plus_5 = make_adder(4)
# print(plus_3(5))
# print(plus_5(10))

# def fruits(*args):
#     for fruit in args:
#         print(fruit)


# s = fruits('apple', 'pineapple', 'orange')
# # s = fruits(spisok)
# print(s)

# def mango(**kwargs):
#     for key, value in kwargs.items():
#         print("{0}: {1}".format(key, value))

# m = mango(name = 'mango', color = 'grenn and red')
# print(m)


# # Определяем полезную функцию
# def greet(name):
#     return f"Привет, {name}!"

# # Этот блок кода выполнится, только если запустить файл напрямую
# if __name__ == "__main__":
#     print("--- Запуск напрямую как основная программа ---")
#     message = greet("Пользователь")
#     print(message)
#     print("---------------------------------------------")
# else:
#     print(f"--- Скрипт '{__name__}' был импортирован ---")
#     # Этот код не выполнится, если его импортировать


# def new_func(name):
#     return f"Hello, {name}!"


# if __name__ == "__main__":
#     print("---Запуск кода---")
#     message = new_func('World')
#     print(message)


# def lus(a, b):
#     return a + b


# __name__ == "__main__"
# sum = lus(5,3)
# print(sum)


# def square(x, y):
#     return x * y


# __name__ == "__main__"
# x = 5
# y = 4
# result = square(x,y)
# print(result)

# def calculate_stats(a, b):
#     return a + b, a - b

# __name__ == "__main__"
# sum_result, diff_result = calculate_stats(10, 5)
# print(sum_result, diff_result)


# def greet(name="Guest"):
#     print("Hello", name)

# greet()
# greet("Syed")

# def user_info(name, age):
#     print(name, age)

# user_info("Syed", 25)
# user_info(age=100, name="Mike")

# def add_numbers(*numbers):
#     return sum(numbers)

# k = add_numbers(1,2,3,4)
# print(k)

# add = lambda a, b: a + b
# s = add(4, 7)
# print(s)

# x = 1
# def add(a, b):
#     global x
#     return a + b + x

# s = add(4, 7)
# print(s)


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner      # Владелец счета
        self.balance = balance  # Текущий баланс

    # Метод для пополнения счета
    def deposit(self, amount):
        if amount > 0:
            self.balance +=amount
            print(f"Счет пополнен на {amount}. Новый баланс: {self.balance}")
        else:
            print("Сумма пополнения должна быть больше нуля!")
    
    # Метод для просмотра инфо
    def show_info(self):
        print(f"Владелец: {self.owner}, Баланс: {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Недостаточно средств!")
        else:
            self.balance -= amount
            print(f"Деньги сняты на сумму {amount}. Новый баланс: {self.balance}")

    def transfer(self, other_account, amount):
        commission = amount * 0.05
        total_deduction = amount + commission
        if amount <= 0:
            print("Сумма перевода должна быть положительной!")
        elif self.balance < total_deduction:
            print(f"Недостаточно средств! Нужно {total_deduction}, а у вас {self.balance}")
        else:
            self.balance -= total_deduction
            other_account.balance += amount
            print(f"Перевод {amount} успешно выполнен для {other_account.owner}. Комиссия составила {commission}")
            print(f"Ваш остаток: {self.balance}")

class GoldAccount(BankAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)

        bonus = 100
        self.balance += bonus
        print(f"Поздравляем, {self.owner}! Вам начислен Gold-бонус: {bonus}")
        
    # Мы можем переопределить метод transfer специально для Gold-клиентов
    def transfer(self, other_account, amount):
        if amount <= 0:
            print("Сумма должна быть больше нуля")
        elif self.balance < amount:
            print("Недостаточно средств!")
        else:
            # У Gold-клиентов нет комиссии!
            self.balance -= amount
            other_account.balance += amount
            print(f"VIP-перевод на {amount} без комиссии!")
            print(f"Ваш остаток: {self.balance}")
    
    def get_cashback(self):
        bonus = self.balance * 0.01
        self.balance += bonus
        print(f"Начислен кэшбэк 1%: {bonus}. Новый баланс: {self.balance}")

# 1.Создание счета для Ивана с начальной суммой 1000
my_account = BankAccount("Иван", 1000)

# 2. Проверяем данные
my_account.show_info()

# 3. Проверяем баланс
my_account.deposit(500)
my_account.deposit(500)
my_account.withdraw(100)

# 1. Создаем двух разных людей
ivan = BankAccount("Иван", 1000)
anna = BankAccount("Анна", 500)
ruslan = GoldAccount("Руслан", 1000)

# 2. Иван переводит  Анне 300 рублей
ivan.transfer(anna, 300)
ivan.transfer(ruslan, 100)

ruslan.get_cashback()

# 3. Проверяем результаты
print("---Итог---")
ivan.show_info()
anna.show_info()
ruslan.show_info()