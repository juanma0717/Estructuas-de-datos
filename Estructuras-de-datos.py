# En este archivo se van a trabajar las estructuras de datos de Python
# Metodos de las listas
# El metodo append se usa para agregar un elemento al final de la lista
animales = ["perro","gato","loro","mono"]
animales.append("vaca")
print(animales)
#Se va a agregar el elemento "vaca"
# El metodo extend se usa para agegar elementos de una lista a otra
nombres = ["Juan","Mariana","Laura","Sebastian","Alejandra"]
apellidos = ["Jimenez","Torres","Angulo","Chivita","Vargas"]
nombres.extend(apellidos)
print(nombres)
# Los elementos de la lista 'apellidos' se van a agregar a la lista 'nombres'
# El metodo insert se usa para agregar un elemento en la posicion indicada
equipos = ["Bayern","Real Madrid","Barcelona"]
equipos.insert(1,"Liverpool")
print(equipos)
# Se va a insertar el elemento "Liverpool" en la posicion 1 de la lista
# El metodo remove se usa para quitar el primer elemento cuyo valor se especifique
numeros = [1, 2 ,3 ,4 ,56, 5]
numeros.remove(56)
print(numeros)
# Se quita el elemento "56"
# El metodo pop quita el elemento de una posicion dada y lo retorna, en caso de no especificar un indice quita el ultimo elemento de la lista y lo retorna
edad = [18, 25, 40, 30, 12]
edad.pop(2)
print(edad)
# Se quita el elemento "40"
# El metodo clear quita todos los elementos de la lista
verduras = ["Zanahoria", "Cebolla", "Lechuga"]
verduras.clear()
print(verduras)
# La lista queda vacia
# El metodo index retorna la posicion de un elemento
alimentos = ["Pollo","Arroz","Huevo"]
print(alimentos.index("Pollo"))
# Se retorna la posicion de el elemento "Pollo"
# El metodo count cuenta el numero de veces que un elemento indicado aparece en la lista
puntos = [1, 3, 3, 2, 4, 5, 2, 3, 3]
print(puntos.count(3))
# Se cuenta el numero de veces que aparece el elemento "3" en la lista
# El metodo sort retorna la lista segun el orden que se le indique
figuras = ['Triangulo', 'Cuadrado', 'Circulo']
figuras.sort(reverse=False)
print(figuras)
# El orden va a ser alfabetico entonces comenzara por el elemento "Circulo"
# El metodo reverse se usa para invertir los elementos de la lista
paises = ["Serbia", "Croacia", "Bosnia"]
paises.reverse()
print(paises)
# Ahora el orden de la lista ahora comineza por el elemento "Bosnia"
# El metodo copy retorna la copia de una lista
capitales = ["Bogota", "Estocolmo","Paris","Tokyo"]
ciudades = capitales.copy()
print(ciudades)
# Se copian la lista capitales en la variable ciudades
# Listas como pilas
# 1. Se declara la lista
pila = [1, 2, 3, 4, 5, 6]
# 2. Se usa el metodo append para agregar elementos a la cima de las listas
pila.append(7)
pila.append(8)
pila.append(9)
pila.append(10)
# 3. Finalmente se usa el metodo pop para retirar elementos de la lista
pila.pop()
pila.pop()
pila.pop()
# 4. Se imprime la lista
print(pila)
# Con los metodos append y pop se apilan y desapilan listas
# Listas como colas
# 1. Se importa la libreria
from collections import deque
# 2. Se declara la lista
cola = deque([1, 2, 3, 4, 5, 6, 7, 8])
# 3. Se agregan elementos al final de la lista
cola.append(9)
cola.append(10)
cola.append(11)
cola.append(12)
cola.append(13)
# 4. Se quitan los primeros elementos de la lista
cola.popleft()
cola.popleft()
cola.popleft()
cola.popleft()
cola.popleft()
# 5. Se imprime la lista
print(cola)
# Comprension de listas
# Usamos la comprension de listas para crear listas aplicando operaciones en elementos de otras listas
# En este caso usamos bucles para crear elementos en la lista multiplicacion que seran multiplos de 4
multiplicacion = []
for x in range(20):
    multiplicacion.append(x*4)
print(multiplicacion)
# Tambien podemos usar condicionales para esto, en el siguiente ejemplo se muestra como usando condicionales hacemos que solo los elementos de las listas que sean pares se puedan multiplicar
pares = []
numeros1 = [6,7,8,9,10]
numeros2 = [1,2,3,4,5]
for x in numeros1:
    for y in numeros2:
        if x%2==0 and y%2==0:
            pares.append((x*y))
print(pares) 
# Comprension de listas anidadas
# Esto es como su nombre lo dice una comprension de lista anidada dentro de otra comprension de lista
# Para este caso usamos una comprension de lista anidada para de una matriz de 3*4 implementar tres listas, en este caso listas con convinaciones de comida para un menu
comida = [
    ['arvejas', 'lentejas', 'frijoles', 'garbanzos'],
    ['cerdo', 'carne', 'huevo', 'pollo'],
    ['papa', 'platano', 'yuca', 'ñame'],
]
convinacion = []
for i in range(4):
    convinacion.append([row[i] for row in comida])
print(convinacion)
# Instruccion del
# La instruccion del se puede usar para vaciar una lista o quitar ciertos elementos especificando un indice
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
del numeros[3]
# Se puede especificar un grupo de una seccion de elementos a borrar
del numeros[0:2]
# Tambien se puede limpiar la lista
del numeros[:]
print(numeros)
# Tuplas y secuencias
# Las tuplas consisten en elementos separados por comas, diferencia de las listas que tienen secuencias homogeneas y mutables las tuplas son heterogeneas e inmutables sin embargo pueden contener elementos mutables como tuplas
tupla1 = 'perro', 'gato', 1034
print (tupla1)
tupla2 = [1,2,3], 3, 4
print(tupla2)
#Conjuntos
# Son un tipo de datos que son una coleccion no ordenada y sin elementos repetidos, dentro de estos se encuetra el uso de verificacion de pertenencia y eliminacion de entradas dupicadas.
# Estos tambien soportan distintas operaciones matematicas
conjunto1 = {1, 2, 3, 4, 5, 6, 7}
print(1 in conjunto1)
print(10 in conjunto1)
# Tambien se puede crear conjuntos con funcion set ademas esta es la que se usa para crear un conjunto vacio
conjunto2 = set('chao')
print(conjunto2)
# Diccionarios
# Son estructura que nos permiten almacenar elementos como pares clave usando Clave-Valor, las claves de estos diccionarios deben ser unicas, para crear un diccionario vacio solo se ponen las llaves
estudiantes = {'maria': 1032, 'dario':3232,'sofia':3232}
print(estudiantes['maria'])
# Tambien se pueden crear diccionarios usando la funcion dict
fruver = dict([('manzana', 4123231),('lechuga',1232132),('papa', 121232)])
print(fruver['papa'])
# Tecnicas de iteracion
# Para obtener la clave de un diccionario y su valor se puede usar el metodo items
capitales = {'Bogota':'Colombia','Santiago':'Chile','Berlin':'Alemania'}
for a, b in capitales.items():
    print(a, b)
# Cuando se itera sobre una secuencia se puede obtener el indice de la posicion usando el metodo enumerate
colores = ['rojo','azul','verde','amarillo']
for a, b in enumerate(colores):
    print(a, b)
# Cuando se necesita iterar dos o mas secuencias al mismo tiempo de usa la funcion zip
nombre = ['Juan','Laura','Cristian']
pais = ['Colombia','Japon','España']
for a, b in zip(nombre, pais):
    print('My name is {0} and I am from {1}.'.format(a, b))
# Para iterar una secuencia en orden inverso se utiliza la funcion reversed
for i in reversed(range(4,100,4)):
    print(i)
# Para iterar una secuencia con su orden original se usa la funcion sorted
legumbres = ['Lentejas','Frijoles','Arvejas','Garbanzos']
for i in sorted(legumbres):
    print(i)

# El set elimina los elementos repetidos, el uso combinado de el sorted y el set nos permite iterar los elementos unicos
color = ['azul','rojo','azul','verde','amarillo','rojo','amarillo','verde']
for i in sorted(set(color)):
    print(i)

# Otras condiciones
'''
En las condiciones while e if se puede poner cualquier operador no solo de comparaciones.
Las comparaciones se pueden combinar usando operadores booleanos and y or, estos se consideran operadores cortocircuito
'''

# Comparando secuencias y otros tipos
'''
Las secuencias pueden ser comparadascon otros objetos del mismo tipo de secuencia. Esta usa orden lexico grafico
primero se compara los dos primeros elementos, si son diferentes esto determina el resultado de la operacion, si son iguales se comparan los 
dos siguientes elementos y asi sucesivamente.
'''