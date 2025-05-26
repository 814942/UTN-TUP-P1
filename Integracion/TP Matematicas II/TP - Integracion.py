# Generación automática de los conjuntos de dígitos únicos.
def generador_de_conjuntos(dni: int):
  conjuntos: list[int] = []
  for i in range(10):
    if str(i) in str(dni):
      conjuntos.append(i)

  return conjuntos

# Suma total de los dígitos de cada DNI.
def suma_dni(dni: int):
  if dni == 0:
    return 0
  else:
    return dni % 10 + suma_dni(dni // 10)

def es_bisiesto(anio):
  """
  Determina si un año es bisiesto.
  Un año es bisiesto si es divisible por 4, 
  excepto los divisibles por 100, a menos que también sean divisibles por 400.
  """
  return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

# Operaciones con años de nacimiento
def nacimientos():
  print("Ingrese los años de nacimiento de los integrantes (ingrese 'fin' para terminar):")
  anios = []

  while True:
    entrada = input("Año de nacimiento (o 'fin' para terminar): ")
    if entrada.lower() == 'fin':
      if len(anios) < 2:
        print("Debe ingresar al menos dos años de nacimiento.")
        continue
      break

    anio = int(entrada)
    if anio < 1925 or anio > 2025:
      print("Por favor ingrese un año válido (entre 1925 y 2025).")
      continue
    anios.append(anio)

  pares = 0
  impares = 0

  for anio in anios:
    if anio % 2 == 0:
      pares += 1
    else:
      impares += 1

  print(f"\nNacieron {pares} personas en años pares y {impares} en años impares.")

  if all(anio > 2000 for anio in anios):
    print("Grupo Z")

  bisiestos = [anio for anio in anios if es_bisiesto(anio)]
  if bisiestos:
    print(f"Tenemos un año especial: {', '.join(map(str, bisiestos))} es/son bisiesto(s).")

  print("\nProducto cartesiano (año de nacimiento, edad en 2025):")
  for anio in anios:
    edad = 2025 - anio
    print(f"({anio}, {edad})", end=" ")
    print("\n")

# Union de conjuntos 
def union(dnis: list[int]) -> list[int]:
  if not dnis:
    return []

  conjunto_unico = set()
  for dni in dnis:
    conjunto_unico.update(generador_de_conjuntos(dni))

  return list(conjunto_unico)

# Diferencia de dos conjuntos A - B
def diferencia(lista_dni: list) -> list:
  """
  Realiza la diferencia de dos conjuntos A y B

  Args:
      List: Con los documentos ingresados por el usuario.

  Returns:
        List: conjunto formado por la diferencia de A - B
  """

  a = generador_de_conjuntos(lista_dni[0]) # Tomo el indice 0 de la lista y se lo paso a la función gnerador_de_conjuntos
  b= generador_de_conjuntos(lista_dni[1]) # Tomo el indice 1 de la lista y se lo paso a la función gnerador_de_conjuntos
  d=[] # Creamos una lista vacia para almacenar los valores del conjunto que será la diferencia entre A y B
  for i in range(len(a)):
    if a[i] not in b: # Este condicional me selecciona los elementos de A que no están en B, y los guarda en la lista d
      d.append(a[i])
  return d

# Complemento del conjunto Union.
def complemento_U(lista_dni)-> bool:
  """
  Realiza el complemento del conjunto X, siendo X una union de conjuntos formados por dígitos del 0 al 9 
  a partir de los DNI de los usuarios, respecto al conjunto universal definido como x/x ∈ Z y 0<= x <= 9.

  Args:
      List: Con los documentos ingresados por el usuario.

  Returns:
        Bool: True si no es un conjunto vacio y False si es un conjunto vacio.
  """
  x = union(lista_dni) 
  c=[]
  for i in range (10):
    if i not in x:
      c.append(i)

  if c == []:
    return False
  else:
    return True

# Interseccion
def interseccion(dnis: list[int]) -> list[int]:
  if not dnis:
    return []

  conjunto_comun = set(generador_de_conjuntos(dnis[0]))

  for dni in dnis[1:]:
    conjunto_comun.intersection_update(generador_de_conjuntos(dni))

  return list(conjunto_comun)

nacimientos()