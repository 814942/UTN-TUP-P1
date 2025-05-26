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
  