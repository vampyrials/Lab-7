
cat > task1.py << 'EOF'
import math

a = float(input("Введіть нижню межу a: "))
b = float(input("Введіть верхню межу b: "))
h = float(input("Введіть крок h: "))

print("x" + " " * 8 + "|" + " " * 8 + "y")
print("-" * 25)

x = a
while x <= b:
    y = math.tan(x) + 1 / math.sqrt(x**2 + 1) - 4**0.1 * x
    print(f"{x:8.2f} | {y:8.4f}")
    x += h
