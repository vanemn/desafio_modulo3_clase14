# Estructuras de datos y funciones (II)

Este proyecto contiene tres proyectos que pretenden validar nuestros conocimientos utilizando las distintas propiedades y funciones en Python.

## 1- Filtrado relevante filtro.py

Una empresa tiene un contrato con una tienda de tecnología en la cual quieren implementar
un filtrado por precio. 

### Descripción

Dada una muestra de los productos que actualmente se encuentran disponibles
en la tienda (un diccionario), se implementa una función que entrega lo
siguiente:
● Un diccionario con los productos que cumplen una cierta condición dado un umbral
● La función permite mostrar los valores mayor que o menor que un umbral
(siempre estrictos).
● Por defecto la función siempre muestra los valores mayor que el umbral a
menos que se indique lo contrario.
● Los argumentos se especifican de la siguiente manera:

python filtro.py 30000

Al indicar el umbral, por defecto debe calcular
los que son estrictamente mayores al umbral.

python filtro.py 30000 menor

Mostrará los productos menores al umbral 

En caso que otro elemento se utilice se indicará lo siguiente:
Lo sentimos, no es una operación válida


## 2- Alertas telemáticas velocidad.py

Se realiza proyecto para una empresa de flotas que debe medir mediante telemetría las velocidades de cada una de sus correas transportadoras. Una de sus políticas es distribuir su energía de manera eficiente, por lo que, para poder entregar energía a las correas más lentas, es necesario ralentizar las más rápidas, para asegurar una correcta distribución de la energía disponible.

### Descripción

● Para determinar una funcionalidad que calcule el promedio de una lista de velocidades. El servidor donde se pretende instalar esta funcionalidad no cuenta con mucha capacidad por lo que se pide no depender de librerías externas.
● Se enlistaron las posiciones de todas las correas transportadoras que están sobre el
promedio.


## 3- Apoyo matemático ong.py

Se realiza proyecto para la empresa que les presta soporte a las ONG. 

### Descripción

En un programa de ayuda escolar que tiene la esta ONG se está enseñando a programar algunas operaciones
avanzadas a niños con alto potencial pero de escasos recursos. Se abordaron dos
operaciones conocidas como el factorial y la productoria.

El factorial se define de la siguiente forma:
𝑛! = 𝑛 * 𝑛 − 1 * 𝑛 − 2 * ... * 2 * 1

Por otro lado la productoria se define como la multiplicación de elementos.
𝐴 = [3, 6, 4, 2, 8]
∏ 𝐴
𝑖 = 3 * 6 * 4 * 2 * 8

Se crea un script llamado ong.py que contiene las siguientes funciones:

○ Una función que calcula el factorial.
○ Una función que calcula la productoria.
○ Una función que permite controlar los cálculos. Esta función permite invocar
de la siguiente manera:

calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)

Se ingresarán un valor numérico como argumento con el nombre fact_i cuando se requiera
calcular un factorial, y una lista como argumento prod_i cuando se requiera calcular una
productoria. La función permite ingresar estos argumentos en
cualquier orden y en cualquier cantidad. 

## Prerrequisitos o Dependencias

Sistema Operativo Windows, Linux, MacOS
Lenguaje de programación Python 3.12

## Instalación del Proyecto

Clonar el repositorio:

```bash
# git@github.com:vanemn/desafio_modulo3_clase14.git
```



Ingresar a la carpeta del proyecto:

```bash
# desafio_modulo3_clase14
```

Elegir el programa a usar:

filtro.py
velocidad.py
ong.py


Autor
- [Vanessa Morales](https://github.com/vanemn)
- [Benjamin Pardo](https://github.com/bpardo02)
- [Andres Gallardo](https://github.com/AndresGallardo95)
- [Camila riquelme](https://github.com/camilariquelme)
- [Nicole Pinilla](https://github.com/Npinilla19)

