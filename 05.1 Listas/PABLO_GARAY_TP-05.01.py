# TP 5.1 Listas - Pablo Garay

# 1- Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
nums: list[int] = list(range(4, 101, 4))
print(nums)

# 2- Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.
my_list: list[str] = ["💻", "🌐", "💾", "🔌", "📡"]
print(my_list[-2])

# 3- Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla
empty_list: list[str] = []
empty_list.append("Uno")
empty_list.append("Dos")
empty_list.append("Tres")
print(empty_list)

# 4- Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla.
animales: list[str] = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

# 5- Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# Crea una lista numerica desordenada
numeros = [8, 15, 3, 22, 7]
# Remueve el maximo valor dentro de la lista "numeros"
numeros.remove(max(numeros))
# Imprime por pantalla
print(numeros)
# Remueve el valor maximo de una lista dada.

# 6- Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
nums: list[int] = list(range(10, 31, 5))
print(nums[:2])

# 7- Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "fiesta"
autos[2] = "peugeot"
print(autos)

# 8- Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
dobles: list[int] = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

# 9-  Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[-1].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

# 10- Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
