import sys
precios = {
    "notebook": 700000,
    "teclado": 25000,
    "mouse": 12000,
    "monitor": 250000,
    "escritorio": 135000,
    "tarjeta de video": 1500000
}
if len(sys.argv) < 2 or len(sys.argv) > 3: 
    print("Debes especificar un umbral y opcionalmente una condición.")
else:
    try:
        umbral =int(sys.argv[1])
    except ValueError:
        print("El umbral debe ser número")
    else:
        condicion = "mayor" if len(sys.argv) == 2 else sys.argv[2].lower()