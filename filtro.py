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



if len(sys.argv) < 2 or len(sys.argv) > 3: 
    print("Debes especificar un umbral y opcionalmente una condición.")
else:
    try:
        umbral =int(sys.argv[1])
    except ValueError:
        print("El umbral debe ser número")
    else:
        condicion = "mayor" if len(sys.argv) == 2 else sys.argv[2].lower()
        if condicion == "mayor":
            productos_filtrados = {producto: precio for producto, precio in precios.items() if precio > umbral}
            print("Los productos mayores al umbral son: ", ",".join(productos_filtrados.keys()))
        elif condicion == "menor":  
            productos_filtrados = {producto: precio for producto, precio in precios.items() if precio < umbral}  
            print("Los productos menores al umbral son:", ', '.join(productos_filtrados.keys()))
        else:
            print("Lo sentimos, no es una operación válida")
