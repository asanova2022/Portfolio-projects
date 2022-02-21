# Исправление "i = 1"
i = 1
while i < 3:
    print(i)
    i = i+1
print("")

# Исправление ":" и "=="
a = 22
b = 22

if a == b:
    print("Переменные равны")
else:
    print("Переменные не равны")
    
if a == b:
    print("Переменные равны")
else:
    print("Переменные не равны")
print("")

# Исправление "F"
is_sql_connection = False

if is_sql_connection:
    print("Есть соединение")
else:
    print("Соединение отсутствует")
print("")

# Исправление "="
summ = 0
for i in range(5): #0, 1, 2, 3, 4 
    summ += i
    
print(summ)
print("")

# Исправление "%"
def function_2(a):
    if a%2 == 0:
        print("Четное число")
    else:
        print("Нечетное число")

function_2(9)
function_2(10)

