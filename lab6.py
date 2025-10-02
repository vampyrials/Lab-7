import math

# Завдання 1
def convert_length(meters):
    print("Сантиметри:", meters * 100)
    print("Дециметри:", meters * 10)
    print("Міліметри:", meters * 1000)
    return meters  # залишимо return щоб було

# Завдання 2
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# Виклики
m = float(input("Введіть довжину в метрах: "))
convert_length(m)

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

print("Відстань:", distance(x1, y1, x2, y2))
