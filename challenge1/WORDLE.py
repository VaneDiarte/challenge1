# Wordle challenge

# Se define la funcion
def verificar_fila (palabra_a_encontrar, palabra_ingresada):

    letras_verificadas = []


    # Se utiliza un bucle for para recorrer las letras en la palabra  
    for posicion_letra in range(len(palabra_ingresada)):

        # Se definen las variables que guardan los datos 

        # Si las letras son iguales
        las_letras_son_iguales = palabra_a_encontrar[posicion_letra] == palabra_ingresada[posicion_letra]

        # Si las letras existen en la palabra
        las_letras_existen = palabra_ingresada[posicion_letra] in palabra_a_encontrar


        # Se utiliza una condicional para agregar las letras a la lista vacia creada al principio
        if las_letras_son_iguales: #si las letras son iguales se agrega a la lista y se las encierra en []
            letras_verificadas.append(f"[{palabra_ingresada[posicion_letra]}]")

        elif las_letras_existen: #si las letras son iguales se agrega a la lista y se las encierra en ()
            letras_verificadas.append(f"({palabra_ingresada[posicion_letra]})")

        else: #caso contrario, se agrega a la lista sin modificar nada
            letras_verificadas.append(palabra_ingresada[posicion_letra])
    
    # Retornamos nuestro resultado en la lista vacia creada
    return letras_verificadas





palabra_secreta = "vanessa"
intentos = 6
cantidad_de_letras = 7

grilla = []

print ('Bienvenidos al WORDLE, escribe una palabra con 7 letras')

while intentos >0:
    print (f'Tienes {intentos} intentos')
    palabra_usuario = input("Ingrese una palabra ")
    intentos -= 1

    if len(palabra_usuario) != cantidad_de_letras:
        print ('Ingrese una palabra con 7 letras')
        continue
    else:
        linea_verificada = verificar_fila (palabra_secreta, palabra_usuario)
        grilla.append(linea_verificada)
        print ('El estado actual del WORDLE: ')
        for fila in grilla:
            print(' '.join(fila))
    if palabra_usuario == palabra_secreta:
        print ('GANASTE')
        break

    























