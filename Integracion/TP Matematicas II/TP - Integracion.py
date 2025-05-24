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

def union(dnis: list[int]) -> list[int]:
  if not dnis:
    return []

  conjunto_unico = set()
  for dni in dnis:
    conjunto_unico.update(generador_de_conjuntos(dni))

  return list(conjunto_unico)

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


def complemento_U(lista_dni)-> bool:
  x = union(lista_dni) 
  c=[]
  for i in range (10):
    if i not in x:
      c.append(i)
  if c == []:
    return False
  else:
    return True










if __name__ == "__main__":
  #list_dni=[23089140, 19118232, 35550208, 32313489, 33814942]
  list_dni=[23089140, 19118232, 35550208, 32313489, 33814942, 12678912]
  #print(f"La diferencia del conjunto A - B es igual a {dif_conjuntos()}")
  
  print(f"La diferencia del conjunto A - B es igual a {dif_conjuntos_op1(list_dni)}")
  
  print(f"Es {complemento_U(list_dni)} que el complemento de X no es un conjunto vacio")


"""
JUAN J: 23089140
ISRAEL I: 19118232
CRISTIAN C: 35550208
FELIPE F: 32313489
PABLO P: 33814942

"""