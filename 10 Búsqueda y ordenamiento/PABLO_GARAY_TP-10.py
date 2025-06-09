import random
import string
import time

randomList = random.sample(range(1, 100), 5)

# Swap aux
def swapping(list, indiceActual, indiceSiguiente):
  list[indiceActual], list[indiceSiguiente] = list[indiceSiguiente], list[indiceActual]

# Bubble sort - Ordenamiento burbujeo
# Compara los elementos adyacentes y los intercambia si estan desordenados
# Repite el proceso hasta que la lista esté ordenada
#      >                      >                      >
#  [5, 2, 8, 1, 9] --> [2, 5, 8, 1, 9] --> [2, 5, 8, 1, 9] --> [2, 5, 1, 8, 9] ...
def bubbleSort(list):
  print("Inicio del burbujeo...")
  inicio_binaria = time.time()
  for i in range(len(list)):
    for j in range(len(list) - 1):
      if list[j]["precio"] > list[j + 1]["precio"]:
        swapping(list, j, j + 1)

  fin_binaria = time.time()
  print(f"Tiempo de busqueda binaria: {fin_binaria - inicio_binaria}")
  return list

def bubbleSortV2(list):
  print("Inicio del burbujeo optimizado...")
  inicio_binaria = time.time()
  swapped: bool = True

  while swapped:
    swapped = False
    for i in range(len(list) - 1):
      if list[i]["precio"] > list[i + 1]["precio"]:
        swapping(list, i, i + 1)
        swapped = True  

  fin_binaria = time.time()
  print(f"Tiempo de busqueda binaria: {fin_binaria - inicio_binaria}")
  return list

# Selection sort - Ordenamiento por seleccion
# Busca el mas pequeño y lo intercambia por el primero
# Continua recorriendo la lista hasta que este completamente ordenada
#           x    swap  x
# [5, 2, 8, 1, 9] --> [1, 2, 5, 8, 9]
def selectionSort(list):
  for i in range(len(list)):
    min_index = i
    for j in range(i + 1, len(list)):
      if list[j] < list[min_index]:
        min_index = j
    swapping(list, i, min_index)

  return list

def selectionSortV2(list):
  for i in range(len(list)):
    min_index = i
    for j in range(i + 1, len(list)):
      if list[j] < list[min_index]:
        min_index = j
    if min_index != i:
      swapping(list, i, min_index)

  return list

# Insertion sort - Ordenamiento por insercion
# Claw machine - La Maquina de peluches
# Al igual que la maquina toma cada peluche con su garra y lo "reubica" en la posicion correcta.
# Toma el menor, como la garra de la maquina, y lo coloca en la posicion adecuada.
#    claw             claw
#     |                |
#     2                2
# [5, 2, 8, 1, 9] --> [5, 5, 8, 1, 9] --> [2, 5, 8, 1, 9]
def insertionSort(list):
  for i in range(1, len(list)):
    j = i - 1
    min_value = list[i]
    while j >= 0 and list[j] > min_value:
      list[j + 1] = list[j]
      j -= 1
    list[j + 1] = min_value

  return list

# Merge sort - Ordenamiento por mezcla
# Divide la lista en dos mitades, hasta que quede dos arrays de un elemento
# Ordena cada mitad
# Mezcla las dos mitades
#                 [8,3,5,4,7,6,1,2] --> Dividimos hasta que cada valor se encuentre en un array.
#         [8,3,5,4]              [7,6,1,2]
#     [8,3]       [5,4]       [7,6]      [1,2]
#   [8]   [3]   [5]   [4]   [7]   [6]  [1]   [2]
# --- Ordernar y Fusionar. Compara cada subconjunto y lo ordena de menor a mayor ---
#     [3,8]       [4,5]       [6,7]       [1,2]
#         [3,4,5,8]               [1,2,6,7]
#                 [1,2,3,4,5,6,7,8]
def mergeSort(list, is_outer_call=True):
  if is_outer_call:
    print("Inicio de la fusion...")
    inicio_binaria = time.time()
  if len(list) > 1:
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    mergeSort(left, False)
    mergeSort(right, False)
    i = j = k = 0
    while i < len(left) and j < len(right):
      if left[i]["precio"] < right[j]["precio"]:
        list[k] = left[i]
        i += 1
      else:
        list[k] = right[j]
        j += 1
      k += 1
    while i < len(left):
      list[k] = left[i]
      i += 1
      k += 1
    while j < len(right):
      list[k] = right[j]
      j += 1
      k += 1

  if is_outer_call:
    fin_binaria = time.time()
    print(f"Tiempo de busqueda binaria: {fin_binaria - inicio_binaria}")
  return list

# Quick sort - Ordenamiento por quick
# Tomamos un elemento al azar como pivot
# Ordenamos a la izquierda los valores menores
# y a la derecha los valores mayores
# [4, 8, 2, 1, 5, 7, 6, 3] --> Tomamos un pivot de forma aleatoria --> 4.
# [3, 2, 1, 4, 5, 7, 6, 8] --> Ahora tenemos ubicado el 4 en su posicion final.
# Ahora el pivot sera pivot --> 3.
# [1, 2, 3, 4, 5, 7, 6, 8] --> Ubicamos el 3 en su posicion final. Tomamos un nuevo pivot...
def quickSort(list):
  if len(list) <= 1:
    return list
  pivot = list[0]

  left = []
  right = []

  for i in range(1, len(list)):
    if list[i] < pivot:
      left.append(list[i])
    else:
      right.append(list[i])

  return quickSort(left) + [pivot] + quickSort(right)

def quickSortV2(list, low=0, high=None):
  if high is None:
    high = len(list) - 1

  if low < high:
    pivot_index = partition(list, low, high)
    # hacia la izquierda
    quickSortV2(list, low, pivot_index - 1)
    # hacia la derecha
    quickSortV2(list, pivot_index + 1, high)

  return list

def partition(list, low, high):
  pivot = list[high]
  i = low - 1

  for j in range(low, high):
    if list[j] <= pivot:
      i += 1
      swapping(list, i, j)

  swapping(list, i + 1, high)
  return i + 1

# Busqueda lineal
def busqueda_lineal(lista, objetivo: int):
  for i in range(len(lista)):
    if lista[i] == objetivo:
      return i
  return -1

# Busqueda binaria
def busqueda_binaria(lista, objetivo: int):
  izquierda, derecha = 0, len(lista) - 1
  while izquierda <= derecha:
    medio = (izquierda + derecha) // 2
    precio_redondeado = round(lista[medio]["precio"])

    if precio_redondeado == objetivo:
      return lista[medio]
    elif precio_redondeado < objetivo:
      izquierda = medio + 1
    else:
      derecha = medio - 1
  return -1

# CASO PRACTICO
def generar_producto():
    # Generar un nombre aleatorio de 5-10 caracteres
    nombre = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10))).capitalize()
    # Generar un precio aleatorio entre 10.00 y 1000.00
    precio = round(random.uniform(10.0, 1000.0), 2)
    return {"nombre": nombre, "precio": precio}

def encontrar_productos():
  cantidad_producto = int(input("Ingrese la cantidad de productos que quiere generar: "))
  # Genera una lista de n cantidad de productos aleatorios
  lista_productos = [generar_producto() for _ in range(cantidad_producto)]
  # Se ordena con el algoritmo mas eficiente
  lista_ordenada = mergeSort(lista_productos)

  precio_producto = int(input("Ingrese el precio del producto a buscar: "))

  # Buscar con busqueda binaria
  producto = busqueda_binaria(lista_ordenada, precio_producto)
  if producto == -1:
    print("Producto no encontrado")
  else:
    print(producto)

encontrar_productos()