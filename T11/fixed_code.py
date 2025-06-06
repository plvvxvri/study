# Задача 1: Отладка функции расчёта факториала
def factorial(n):
    result = 1
    for i in range(1, n + 1):  # Исправлено: до n включительно
        result *= i
    return result

print(factorial(5))  # Теперь выводит 120


# Задача 2: Работа с условиями
def check_password(password):
    if len(password) < 8:
        return "Слишком короткий!"
    elif not any(char.isdigit() for char in password):
        return "Нет цифр!"
    else:
        return "Пароль надёжен!"

print(check_password("qwerty"))  # Теперь корректно возвращает "Слишком короткий!"


# Задача 3: Работа с логикой
def calculate_sum(arr):
    total = 0
    for i in range(len(arr)):  # Исправлено: убран выход за границы
        total += arr[i]
    return total

numbers = [10, 20, 30]
print(calculate_sum(numbers))  # Теперь выводит 60
