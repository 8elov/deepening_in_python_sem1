#  1.Треугольник существует только тогда,
# когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

def is_triangle(a, b, c):
    """The function prints whether the triangle exists or not"""
    if (side_a >= side_b + side_c
            or side_b >= side_a + side_c
            or side_c >= side_a + side_b):
        print("Треугольник с данными сторонами не существует")
    else:
        print("Треугольник с данными сторонами существует")


def triangle_type(a, b, c):
    """The function prints the type of triangle"""
    if side_a == side_b == side_c:
        print("Равносторонний треугольник")
    elif side_a == side_b or side_b == side_c or side_a == side_c:
        print("Равнобедренный треугольник")
    else:
        print("Разносторонний треугольник")


side_a = int(input("Введите длину стороны a: "))
side_b = int(input("Введите длину стороны b: "))
side_c = int(input("Введите длину стороны c: "))

is_triangle(side_a, side_b, side_c)
triangle_type(side_a, side_b, side_c)
