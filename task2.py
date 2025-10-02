import math

a = float(input("Введіть нижню межу a: "))
b = float(input("Введіть верхню межу b: "))
h = float(input("Введіть крок h: "))

print("x" + " " * 8 + "|" + " " * 8 + "y")
print("-" * 25)

x = a
while x <= b:
    y = (math.cos(x) + 0.9) / (math.exp(x) + 0.33)
    print(f"{x:8.2f} | {y:8.4f}")
    x += h
