# #Operaciones básicas, como obtener un decimal o entero

# #decimal
# print(5/2)
# print (5*2.1)

# #entero
# print (5//2) #// devuelve un entero
# print (5%2) #Operador de módulo, me permite obtener el residuo

age = input ("Coloca tu edad: ")
#por defecto se considera string (input), por eso la aclaración
new_age = int(age)+10 
print (new_age)