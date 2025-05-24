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