def decorator(func):
    def new_func(*args,**kwargs):
        print("Ejecutar función")
        resultado=func(*args,**kwargs) 
        print("Función ejecutada")
        return resultado
    return new_func


@decorator
def suma(n1,n2):
    return n1+n2

resultado2=suma(25,5)
print(resultado2)