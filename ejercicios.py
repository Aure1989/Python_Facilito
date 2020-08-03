##1.Información sobre la versión##
# # import sys
# print(sys.version)
# print(sys.version_info)


##2.Ejercicios de print##
# print('Lorem Ipsum is simply dummy text of the')
# print('Lorem Ipsum is simply dummy text of the', end=' ')#elimina salto de línea

# print('python3', 'es', 'tremendo')
# print('python3', 'es', 'tremendo', sep='-')#añade un separador

#print('{} es {}'.format('python3', 'la polla'))

##3.Obtener fecha y hora del sistema##
# import datetime
# ahora= datetime.datetime.now()
# print(ahora)

# print(type(ahora))

# print(ahora.strftime('%d/%m/%y %H:%M:%S'))


##4.pedir el valor del radio de un círculo para calcular su área##
# from math import pi 
# r=float(input('Ingresa el radio del círculo: '))
# area = pi*r**2

# print('El area del círculo es {}'.format(area))


##5.Conseguir la representación inversa de una cadena de caracteres##
#Ex Python >> nohtyP
# cadena='python'
# for i in range(len(cadena)-1,-1,-1): #Aquí recorremos cada elemente mediante un for
#     print(cadena[i], end=" ")

# print(cadena[::-1]) #este método es mucho más sencillo


##6.Obtener conjunto de numeros separados por coma y crear una lista##
# entrada=input('Escribe números separados por coma: ') 
# numeros=entrada.split(',')
# print(type(numeros))
# print(numeros)

# entrada=input('Escribe números: ') 
# lista=list(entrada)
# print(type(lista))
# print(lista)