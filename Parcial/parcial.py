# Ejercicio 2
for t in range(1, 3):  # Primer bucle va de 1 a 2
    for i in range(1, 4):  # Segundo bucle va de 1 a 3
        print(t * i, end=" ")  # Multiplicamos los índices para obtener la secuencia deseada

# Ejercicio 3
lista = [0,0,0,0,0,0,0,0,0,0]

lista[0] = 1
lista[1] = 1
lista[2] = 1
lista[3] = 2
lista[4] = 1

n = 5
r = 0

if n == 0:
    r = 0
else:
    r = lista[n-1]
    for i in range(n-1, 0, -1):  # Cambiar el paso a -1
        r += lista[i-1]
print(r)

# Ejercicio 4
f="HolaMundoCruel"
r = f
l = len(f)

for i in range(0, l+1, 5):
    r = f[i:l]

print(r)

# Ejercicio 5
for i in range(1, 11):
    bandera=False
    d=0

    for c in range(1, i+1):
        if i%c==0:
            d+=1
            if d<=2:
                bandera=True
            else:
                bandera=False

    if bandera:
        print(i)

# Ejercicio 6
n = 5
a = [0] * n
b = [0] * n

for i in range(n):
    a[i] = i+i+i

for i in range(n):
    b[i] = i*2

contador=0

for i in range(n):
    if a[0] == a[i] and a[0] == b[i]:
        contador += 1
        n = n - contador

resultado = str(contador)

if a[0] == 1:
    resultado = "VERDADERO"
elif a[0] == 2:
    resultado = "2"
elif a[0] == 3:
    resultado = "FALSO"

print(resultado)