# Calculadora binaria

def son_todos_digitos(numero: str) -> bool: 
    # Verifica que el numero pasado como argumento, contiene solo digitos. 
    # Si es asì devuelve True, caso contrario False
    if numero.isdigit():
        return True
    else:
        return False

def son_todos_digitos(numero: str) -> bool: 
    # Verifica que el numero pasado como argumento, contiene solo digitos. 
    # Si es asì devuelve True, caso contrario False
    if numero.isdigit():
        return True
    else:
        return False

def tiene_longitud(numero: str) -> bool: 
    if len(numero) != 0:
        return True
    else:
        return False

def validar_numero_binario(mensaje: str):
    num: str = input(f"{mensaje}: ")
    # validar que ingrese algun valor
    longitud: bool = tiene_longitud(num)
    # validar que sean todos digitos
    binario: bool = son_todos_digitos(num)

    if binario and longitud:
        for i in range(0, len(num)):
            if int(num[i]) < 0 or int(num[i]) > 1:
                return validar_numero_binario("El numero ingresado no es binario, ingrese otro")
    else:
        return validar_numero_binario("El numero ingresado no es valido, ingrese otro")

    return num

def convertir_a_decimal(num1):
    suma1 = 0

    for i in range(len(num1), 0, -1):
        suma1 += int(num1[i-1]) * (2 ** (len(num1)-i))
    return suma1

def agregar_numeros(num: str, longitud: int) -> str:
    numero_invertido = num[::-1]
    numero_invertido += longitud * "0"
    return numero_invertido[::-1]

def sumar(numeros: list[str]):
    num1: str = numeros[0]
    num2: str = numeros[1]
    total: str = ""
    carry: int = 0
    # Comprobar la longitud
    longitud = abs(len(num1) - len(num2))
    if len(num1) > len(num2):
        num2 = agregar_numeros(num2, longitud)
    else:
        num1 = agregar_numeros(num1, longitud)

    def sumando(num1: str, num2: str) -> str:
        nonlocal carry
        nonlocal total

        if int(num1) == 0 and int(num2) == 0:
            carry -= 1
            total += "0"
        elif (int(num1) == 0 and int(num2) == 1) or (int(num1) == 1 and int(num2) == 0):
            carry -= 1
            total += "1"
        else:
            carry += 1
            total += "0"

    def sumando_con_carry(num1: str, num2: str) -> str:
        nonlocal carry

        if (int(num1) == 0 and int(num2) == 1) or (int(num1) == 1 and int(num2) == 0):
            carry -= 1
            return "1"
        else:
            carry += 1
            return "0"

    # igualar los digitos agregando 0 a la izquierda
    # iterar y sumar cada digito empezando de der a izq
    for i in range(len(num1)-1, -1, -1):
        # carry = 0 if carry < 0 else carry
        if carry < 0:
            carry = 0

        if carry > 0:
            sumando(sumando_con_carry(num1[i], "1"), num2[i])
        else:
            sumando(num1[i], num2[i])

    if carry > 0:
        total += "1"

    # agregar comparacion parceandolo a decimal
    # escribir mejor los nombres
    num1_parceado = convertir_a_decimal(num1)
    num2_parceado = convertir_a_decimal(num2)
    total_parceado = num1_parceado + num2_parceado
    total2 = convertir_a_decimal(total[::-1])
    if total_parceado == total2:
        print("Esta bieeeee")

    print(total)
    print(total[::-1])
    return total[::-1]
# def resta():
# def multiplicar():
# def dividir():

def calculadora():
    print("Elije la operacion a realizar del siguiente menu: ")
    print("1 - Sumar \n2 - Resta \n3 - Multiplicar \n4 - Dividir")
    # Agregar la operacion para cerrar el programa
    operacion: int = int(input("Elije la operacion: "))
    # Validar la operacion
    lista_de_operadores: tuple = (1, 2, 3, 4)
    numeros: list = []
    for i in range(0, 2):
        numeros.append(validar_numero_binario(f"Ingrese el numero binario {i+1}"))

    if operacion == lista_de_operadores[0]:
        print(f"El resultado es: {sumar(numeros)}")
    elif operacion == lista_de_operadores[1]:
        print("Restando")
    elif operacion == lista_de_operadores[2]:
        print("Multiplicando")
    elif operacion == lista_de_operadores[3]:
        print("Dividiendo")

# operador = 1
# ["1010", "1"]
# Validamos los arg.
# Guardamos los arg.
# Realizamos la operacion pertinente

calculadora()


