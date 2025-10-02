# Створюємо список з N перших чисел, кратних 22
N = int(input("Введіть N: "))
numbers = [22 * i for i in range(1, N + 1)]

print("Початковий список:", numbers)

# Беремо останні 3 елементи
last_three = numbers[-3:] if len(numbers) >= 3 else numbers

print("Останні 3 елементи:", last_three)
