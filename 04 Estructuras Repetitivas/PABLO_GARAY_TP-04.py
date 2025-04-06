# TP 4 Estructuras Repetitivas - Pablo Garay

# 1 - Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for x in range(101):
    print(x)

# 2 - Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
counter: int = 0
num: int = abs(int(input("Por favor, ingrese un número: ")))

if num == 0:
    counter = 1
else:
    while num > 0:
        num //= 10
        counter += 1

print(f"Su numero posee {counter} digitos")

# 3 - Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
total: int = 0
firstNum: int = int(input("Por favor, ingrese el primer numero: "))
secondNum: int = int(input("Por favor, ingrese el segundo numero: "))

for x in range(firstNum + 1, secondNum):
    total += x

print(f"La suma de los numeros entre {firstNum} y {secondNum} es: {total}")

# 4 - Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
stop: bool = False
total: int = 0

while not stop:
    num = int(input("Por favor, ingrese un numero: "))
    total += num
    if num == 0:
        stop = True

print(f"La suma de los numeros ingresados es: {total}")

# 5 - Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

num: float = float('inf')
counter: int = 0
randomNum: int = random.randint(0, 9)
print("Adivine el numero en la menor cantidad de intentos")

while num != randomNum:
    num = int(input("Por favor, ingrese un numero: "))
    counter += 1

print(f"Felicidades, has adivinado el numero en {counter} intentos")

# 6 - Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for x in range(100, -1, -1):
    if x % 2 == 0:
        print(x, end=' ')

# 7 - Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
num = int(input("Por favor, ingrese un numero positivo: "))
if num < 0:
    print("Por favor, ingrese un numero positivo")
    exit()

counter: int = 0
for x in range(0, num + 1):
    counter += x

print(f"La suma de los numeros entre 0 y {num} es: {counter}")

# 8 - Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son
# pares, cuántos son impares, cuántos son negativos y cuántos son positivos.
even_num: int = 0
odd_num: int = 0
positive_num: int = 0
negative_num: int = 0

# Para i = 0 Hasta 100 Hacer
#     Escribir "Ingresa el número ", i+1
#     Leer num
#     Si num MOD 2 == 0 Entonces
#         even_num = even_num + 1
#     SiNo
#         odd_num = odd_num + 1
#     FinSi
#     Si num < 0 Entonces
#         negative_num = negative_num + 1
#     SiNo
#         positive_num = positive_num + 1
#     FinSi
# FinPara

for x in range(100):
    num = int(input("Por favor, ingrese un numero: "))
    # Condicional para determinar si es par o no
    if num % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
    # Condicional para determinar positivos o no
    if num > 0:
        positive_num += 1
    elif num < 0:
        negative_num += 1

print(f"La cantidad de numeros pares es: {even_num}")
print(f"La cantidad de numeros impares es: {odd_num}")
print(f"La cantidad de numeros positivos es: {positive_num}")
print(f"La cantidad de numeros negativos es: {negative_num}")

# 9 - Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
acc: int = 0

# Para i = 0 Hasta 100 Hacer
#     Escribir "Ingresa el número ", i+1
#     Leer num
#     acumulador = acumulador + num
# FinPara

for x in range(100):
    num = int(input("Por favor, ingrese un numero: "))
    acc += num

print(f"El promedio es: {acc / 10:.2f}")

# 10 - Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.
num: int = abs(int(input("Por favor, ingrese un numero: ")))
inverted_num: int = 0

# Mientras num_abs > 0 Hacer
#     digito = num_abs MOD 10
#     num_invertido = num_invertido * 10 + digito
#     num_abs = trunc(num_abs / 10)
# FinMientras

while num > 0:
    # Obtener último dígito
    digito = num % 10
    # Construir el número invertido
    inverted_num = inverted_num * 10 + digito
    # Eliminar último dígito
    num = num // 10

print(f"El numero invertido es: {inverted_num}")