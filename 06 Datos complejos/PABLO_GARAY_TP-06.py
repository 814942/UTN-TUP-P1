from collections import deque
import math

# 1-  Dado el diccionario precios_frutas, Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2- Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3- Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
frutas: list[str] = list(precios_frutas.keys())

print(frutas)
print(precios_frutas)

# 4- Crear una clase llamada Persona que contenga un método __init__ con los atributos
# nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un
# mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad] años."
class Persona:
    def __init__(self, nombre, pais, edad) -> None:
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self) -> None:
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

usuario_pablo = Persona("Pablo", "Argentina", 23)
print(usuario_pablo.saludar())

# 5- Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
# calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
class Circulo:
    radio: float = 0.0

    def __init__(self, radio) -> None:
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * self.radio ** 2

    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.radio

circulo = Circulo(20)
print(f"El area del circulo es: {circulo.calcular_area():.2f}")
print(f"El perimetro del circulo es: {circulo.calcular_perimetro():.2f}")

# 6- Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente balanceados usando una pila.
def estaBalanceado(cadena: str) -> bool:
    stack: list[str] = []
    pares: dict[str, str] = {"(": ")", "{": "}", "[": "]"}

    for i in range(len(cadena)):
        if cadena[i] in pares:
            stack.append(cadena[i])
        elif not stack or pares[stack.pop()] != cadena[i]:
            return False
    return not stack

estaBalanceado("({[})") # False
estaBalanceado("({[]})") # True

# 7- Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir: 
# Agregar clientes (encolar).
# Atender clientes (desencolar).
# Mostrar el siguiente cliente en la fila
class Turnero:
    def __init__(self):
        self.clientes = deque()

    def encolar(self, cliente):
        self.clientes.append(cliente)

    def desencolar(self):
        return self.clientes.popleft() if not self.esta_vacia() else "La cola está vacía"

    def siguiente(self):
        return self.clientes[0] if not self.esta_vacia() else "La cola está vacía"

    def esta_vacia(self):
        return len(self.clientes) == 0

cola = Turnero()
cola.encolar("Cliente 1")
cola.encolar("Cliente 2")
cola.encolar("Cliente 3")
print(cola.siguiente())
print(cola.esta_vacia())
print(cola.desencolar())
print(cola.desencolar())
print(cola.desencolar())
print(cola.esta_vacia())
print(cola.desencolar())

# 8-  Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar los valores almacenados.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' ➡️ ')
            actual = actual.siguiente
        print("Fin")

# 9- Dada una lista enlazada, implementa una función para invertirla
    def invertir_lista(self):
        stack: list = []
        actual = self.cabeza
        while actual:
            stack.append(actual.dato)
            actual = actual.siguiente

        self.cabeza = None
        while stack:
            self.insertar(stack.pop())
        print("Fin")

lista = ListaEnlazada()
lista.insertar(3)
lista.insertar(2)
lista.insertar(1)
lista.mostrar()
lista.invertir_lista()
lista.mostrar()