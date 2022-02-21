print("Hello World!")
print("")
print("")

# Простой цикл while
i = 10
while i<=20:
    print(i, end=' ')
    i += 1
print("")
print("")


# Печать только чисел, делящихся на 3, с использованием continue
for i in range(13): # 0, 1, 2, 3 ... 12
    if i%3 != 0:
        continue
    print(i, end=' ')
print("")
print("")

# Печать первого элемента, меньшего 1, с использованием break
numbers = [1, 7, 11, 0, 23, 8, 5]
for number in numbers:
    if number < 1:
        print(number)
        break
print("")

# Печатаем, если элемент не найден, при помощи else
numbers = [1, 7, 11, 23, 8, 5]
for number in numbers:
    if number < 1:
        print(number)
        break
else:
    print("Элемент не найден")    

