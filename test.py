my_string ="Lorem Ipsum is simply dummy text of the printing and typesetting industry."
text= "Cod Facilito"

#métodos para dar formato
result= '{x} conectando {y}'.format(y=my_string,x=text)
result= result.title()
print(result)

#métodos de búsqueda
po= result.count('s')
print(po)

new= result.replace('s','x')
new= result.split(' ')
print(new)