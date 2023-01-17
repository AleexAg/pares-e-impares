import random
random.seed(192131)  #ENTREGA SIEMPRE LOS MISMOS NUMEROS   (NO ES NECESARIO, SOLO ESTA PARA PROBAR)

def principal():
    pares = []
    impares = []
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in numeros:
        numero = random.randint(1, 100) #GENERA UN NUMERO ENTRE 1 Y 1000
        multi = i * numero
        if multi % 2 == 0:
            print(f'{i} x {numero} = {multi}')
            pares.append(multi)  #AGREGA EL RESULTADO A PARES
        else:
            print(f'{i} x {numero} = {multi}')
            impares.append(multi) #AGREGA EL RESULTADO A IMPARES

    print("LISTA DE NUMEROS PARES:", pares)
    print("LISTA DE NUMEROS IMPARES:", impares)

if __name__ == '__main__':
    principal()
