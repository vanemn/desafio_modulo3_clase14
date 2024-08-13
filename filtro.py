import sys
precios = {
    "Notebook": 700000,
    "Teclado": 25000,
    "Mouse": 12000,
    "Monitor": 250000,
    "Escritorio": 135000,
    "Tarjeta de video": 1500000
}

def filtrado_por_precio(precios, umbral, condicion):
    if condicion == "mayor":
        return {producto: precio for producto, precio in precios.items() if precio > umbral}
            
    elif condicion == "menor":  
        return {producto: precio for producto, precio in precios.items() if precio < umbral}  
        
    else:
        return "Lo sentimos, no es una operación válida"


def resultado_errores():
    if len(sys.argv) < 2: 
        print("Debes especificar un umbral y opcionalmente una condición, ejemplo python filtro.py umbral(valor) mayor/menor")
        return

    try:
        umbral =int(sys.argv[1])
    except ValueError:
        print("El umbral debe ser número")
        return

    
    condicion = 'mayor'
    if len(sys.argv) == 3:
        condicion = sys.argv[2].lower()

    precio_filtrado = filtrado_por_precio(precios, umbral, condicion)

    if isinstance(precio_filtrado, str):
        print(precio_filtrado)
    else:
        productos = ', '.join(precio_filtrado.keys())
        if condicion == 'mayor':
            print(f"Los productos mayores al umbral son: {productos}")
        elif condicion == 'menor':
            print(f"Los productos menores al umbral son: {productos}")

if __name__ == "__main__":
    resultado_errores()



