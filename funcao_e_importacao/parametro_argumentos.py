def somar_dois(n):
    return n + 2

x = 10

resultado = somar_dois(x)
print(resultado)

def adicionar_final(texto, final='!!!'):
    return texto + final

print(adicionar_final('Olá'))

def dividir(a, b):
    if b == 0:
        return 'Impossivel de Dividir'
    return a / b

print(dividir(a=10, b=2))
