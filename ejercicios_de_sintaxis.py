""" Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
Por ejemplo:
string + string → ?
string + int → ?
int + string → ?
list + list → ?
string + list → ?
float + int → ?
bool + bool → ? """

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

# Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.