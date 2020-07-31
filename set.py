colors={'red','green','blue','yellow'}
# print('red' in colors)
# print(type(colors))

# #Al no contar con una key y al no ser una lista, el valor se
# # agrega a cualquier posición
# colors.add('purple')

#podemos eliminar los elementos de un set con clear
#tambien podemos eliminar el set con del
colors.clear()
del colors
print(colors)#nos da un error pues ya no existe