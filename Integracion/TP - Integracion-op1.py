# Calculadora binaria
import sys

def son_todos_digitos(numero: str) -> bool: 
    """
    Verifica si el número pasado como argumento contiene solo dígitos.

    Args:
        numero (str): Cadena a verificar.

    Returns:
        bool: True si la cadena contiene solo dígitos, False en caso contrario.
    """
    return numero.isdigit()

def tiene_longitud(numero: str) -> bool:
    """
    Verifica que el número pasado como argumento tiene longitud.

    Args:
        numero (str): Cadena a verificar.

    Returns:
        bool: True si la cadena tiene al menos un carácter, False si está vacía.
    """
    return len(numero) != 0

def es_binario(numero: str) -> bool:
    """
    Verifica si el número pasado como argumento es un número binario.

    Args:
        numero (str): Cadena a verificar.

    Returns:
        bool: True si la cadena es un número binario, False en caso contrario.
    """
    for i in range(0, len(numero)):
        if int(numero[i]) < 0 or int(numero[i]) > 1:
            return False
    return True

def comprobar_negativo(num):
    if int(num[0]) == 0 :
        return False
    elif not (len(num) in [2, 4, 8, 16, 32, 64, 128, 256]):
        return False
    else:
        return True

def validar_numero_binario(mensaje: str) -> str:
    """
    Solicita al usuario un número binario y válida:
    * que la cadena no esté vacía.
    * que la cadena contenga solo digitos.
    * que la cadena contenga números 0 y 1

    Args:
        mensaje (str): Mensaje que se muestra al usuario para solicitar el número.

    Returns:
        str: El número binario válido ingresado por el usuario.
    """
    num: str = input(mensaje)
    tipo_num = input("El numero ingresado es un binario negativo, es una palabra de 2^n bits y esta representado en complemento A2? (si/no)")

    if not (tiene_longitud(num) and son_todos_digitos(num)):
        return validar_numero_binario("El numero ingresado no es valido, ingrese otro: ")

    if not (es_binario(num)):
        return validar_numero_binario("El numero ingresado no es binario, ingrese otro: ")

    if tipo_num in ["si", "SI", "NO", "no"] and (tipo_num == ("si" or "SI")):
        negativo: bool = comprobar_negativo(num)
        if negativo == False:
            print("El numero ingresado no es un binario negaativo, reintente")
            validar_numero_binario(mensaje)
        else:
            decimal = convertir_a_decimal(num, tipo_num) #convertir a decimal y preguntar si es correcto
            pass

    return [num, tipo_num]

def convertir_a_decimal(numero: str, tipo_num) -> int:
    """
    Convierte una cadena binaria a su valor decimal.

    Args:
        numero (str): Cadena que representa un número binario.

    Returns:
        int: Valor decimal equivalente.
    """
    decimal: int = 0

    if tipo_num in ["NO", "no"]:
        for i in range(len(numero), 0, -1):
            decimal += int(numero[i-1]) * (2 ** (len(numero)-i))
        return decimal
    else:
        numero = complementoA2(numero[1:])
        for i in range(len(numero), 1, -1):
            decimal += int(numero[i-1]) * (2 ** (len(numero)-i))
        return decimal*-1
        


def rellenar_con_ceros_izquierda(numero: str, longitud: int) -> str:
    """
    Rellena con ceros a la izquierda para igualar la longitud de los números binarios.

    Args:
        numero (str): Número binario como cadena.
        longitud (int): Cantidad de ceros a agregar.

    Returns:
        str: Número binario con ceros agregados a la izquierda.
    """
    numero_invertido = numero[::-1]
    numero_invertido += longitud * "0"
    return numero_invertido[::-1]

def igualar_numeros(binario1: str, binario2: str):
    """
    Verifica si los dos numeros ingresados por el usuario tienen la misma cantidad de bits 
    caso contrario, los iguala.

    Args: binario1(str) y binario2(str) numeros binarios como cadenas

    Returns:
        str: Los dos número binario recibidos, igualados en cantidad de bits.
    """
    longitud = abs(len(binario1) - len(binario2))
    if len(binario1) > len(binario2):
        binario2 = rellenar_con_ceros_izquierda(binario2, longitud)
    else:
        binario1 = rellenar_con_ceros_izquierda(binario1, longitud)
    return (binario1, binario2)

def sumar(numeros: list[str]):
    """
    Suma dos números binarios representados como cadenas.

    Args:
        numeros (list[str]): Lista con dos cadenas que representan números binarios.

    Returns:
        str: Resultado de la suma en binario.
    """
    binario1: str = numeros[0][0]
    binario2: str = numeros[1][0]
    tipo_num1 = numeros[0][1]
    tipo_num2 = numeros[1][1]
    resultado : str = ""
    carry: int = 0

    binario1, binario2 = igualar_numeros(binario1, binario2)

    def sumando(num1: str, num2: str) -> None:
        """
        Suma dos dígitos binarios (como caracteres) y actualiza el resultado y el carry globales.

        Args:
            num1 (str): Primer dígito binario a sumar ('0' o '1').
            num2 (str): Segundo dígito binario a sumar ('0' o '1').

        Returns:
            None: Modifica las variables 'resultado' y 'carry' no locales.
        """
        nonlocal carry
        nonlocal resultado 

        if int(num1) == 0 and int(num2) == 0:
            carry -= 1
            resultado  += "0"
        elif (int(num1) == 0 and int(num2) == 1) or (int(num1) == 1 and int(num2) == 0):
            carry -= 1
            resultado  += "1"
        else:
            carry += 1
            resultado  += "0"

    def sumando_con_carry(num1: str, num2: str) -> str:
        """
        Suma dos dígitos binarios considerando el acarreo previo y devuelve el resultado como carácter.

        Args:
            num1 (str): Primer dígito binario a sumar ('0' o '1').
            num2 (str): Segundo dígito binario a sumar ('0' o '1').

        Returns:
            str: Resultado de la suma considerando el acarreo ('0' o '1').
        """
        nonlocal carry

        if (int(num1) == 0 and int(num2) == 1) or (int(num1) == 1 and int(num2) == 0):
            carry -= 1
            return "1"
        else:
            carry += 1
            return "0"

    for i in range(len(binario1)-1, -1, -1):
        # Reiniciamos el carry en caso negativo
        if carry < 0:
            carry = 0

        if carry > 0:
            sumando(sumando_con_carry(binario1[i], "1"), binario2[i]) 
        else:
            sumando(binario1[i], binario2[i])

    # Añadimos el carry final si es 1
    if carry > 0:
        resultado += "1"

    # Convertimos los binarios a decimales para verificar el resultado
    decimal1 = convertir_a_decimal(binario1, tipo_num1)
    decimal2 = convertir_a_decimal(binario2, tipo_num2)
    total = decimal1 + decimal2
    resultado_decimal = convertir_a_decimal(resultado[::-1], "no") # modificar el segundo argumento
    if total == resultado_decimal:
        print("Binario verificado...")

    return resultado[::-1]

def complementoA2(binario2: str, tipo_num2):
    """
    Recibe un binario como cadena, lo invierte y suma 1 

    Arg: binario2(str) numero binario como cadena

    Returns:
            str: El complemento A2 del numero dado.
    """
    binarioA1 = ""
    for i in range(len(binario2)):
        if int(binario2[i]) == 0:
            binarioA1 += "1"
        else:
            binarioA1 += "0"

    binarioA2 = sumar([binarioA1, tipo_num2, "1", "NO"]) # ver esto como se comporta
    return binarioA2

def restar(numeros: list[str]):
    """
    Resta dos números binarios representados como cadenas.

    Args:
        numeros (list[str]): Lista con dos cadenas que representan números binarios.

    Returns:
        str: Resultado de la resta en binario y en caso de resultado negativo, su expresion en valor absoluto.
    """

    binario1: str = numeros[0][0]
    binario2: str = numeros[1][0]
    tipo_num1: str = numeros[0][1]
    tipo_num2: str = numeros[1][1]
    resultado : str = ""
    num_mod = []

    binario1, binario2 = igualar_numeros(binario1, binario2)
    if binario1 > binario2:
        num_mod = [[binario1, tipo_num1], [complementoA2(binario2, tipo_num2), tipo_num2]]
        resultado = sumar(num_mod)
        if len(resultado) > len(binario2):
            resultado = resultado[1:]
            return f"El resultado de la resta es {resultado}"
    else:
         resultado = sumar(num_mod)
         resultado1 = complementoA2(resultado[1:])
         return f"El resultado es {resultado}. Como es un binario negativo, el valor absoluto es {resultado1} "

# def multiplicar():
# def dividir():

def calculadora():
    """
    Menú principal de la calculadora binaria.
    Permite seleccionar la operación y solicita los números binarios al usuario.
    """
    print("\nElije la operacion a realizar del siguiente menu:\n ")
    print("1 - Sumar \n2 - Resta \n3 - Multiplicar \n4 - Dividir\n5 - Salir")
    operacion: int = int(input("\nIngrese la operacion elegida: "))
    lista_de_operadores: tuple = (1, 2, 3, 4, 5)
    if operacion not in lista_de_operadores:
        print("Opcion no valida, intente de nuevo")
        return calculadora()
    elif operacion == lista_de_operadores[4]:
        sys.exit()


    numeros: list = []
    for i in range(0, 2):
        numeros.append(validar_numero_binario(f"Ingrese el numero binario {i+1}: "))

    if operacion == lista_de_operadores[0]:
        print(f"El resultado de la suma es: {sumar(numeros)}")
    elif operacion == lista_de_operadores[1]:
        print(f"{restar(numeros)}")
    elif operacion == lista_de_operadores[2]:
        print("Multiplicando")
    elif operacion == lista_de_operadores[3]:
        print("Dividiendo")
    

calculadora()


