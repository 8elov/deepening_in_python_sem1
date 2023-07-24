# Напишите код,
# который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки:
# “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def is_prime(number):
    """The function tells whether the number is simple or composite"""
    if number == 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


while True:
    num = int(input("Введите число (от 1 до 100000): "))
    if num <= 0 or num > 100000:
        print("Введите число в диапазоне (от 1 до 100000).")
        continue
    break

result = is_prime(num)
if result:
    print(f"{num} - простое число.")
else:
    print(f"{num} - составное число.")
