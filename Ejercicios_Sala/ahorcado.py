# Variables
palabraAdivinar = ''
adivinar= []
PalabraMost = []
intentos = 5
letra = ''
run = True

# Logica

## Pedimos la palabra a adivinar
print('AHORCADO')
palabraAdivinar=open('C:\\Users\\SALA\\Desktop\\ahorcado\\palabras.txt','r')

## Separamos la palabra en letras
adivinar=(palabraAdivinar)

for item in palabraAdivinar:
    PalabraMost.append('_')

def new_func(adivinar, PalabraMost, intentos, letra):
    if letra not in adivinar:
        ## Ha fallado
        fallo = True
        intentos = intentos - 1
        print('Has fallado!!!! Te quedan {intentos} intentos'.format(intentos=intentos))
    else:
        ## Adivinado, sustituimos
        for key, value in enumerate(adivinar):
            if value == letra:
                PalabraMost[key] = value

    ## Comprueba si ha terminado la partida
    ### Se le acaban los intentos
    return intentos

while run:
    ## Mostramos la palabra a adivinar
    print(' '.join(PalabraMost))

    ## Pedimos una letra
    letra = str(input('Dame una letra: '))

    ## Limpiar pantalla
    for num in range(100):
        print()

    ## Comprueba si se ha equivocado
    fallo = False

    intentos = new_func(adivinar, PalabraMost, intentos, letra)
    if intentos <= 0:
        run = False
        print('Has perdido, la palabra ''era"{palabra}"'.format(palabra=''.join(adivinar)))
    elif adivinar == PalabraMost:
        run = False
        print('Has ganado, la palabra '
              'era "{palabra}"'.format(palabra=''.join(adivinar)))