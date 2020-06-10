dicc = {'a':55, 22:"Esto es texto o string", 'a':125}
dicc['c']="Nicole no te ama"

del dicc['c']

value= dicc.get('z', "No existe esa clave")

llaves= list(dicc.keys())
print(llaves)
print(dicc)