JUAN = 23089140
ISRAEL = 19118232
CRISTIAN = 35550208
FELIPE = 32313489
PABLO = 33814942

# Lista de DNIs
dnis = [JUAN, ISRAEL, CRISTIAN, FELIPE, PABLO]

# Generación automática de los conjuntos de dígitos únicos.
def generador_de_conjuntos(dni: int):
  conjuntos: list[int] = []
  for i in range(10):
    if str(i) in str(dni):
      conjuntos.append(i)

  return conjuntos

def interseccion(dnis: list[int]) -> list[int]:
  if not dnis:
    return []

  conjunto_comun = set(generador_de_conjuntos(dnis[0]))

  for dni in dnis[1:]:
    conjunto_comun.intersection_update(generador_de_conjuntos(dni))

  return list(conjunto_comun)

# Mostrar resultado de la intersección
resultado = interseccion(dnis)
print("Dígitos en común entre todos los DNIs:", sorted(resultado))