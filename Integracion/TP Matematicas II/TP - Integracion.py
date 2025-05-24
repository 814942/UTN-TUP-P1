JUAN: int = 23089140
ISRAEL: int = 19118232
CRISTIAN: int = 35550208
FELIPE: int = 32313489
PABLO: int = 33814942

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

def union(dnis: list[int]) -> list[int]:
  if not dnis:
    return []

  conjunto_unico = set()
  for dni in dnis:
    conjunto_unico.update(generador_de_conjuntos(dni))

  return list(conjunto_unico)