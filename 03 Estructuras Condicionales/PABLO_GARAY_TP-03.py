# TP 2 Estructuras Condicionales - Pablo Garay

# 1- Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

age: int = int(input("Por favor, ingrese su edad: "))

if age > 18:
    print("Es mayor de edad")

# 2- Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar 
# por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”

grade: int = int(input("Por favor, ingrese su nota: "))

if grade >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3- Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por pantalla
# el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par"

number: int = int(input("Por favor, ingrese un número: "))

if number % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4- Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

age: int = int(input("Por favor, ingrese su edad: "))

if age < 12:
    print("Niño/a")
elif age < 18:
    print("Adolescente")
elif age < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5- Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por pantalla el mensaje "Ha ingresado una contraseña correcta";
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

password: int = int(input("Por favor, ingrese su contraseña: "))

if password >= 8 and password <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6- Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y 
# las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random

random_number_list: list = [random.randint(1, 100) for _ in range(50)]

moda: int = mode(random_number_list)
mediana: float = median(random_number_list)
media: float = mean(random_number_list)

if media > mediana:
    print("Sesgo positivo")
elif media < mediana:
    print("Sesgo negativo")
else:
    print("No hay sesgo")

# 7- Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal,
# añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario,
# dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

word: str = input("Por favor, ingrese una palabra: ")

if word[-1] in "aeiouAEIOU":
    print(f"{word}!")
else:
    print(word)

# 8-  Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee.

name: str = input("Por favor, ingrese su nombre: ")
print(f"A continuacion seleccione una de las siguientes opciones: \n 1- Si quiere su nombre en mayúsculas. \n 2- Si quiere su nombre en minúsculas \n 3- Si quiere su nombre con la primera letra mayúscula")
option: int = int(input("Por favor, ingrese su opción: "))

TO_UPPER: int = 1
TO_LOWER: int = 2
TO_TITLE: int = 3

if option == TO_UPPER:
    print(name.upper())
elif option == TO_LOWER:
    print(name.lower())
elif option == TO_TITLE:
    print(name.title())
else:
    print("Por favor, ingrese una opción válida")

# Opcion optimizada:
dic = {
    1: name.upper(),
    2: name.lower(),
    3: name.title()
}

print(dic.get(option, "Por favor, ingrese una opción válida"))

# 9- Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las
# siguientes categorías según la escala de Richter e imprima el resultado por pantalla

earthquake: int = int(input("Por favor, ingrese la magnitud del terremoto: "))

if earthquake < 3:
    print("Muy leve")
elif earthquake < 4:
    print("Leve")
elif earthquake < 5:
    print("Moderado")
elif earthquake < 6:
    print("Fuerte")
elif earthquake < 7:
    print("Muy grave")
else:
    print("Extremo")

# 10- Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es
# y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# Periodo del año                                                  || Estación en el hemisferio norte  || Estación en el hemisferio sur
# Desde el 21 de diciembre hasta el 20 de marzo (incluidos)        || Invierno                         || Verano
# Desde el 21 de marzo hasta el 20 de junio (incluidos)            || Primavera                        || Otoño
# Desde el 21 de junio hasta el 20 de septiembre (incluidos)       || Verano                           || Invierno
# Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)   || Otoño                            || Primavera


hemisphere: str = input("Por favor, ingrese el hemisferio (N, S): ")
month: int = int(input("Por favor, ingrese el mes (del 1 al 12, siendo 1 Enero y 12 Diciembre): "))
day: int = int(input("Por favor, ingrese el día (del 1 al 31, si corresponde): "))

if month == 12 and day >= 21 or month == 1 or month == 2 or month == 3 and day <= 20:
    print(f"Usted se encuentra en {hemisphere.upper() == 'N' and 'Invierno' or 'Verano'}")
elif month == 3 and day >= 21 or month == 6 and day <= 20:
    print(f"Usted se encuentra en {hemisphere.upper() == 'N' and 'Primavera' or 'Otoño'}")
elif month == 6 and day >= 21 or month == 9 and day <= 20:
    print(f"Usted se encuentra en {hemisphere.upper() == 'N' and 'Verano' or 'Invierno'}")
elif month == 9 and day >= 21 or month == 12 and day <= 20:
    print(f"Usted se encuentra en {hemisphere.upper() == 'N' and 'Otoño' or 'Primavera'}")
else:
    print("Por favor, ingrese una opción válida")