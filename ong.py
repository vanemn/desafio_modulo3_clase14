def factorial(n):
    #Calcula el factorial de numero positivo n
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


def productoria(numeros):
    #calcula la productoria de una lista de numeros
    producto = 1
    #iterar en la lista
    for numero in numeros:
        producto *= numero
    return producto

#funcion que procesa ambas funciones anteriores y devuelve el valor impreso
def procesar(fact_i=None, prod_i=None):
    if fact_i is not None:
        print(f"El factorial de {fact_i} es {factorial(fact_i)}")
    if prod_i is not None:
        print(f"La productoria de {prod_i} es {productoria(prod_i)}")


procesar(fact_i=5)
procesar(prod_i=[4, 6, 7, 4, 3])
procesar(fact_i=6)