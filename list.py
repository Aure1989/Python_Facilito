# #formas de crear una lista

# #almacenandola en una variable
# my_list=[5,4,3,'texto']

# #con un constructor 'list'
# numbers_list=list((1,2,3,4,5))#pasando 5 argumentos, pero com un grupo gracias a una tupla
# print(numbers_list)

# #creando una lista a partir de un rango (range)
# r=list(range(1,10))#solo imprime hasta una posición antes de la cifra final del rango
# print(r)

#colors=['blue', 'red', 'yellow']
# print(type(colors))
# print(len(colors))
# print('red' in colors)

# print(colors)
# colors[1]='green' #reemplazar un elemento en la lista
# print(colors)

# #colors.append('violet')#permite agregar 1 elemento a la lista
#permite agregar varios elementos, pero debe recibirlos como tupla o lista
# colors.extend(['purple', 'red', 'black'])
# print(colors)

#insertar un elemento en una posición específica
# colors=['blue', 'red', 'yellow']
# print(colors)
# colors.insert(1,'black')
# print(colors)

# colors=['blue', 'red', 'yellow']
# #al usar len obtengo un número, siendo esta la posición (final)
# #dónde se añadirá el nuevo elemento 'violet'
# colors.insert(len(colors),'violet')
# print(colors)

# #quitar el último elemento
# colors.pop() #puedo especificar una posición dentro del paréntesis
# print(colors)

# #remover
# colors.remove('red')
# print(colors)

# #puedo remover todo de la lista con 'clear'
# colors.clear()
# print(colors)

colors=['blue', 'red', 'yellow']
#sort para ordenarlos
# colors.sort() #sort(reverse=True) para ordenar a la inversa
#conocer la posición o ndice
print(colors.index('red'))


colors2=['blue', 'red', 'yellow','red','red']
#contar cuantas veces se repite un elemento
print(colors2.count('red'))