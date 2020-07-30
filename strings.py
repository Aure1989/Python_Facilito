my_string='Hello-World'

#print(dir(my_string)) la palabra reservada dir nos muestra lo que podemos
#hacer con cierto tipo de dato

# print(my_string.upper()) #el método upper convierte el texto a mayúscula
# print(my_string.title())
# print(my_string.swapcase())
# print(my_string.capitalize()) #Solo la primera letra del string cambia a mayúscula

# print (my_string.replace('Hello','bye')) #replace solo sirve si se escribe igual

# print(my_string.split('-'))#puedo indicarle a este método que usará como separador

# print(len(my_string))#longitud del string

# print(my_string.isnumeric())

print (my_string[4:8])
print (my_string[-3])

print (f'My name is {my_string}') #f indica que lo que esta entre {} es una variable previa
print ('My name is {}'.format(my_string))