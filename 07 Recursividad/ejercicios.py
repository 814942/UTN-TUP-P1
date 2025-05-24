# Factorial
def factorial(num: int) -> int:
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# print(factorial(4))

# Suma recursiva
def sum_factorial(nums: list[int]) -> int:
    if (len(nums) == 0):
        return 0
    else:
        return sum_factorial(nums[1:]) + nums[0]

# print(sum_factorial([5,2,3,8]))

# Repetir frase
def rep_factorial(frase: str, num: int) -> str:
    if num == 1:
        return frase
    else:
        return rep_factorial(frase, num - 1) + "\n" + frase

print(rep_factorial("Hola", 4))

# Sucesion Fibonacci - 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
def fibonacci(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(10))

# Sumar los n primeros numeros
def suma_recursiva(num):
    if num == 0:
        return 0
    else:
        return num + suma_recursiva(num - 1)

print(suma_recursiva(5))