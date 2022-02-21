print("Hello World!")

do_print = True
do_print = False

if do_print:
    print("Условие выполнено")
    
print("После условия")
print("")

is_sql_connection = True
is_sql_connection = False

if is_sql_connection:
    print("Есть соединение")
else:
    print("Соединение отсутствует")
    
print("")

a = 3
b = 7

if a == b:
    print("Переменные равны")
elif a > b:
    print("а больше b")
elif a < b:
    print("a меньше b")
else:
    print("Не должно быть напечатано")
    
print("")

if b%3 == 0:
    print("b делится на 3")
else:
    print("b не делится на 3")
    
print("")

a = False
b = False
b = True

if a and b:
    print("a и b")
elif a or b:
    print("Один из a или b")
else:
    print("Ничего")

