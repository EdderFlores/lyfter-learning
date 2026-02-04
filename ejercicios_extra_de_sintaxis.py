import random
# Excercise 1 

#Excercise 1.1

product_price = float(input("Ingresa el precio del producto: "))
discount = 0
final_price = 0
if product_price < 100:
    discount = .02
    final_price = product_price - (product_price * discount)
else:
    discount = .1
    final_price = product_price - (product_price * discount)

print(f"El precio final del producto con descuento es de: ${final_price}")
print(f"Obtuviste un descuentdo del %{discount*100}")
print("")

#Excercise 1.2

seconds_left = 0
time_in_seconds = int(input("Ingrese un tiempo en segundos: "))
ten_minutes_in_seconds = 10 * 60
if time_in_seconds < ten_minutes_in_seconds:
    seconds_left = ten_minutes_in_seconds - time_in_seconds
    print(f"Faltan {seconds_left} segundos para llegar a 10 minutos.")
elif time_in_seconds > ten_minutes_in_seconds:
    print("Mayor")
else:
    print("Igual")
print("")

#Excercise 1.3

user_number = int(input("Ingresa un número entero: "))
total_sum = 0
summed_times = 0
while summed_times != user_number:
    summed_times = summed_times + 1
    total_sum = total_sum + summed_times
print(f"La suma de los números enteros desde 1 hasta {user_number} es: {total_sum}")

print("")

#Excercise 2
#Excercise 2.1
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

print("")

#Excercise 2.2
first_number = int(input("Ingresa el primer número: "))
second_number = int(input("Ingresa el segundo número: "))
third_number = int(input("Ingresa el tercer número: "))
expected_total = 30
all_numbers_sum = first_number + second_number + third_number
if all_numbers_sum == expected_total:
    print("Correcto")
elif first_number == expected_total:
    print("Correcto")
elif second_number == expected_total:
    print("Correcto")
elif third_number == expected_total:
    print("Correcto")
else:
    print("Incorrecto")

print("")

#Excercise 3

celcius_temp = float(input("Ingresa la temperatura en grados Celsius: "))
farenheit_temp = (celcius_temp / (5/9)) + 32
kelvin_temp = celcius_temp + 273.15

print(f"La temperatura en grados Celsius es: {celcius_temp} °C")
print(f"La temperatura en grados Farenheit es: {farenheit_temp} °F")
print(f"La temperatura en grados Kelvin es: {kelvin_temp} K")  
print("")

#Excercise 4

multiplier_number = int(input("Ingresa un número para ver su tabla de multiplicar: "))
counter = 1
total_multiplication_times = 12
while counter <= total_multiplication_times:
    print(f"{multiplier_number} x {counter} = {multiplier_number*counter}")
    counter += 1