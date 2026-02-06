#Ejercicio 1

first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

for index in range(0, len(first_list)):
    print(f'{first_list[index]} {second_list[index]}')
print("")

#Ejercicio 2

goal_method = "SMART"
for char in goal_method:
    if char == "S":
        print(f"{char}-pecific")
    elif char == "M":
        print(f"{char}-easurable")
    elif char == "A":
        print(f"{char}-chievable")
    elif char == "R":
        print(f"{char}-elevant")
    elif char == "T":
        print(f"{char}-ime-bound")
    
#Ejercicio 3
list_of_cities = [
    'New York', 
    'Los Angeles',
    'Chicago',
    'Houston',
    'San Diego',
    'Phoenix',
    'Philadelphia',
    'San Antonio',
    'Dallas',
    'San Jose',
    'Austin',
    'Jacksonville',
    'Fort Worth',
    ]

fist_city = list_of_cities.pop(0)
last_city = list_of_cities.pop(-1)

list_of_cities.insert(0, last_city)
list_of_cities.append(fist_city)

print(list_of_cities)
print("")

#Ejercicio 4
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

non_even_number = 0
for index, number in enumerate(numbers_list):
    if number % 2 != 0:
        non_even_number = index
    numbers_list.pop(non_even_number)
print(numbers_list) 
print("")

#Ejercicio 5
user_numbers_list = []
user_number = 0
limit_numers = 10
counter = 1
highest_number = 0

while counter <= limit_numers:
    user_numbers_list.append(user_number)
    user_number = int(input(f"Dame un numero entero ({counter}/10): "))
    if user_number > highest_number:
        highest_number = user_number
    counter += 1

print(f"{user_numbers_list}. El numero mas alto es: {highest_number}")

