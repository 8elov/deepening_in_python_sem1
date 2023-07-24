# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for i in range(2, 11):
    print(" ")

    for j in range(2, 6):
        result = i * j
        if 1 <= result <= 9 and i != 10:
            print(f"{j} x {i} =   {result}", end="    ")
        elif 10 <= result <= 99 and i != 10:
            print(f"{j} x {i} =  {result}", end="    ")
        elif i == 10:
            print(f"{j} x {i} = {result}", end="    ")

print()

for i in range(2, 11):
    print(" ")

    for j in range(6, 10):
        result = i * j
        if 1 <= result <= 9 and i != 10:
            print(f"{j} x {i} =   {result}", end="    ")
        elif 10 <= result <= 99 and i != 10:
            print(f"{j} x {i} =  {result}", end="    ")
        elif i == 10:
            print(f"{j} x {i} = {result}", end="    ")
