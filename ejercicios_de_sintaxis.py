import random

""" Ejercicio 1.

first_string = "Hola"
second_string = "Mundo"
first_int = 10
first_float = 5.5
first_int_list = [
    1,
    2,
    3,
    4
]
first_string_list = [
    "Roberto",
    "Miguel",
    "Sheldon"
]
first_boolean = False
second_boolean = True

print(first_string + " " + second_string) 
print(second_string + " " + str(first_int))
print(str(first_int) + " " + first_string)
print(first_int_list + first_string_list)
print(first_float + first_int)
print(first_boolean + second_boolean)

# Ejercicio 2.

name = input("Cual es tu primer nombre?")
last_name = input("Cual es tu apellido?")
age = int(input("Cual es tu edad?"))
stage = ""
full_name = name + " " + last_name
if age < 2:
    stage = "bebe"
elif age < 12:
    stage = "niño"
elif age < 18:
    stage = "adolescente"
elif age < 30:
    stage = "adulto joven"
elif age < 60:
    stage = "adulto"
else:
    stage = "adulto mayor"
print(f"Hola {full_name}, tienes {age} años y eres un {stage}.")
"""

#### Ejercicio 3 

secret_number = random.randint(1, 10)
user_guess = 0

while user_guess != secret_number:
    user_guess = int(input("Adivina un número entre 1 y 10: "))
    if user_guess < secret_number:
        print("Demasiado bajo. Intenta de nuevo.")
    elif user_guess > secret_number:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print("¡Felicidades! Has adivinado el número secreto.") 

#### Ejercicio 4

first_number = int(input("Ingresa el primer número: "))
second_number = int(input("Ingresa el segundo número: "))
third_number = int(input("Ingresa el tercer número: "))

if first_number > second_number and first_number > third_number:
    largest = first_number
elif second_number > first_number and second_number > third_number:
    largest = second_number
else:
    largest = third_number

print(f"El número más grande es: {largest}")

#### Ejercicio 5
counter = 1 
current_grade = 0
total_passed_grades = 0
total_failed_grades = 0
average_passed_grades = 0
average_failed_grades = 0
total_grades = int(input("¿Cuántas calificaciones deseas ingresar? "))

while counter <= total_grades:
    current_grade = float(input(f"Ingresa la calificación {counter}: "))
    if current_grade >= 6.0:
        total_passed_grades += current_grade
    else:
        total_failed_grades += current_grade
    counter += 1