def factorial_numero(n):
    factorial=1
    while n>0:
        factorial=factorial*n
        n-=1
    return factorial

r=factorial_numero(5)
print(r)