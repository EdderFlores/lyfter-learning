# Genera Correo Electronico en formato profesional obteniendo dominio y nombre y apellido de un empleado.
""" 
Inicio
Definir dominio
Definir professional_email
dominio = "empresa.com"
Mostrar "Cual es tu nombre?"
Pedir nombre
Mostrat "Cual es tu apellido?"
Pedir apellido
professional_email = nombre + "." + apellido + "@" + dominio
Mostrar "Tu correo electronico profesional es: " + professional_email
Fin
 """

domain = "business.com"
professional_email = ""
name = input("What is your first name? ")
last_name = input("What is your last name? ")
professional_email = name + "." + last_name + "@" + domain
print("Your professional email is: " + professional_email)