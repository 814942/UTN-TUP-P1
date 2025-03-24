# TP 1 Secuenciales - Pablo Garay

# 1- Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola mundo!")

# 2- Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
name = input("Ingresa tu nombre: ")

print(f"Hola {name}!, bienvenido a Python")

# 3- Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
print("Bienvenido!!! Completa los siguientes campos, por favor")

first_name = input("Ingresa tu nombre: ")
last_name = input("Ingresa tu apellido: ")
age = input("Ingresa tu edad: ")
location = input("Ingresa tu ubicación: ")

print(f"Hola soy {first_name} {last_name}, y tengo {age} años, y vivo en {location}")

# 4- Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
import math

radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

# 5- Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
seconds = float(input("Ingrese una cantidad de segundos: "))
hours = seconds / 3600

print(f"{seconds} segundos equivalen a {hours:.2f} horas")

# 6- Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
user_number = int(input("Por favor, ingrese un numero: "))

for i in range(1, user_number + 1):
    print(f"{user_number} por {i} = {user_number * i}")

print("Tabla de multiplicar completada!")

# 7- Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos..
print("Ingrese dos numeros, enteros distintos del 0, y le mostrare el resultado de sumarlos, dividirlos, multiplicarlos y restarlos")

first_user_number = int(input("Por favor, ingrese el primer numero: "))
second_user_number = int(input("Por favor, ingrese el segundo numero: "))

if first_user_number <= 0 or second_user_number <= 0:
    print("Por favor, ingrese numeros enteros distintos del 0")
    exit()

print(f"La suma de {first_user_number} y {second_user_number} es {first_user_number + second_user_number}")
print(f"La division de {first_user_number} y {second_user_number} es {(first_user_number / second_user_number):.2f}")
print(f"La multiplicacion de {first_user_number} y {second_user_number} es {first_user_number * second_user_number}")
print(f"La resta de {first_user_number} y {second_user_number} es {first_user_number - second_user_number}")

# 8- Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: IMC = peso / altura^2
height = float(input("Por favor, ingrese su altura: "))
weight = float(input("Por favor, ingrese su peso: "))

imc = weight / height ** 2

print(f"Su IMC es {imc:.2f}")

# 9- Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =  9. 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
celsius = float(input("Por favor, ingrese la temperatura en grados Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"La temperatura en grados Fahrenheit es {fahrenheit:.2f}")

# 10- Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
print("Ingrese 3 numeros, y le mostrare el promedio de ellos")
num1 = float(input("Por favor, ingrese el primer numero: "))
num2 = float(input("Por favor, ingrese el segundo numero: "))
num3 = float(input("Por favor, ingrese el tercer numero: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de {num1}, {num2} y {num3} es {promedio:.2f}")