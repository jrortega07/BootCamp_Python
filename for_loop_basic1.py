print("Básico : imprime todos los enteros del 0 al 150.")
for x in range(151):
    print(x)

print(" ")
print("Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000.")
for x in range(0, 1001, 5):
    print(x)

print(" ")
print('Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".')
for x in range(1, 101, 1):
    if (x % 10 == 0):
        print("Coding Dojo")
    elif (x % 5 == 0):
        print("Coding")
    else:
        print(x)

print(" ")
print("¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.")
suma = 0
for x in range(0, 500001, 1):
    if (x % 2 != 0):
        suma = suma + x
print(" ")
print("La suma total de los número impares entre 0 y 5000 es: ", suma)
print(" ")

print("Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.")
for x in range(2018, 0, -4):
    print(x)

print("""Contador flexible : establece tres variables: lowNum, highNum, mult. 
Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. 
Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)""")
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, (highNum+1), 1):
    if( x % mult == 0):
        print(x)

print(" ")
print("¿Como detectar si un número entre 1 y 1000 es primo?")
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print(num, "No es primo", n, "es divisor")
            return False
    print(num, "Es primo")
    return True
for x in range(1, 1001, 1):
    es_primo(x)