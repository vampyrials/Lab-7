numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

sum_negative = 0
for num in numbers:
    if num < 0:
        sum_negative += num

print("Сума від’ємних елементів:", sum_negative)
