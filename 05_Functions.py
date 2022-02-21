
# Простая функция
def simple_function():
    print("Печать из функции")
    
print("Печать до вызова функции")
simple_function()
print("Печать после вызова функции")

print("")

# Функция печати элементов списка, делящихся на 5
def function_list_2(numbers):
    for number in numbers:
        if number%5 !=0:
            continue
        print(number, end=' ')
    print("")
    
numbers1 = [5, 7, 11, 15, 21]
numbers2 = [3, 55, 8, 37, 46]

function_list_2(numbers1)
function_list_2(numbers2)

print("")

# Функция простого поиска и возвращения минимального элемента в списке

def get_min_simple(numbers):
    m = numbers[0]
    for number in numbers:
        if number < m:
           m = number
    return m
    
numbers1 = [5, 7, 11, 15, 21]
numbers2 = [9, 55, 3, 37, 46]

my_min = get_min_simple(numbers1)
print(my_min)
my_min = get_min_simple(numbers2)
print(my_min)

print("")

# Функция поиска в списке первого элемента, меньшего my_value
def get_first_exceed(numbers, my_values):
    for number in numbers:
        if number < my_values:
           print(number)
           break
           
numbers1 = [5, 7, 11, 15, 21]
numbers2 = [100, 55, 3, 37, 46]

get_first_exceed(numbers1, 20)
get_first_exceed(numbers2, 50)
   
   
   
   
   
   
   
           
           







        
