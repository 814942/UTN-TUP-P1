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
  
  # Diferencia de dos conjuntos A - B


def dif_conjuntos():
  """
    Realiza la diferencia de dos conjuntos A y B, solicitando al usuario dos números de DNI:


    Args:
        No recibe.


    Returns:
        List: conjunto formado por la diferencia de A - B
  """


  dni = int(input("Ingrese el  1er. DNI para el conjunto A: "))
  a = generador_de_conjuntos(dni)
  dni = int(input("Ingrese el  2do. DNI para el conjunto B: "))
  b= generador_de_conjuntos(dni)
  d=[]
  for i in range(len(a)):
    if a[i] not in b:
      d.append(a[i])
  return d


# Opcion al codigo anterior, es recibiendo una lista con los DNI


def dif_conjuntos_op1(lista_dni: list):
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


# El complemento del conjunto X, siendo X= J ∪ I ∪ C ∪ F ∪ P, respecto al conjunto universal
# definido como x/x ∈ Z y 0<= x <= 9, no es un conjunto vacío.


def complemento_U(lista_dni):
  X = union_de_conjuntos(lista_dni) # reemplazar por el nombre de la función union que hizo Pablo












if __name__ == "__main__":
  print(f"La diferencia del conjunto A - B es igual a {dif_conjuntos()}")
  print(f"La diferencia del conjunto A - B es igual a {dif_conjuntos_op1([35550208, 23089140])}")
