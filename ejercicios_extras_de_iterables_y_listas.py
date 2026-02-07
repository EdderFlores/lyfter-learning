#Ejercicio 1

user_number_list = []
user_number = 0 
numbers_to_add = int(input("¿Cuántos números desea agregar a la lista? "))
counter = 1
while counter <= numbers_to_add:
    user_number = int(input(f"Ingrese el número {counter}: "))
    user_number_list.append(user_number)
    counter += 1
number_to_search = int(input("Ahora,que número te gustaria buscar en la lista: "))

if number_to_search in user_number_list:
    print(f"El número {number_to_search} aparece {user_number_list.count(number_to_search)} veces en la lista.")
else:
    print(f"El número {number_to_search} no se encuentra en la lista.")
print("")
print("*********************************")
print("")

#Ejercicio 2

numbers_list = [3, 5, 6, 6, 9, 0, 4, -12, 45, -1, -0.5, -56, 34, 23, 12, 11, -3]
negative_count = 0
for number in numbers_list:
    if number < 0:
        negative_count += 1
if negative_count <= 1:
    if negative_count == 0:
        print(f"No hay números negativos en la lista.")
    print(f"Hay {negative_count} número negativo en la lista.")
else:
    print(f"Hay al menos {negative_count} números negativos en la lista.")
    
print("")
print("*********************************")
print("")
#Ejercicio 3

my_numbers_list = [1, 2, 3, 4, 5, -1, 120, 0, 3, 4, 5, 6, 7, 8, 9]
smallest_number = 100

for number in my_numbers_list:
    if smallest_number > number:
        smallest_number = number

print(f"El menor valor es {smallest_number}")
print("")
print("*********************************")
print("")
#Ejercicio 4

grade_list = []
total_grades = 0
average = 0
higher_average_numbers = []
grades_to_add = int(input("¿Cuántas notas desea agregar a la lista? "))
counter = 1

while counter <= grades_to_add:
    grade = float(input(f"Ingrese la nota {counter}: "))
    grade_list.append(grade)
    counter += 1

total_grades = sum(grade_list)
average = total_grades / len(grade_list)

for higher_average in grade_list:
    if higher_average > average:
        higher_average_numbers.append(higher_average)

print(f"Promedio: {average}")
print(f"Notas Superiores a Promedio: {higher_average_numbers}")
print("")
print("*********************************")
print("")
#Ejercicio 5

user_words_list = []
words_to_add = 5
counter = 1
limit_characters = 4
more_than_limit_characters = []

while counter <= words_to_add:
    word = input(f"Ingrese la palabra {counter}: ")
    user_words_list.append(word)
    counter += 1

for each_word in user_words_list:
    if len(each_word) > limit_characters:
        more_than_limit_characters.append(each_word)

print(more_than_limit_characters)