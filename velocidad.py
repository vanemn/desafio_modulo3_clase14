#lista proporcionada
velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

#funcion promedio mayor a 
def promedio(velocidad):
    #obtener promedio
    avg = sum(velocidad) / len(velocidad)
    print(f'El promedio es: {avg}')
    print(f'Los valores mayores al promedio son: ')
    #generar una lista nueva
    mayores = []
    #iterar para añadir los mayores al promedio
    for num in velocidad:
        if num>avg:
            mayores.append(num)
    #ordenar de menor a mayor
    mayores.sort()

    print(mayores)
    
#inicializar funcion
promedio(velocidad)
