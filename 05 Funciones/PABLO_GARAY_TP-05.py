# TP 5 Funciones - Pablo Garay

# 1- Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
def imprimir_hola_mundo() -> None:
    print("Hola Mundo")

imprimir_hola_mundo()

# 2- Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
def saludar_usuario(nombre: str) -> None:
    print(f"Hola {nombre}!")

saludar_usuario(input("Ingrese su nombre: "))

# 3- Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: 
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los 
# valores ingresados.
def  informacion_personal(nombre: str, apellido: str, edad: int, residencia: str) -> None:
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre: str = input("Ingrese su nombre: ")
apellido: str = input("Ingrese su apellido: ")
edad: int = int(input("Ingrese su edad: "))
residencia: str = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# 4-  Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
import math

def calcular_area_circulo(radio: float) -> float:
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio: float) -> float:
    return 2 * 3.14159 * radio

radio: float = float(input("Ingrese el radio de un circulo: "))

print(f"El area del circulo es {calcular_area_circulo(radio):.2f} y el perimetro es {calcular_perimetro_circulo(radio):.2f}")

# 5- Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas(segundos: float) -> float:
    return segundos / 3600

segundos: float = float(input("Ingrese una cantidad de segundos: "))

print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos):.2f} horas")

# 6- Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero: int) -> None:
    for i in range(1, 11):
        print(f"{numero} por {i} = {numero * i}")

numero: int = int(input("Por favor, ingrese un numero: "))
tabla_multiplicar(numero)

# 7- Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de 
# sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
def mostrar_resultados(resultados: tuple) -> None:
    print(f"La suma de {a} y {b} es {resultados[0]}")
    print(f"La resta de {a} y {b} es {resultados[1]}")
    print(f"La multiplicacion de {a} y {b} es {resultados[2]}")
    print(f"La division de {a} y {b} es {resultados[3]}")

def operaciones_basicas(a: int, b: int) -> None:
    mostrar_resultados((a + b, a - b, a * b, a / b))

a: int = int(input("Por favor, ingrese un numero: "))
b: int = int(input("Por favor, ingrese otro numero: "))

operaciones_basicas(a, b)

# 8- Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso: float, altura: float) -> float:
    return peso / (altura ** 2)

peso: float = float(input("Por favor, ingrese su peso: "))
altura: float = float(input("Por favor, ingrese su altura: "))

print(f"Su IMC es {calcular_imc(peso, altura):.2f}")

# 9- Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
def celsius_a_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

celsius: float = float(input("Por favor, ingrese la temperatura en grados Celsius: "))

print(f"La temperatura en grados Fahrenheit es {celsius_a_fahrenheit(celsius):.2f}")

# 10- Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.
def calcular_promedio(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3

a: float = float(input("Por favor, ingrese el primer número: "))
b: float = float(input("Por favor, ingrese el segundo número: "))
c: float = float(input("Por favor, ingrese el tercer número: "))

print(f"El promedio de {a}, {b} y {c} es {calcular_promedio(a, b, c):.2f}")