# TP 7 Aplicación de la Recursividad - Pablo Garay

# 1
"""
Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        result = factorial(n - 1)
        print(f"El factorial de {n} es: {n * result}")
        return n * result

def factoriales():
    numero: int = int(input("Ingrese un número entero positivo: "))
    print("\nFactoriales desde 1 hasta", numero, ":")

    if numero < 1:
        print("Por favor ingrese un número mayor o igual a 1")
        return
    
    # factorial(numero - 1)
    return factorial(numero)

factoriales()

# 2
"""
Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
"""
def fibonacci(n, memo={0: 0, 1: 1}):
    """
    Función recursiva que calcula el n-ésimo número de Fibonacci.
    Utiliza memorización para mejorar la eficiencia.
    """
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

def mostrar_serie_fibonacci():
    """
    Muestra la serie de Fibonacci desde la posición 0 hasta n
    """
    posicion = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))
    if posicion < 0:
        print("Por favor ingrese un número no negativo")

    print(f"Serie de Fibonacci hasta la posición {posicion}:")
    for i in range(posicion + 1):
        print(f"Posición {i}: {fibonacci(i)}", end=" \n ")
    print()  # Salto de línea al final

mostrar_serie_fibonacci()

# 3
"""
Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛
𝑚 = 𝑛 ∗ 𝑛
(𝑚−1)
. Prueba esta función en un
algoritmo general.
"""
def potenciador(num: int, posicion: int): 
  return num * num if posicion == 2 else num * potenciador(num, posicion - 1)

print(potenciador(12, 5))

# 4
"""
Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
"""
def de_decimal_a_binario(num: int):
    if num <= 1:
        return str(num)

    return de_decimal_a_binario(num // 2) + str(num % 2)

numero = int(input("Ingrese un número entero positivo: "))
if numero < 0:
  print("Por favor ingrese un número positivo")
else:
  binario = de_decimal_a_binario(numero)
  print(f"El número {numero} en binario es: {binario}")

# 5
"""
Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
Ejemplos:
  es_palindromo("anita lava la tina") -> True
  es_palindromo("ana abre la ventana") -> False
"""
def  es_palindromo(palabra: str)-> bool:
  # Validacion para aceptar tambien frases
  palabra = palabra.replace(" ", "")
  if len(palabra) == 1:
    return True

  if palabra[0] == palabra[-1]:
    return es_palindromo(palabra[1:-1])

  return False

print(es_palindromo(input("Ingrese una palabra o frase: ")))

# 6
"""
Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
  suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
  suma_digitos(9) → 9
  suma_digitos(305) → 8 (3 + 0 + 5)
"""
def  suma_digitos(num: int) -> int:
  return num if num < 10 else num % 10 + suma_digitos(num // 10)

print(suma_digitos(int(input("Ingrese un numero: "))))

# 7
"""
Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
Ejemplos:
  contar_bloques(1) → 1 (1)
  contar_bloques(2) → 3 (2 + 1)
  contar_bloques(4) → 10 (4 + 3 + 2 + 1)
"""
def  contar_bloques(num: int) -> int:
  return 1 if num == 1 else num + contar_bloques(num - 1)

print(contar_bloques(int(input("Ingrese un numero: "))))

# 8
"""
Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
Ejemplos:
  contar_digito(12233421, 2) → 3
  contar_digito(5555, 5) → 4
"""
def contar_digito(numero: int, digito: int) -> int:
  if numero == 0:
      return 0
  return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

print(contar_digito(int(input("Ingrese un numero: "))))