#  Terminando el juego de la serpiente aplicando fucniones

import os
import random


filas = 10
columnas = 20
serpiente = [[7,5],[7,4],[7,3]] # [Fila, Columna]
comida = [2,10]
direccion = "D" # Empieza moviendose a la derecha la serpiente es el movimiento inicial
juego = True

def dibujar_tablero(): # En esta funcion estoy dando las dimensiones del tablero de juego de la serpiente
    for i in range(filas):
        for j in range(columnas):
            if[i,j]==comida:
                print ("F",end = "") # F Es es simbolo que le di a la comida 
            elif[i,j] in serpiente:
                print("O", end= "") # O Es es cuerpo de la serpiente 
            else:
                print(".", end= "") # Aqui estoy dando al dimension del tablero con puntos es por donde la serpiente correra
        print()
def leer_movimiento(): # Aqui estoy denominando las teclas que va ha tener que utilizar el jugador 
    global direccion, juego
    print("W = arriba, S = abajo, A = izquierda, D = derecha") # Imprimo aqui las especificaciones del juego con respecto a lso controles
    movimiento = input("Movimiento: ").upper() # El upper hace que cualquier letra que ingrese el jugador no importa sea minuscula o mayuscula
    if movimiento in ["W", "A", "S", "D"]:
        direccion = movimiento 
    else :
        print("Letra no valida") # Aqui en un caso qeu no sea una letra que no estipule       
def mover_serpiente(): # Aqui ya le doy movimiento de la serpiente cada vez que el usuario digite una letra la serpiente se mueva
    cabeza = serpiente[0].copy()
    if direccion == "W":# Esta letra es para subir restandole un puesto 
        cabeza[0] -= 1
    elif direccion == "S": # Esta letra es para bajar sumandole un puesto 
        cabeza[0] += 1
    elif direccion == "A": # Esta letra es para ir a la izquierda restandole un puesto 
        cabeza[1] -= 1
    elif direccion == "D": # Esta letra es para ir a la derecha sumandole un puesto 
        cabeza[1] += 1
    return cabeza
def verificar_colision(nueva_cabeza): # En esta funcion verifico la colision de la serpiente
    if (
        nueva_cabeza[0] < 0 or nueva_cabeza[0] >= filas or  # Es una lista con dos coordenadas [fila,columna]
        nueva_cabeza[1] < 0 or nueva_cabeza[1] >= columnas or # que representan la posicion a la que la serpiente intenta moverse
        nueva_cabeza in serpiente  # Aqui es la autocolision con el cuerpo
    ):
        return True # Aqui si se choco contra una pared o contra si mismo se detiene el juego 
    return False # Aqui es para que el juego siga en marcha
def verificar_comida (nueva_cabeza): # Aqui es donde se toma en cuenta cunado la serpiente come y crece
    global comida # El global es una variable que puedes utilizar para cambiar sin afectar a lo demas 
    if nueva_cabeza == comida: # Aqui al momento de comer la serpiente hace que todo se ejecute para crecer
        comida = [random.randint(0, filas -1), # Utilizando random. randint hago que la comida aparezca en modo azar
                  random.randint(0, columnas -1)] # Eligen la fila y la columna al azar com siguiente destino de la comida
        return True # Devuelve si la comio
    return False # Se devuelve si la cabeza se devolivo a un espacio vacio
def iniciar_juego():
    global juego
juego = True
while juego : # Aqui repito el juego una y otra vez mientras las condiciones sean verdaderas
    os.system('cls' if os.name == 'nt' else 'clear')
    dibujar_tablero() # Muestra visualmente la posicion de la serpiente y la comida en al pantalla
    leer_movimiento() # Sabe para donde dirigirse dependiendo que tecla se presiono
    if not juego: # Para detener el juego si el jugador decidio detenerlo 
        break
    nueva_cabeza = mover_serpiente() # Calcula la siguiente coordenada a la que quiere ir la serpiente
    if verificar_colision(nueva_cabeza): # Aqui es donde se detecta si hay un choque contra la pared o el mismo cuerpo            
        print("Perdiste! Te chocaste")
        juego = False
        break # Y se detiene si hay choque 
    serpiente.insert(0, nueva_cabeza)  # aqui es donde se ingresa un nuevo O al cuerpo
    if not verificar_comida(nueva_cabeza): # Aqui se ejcuta el movimiento de la serpiente eliminando un O de la cola y aumentandola en la 
        serpiente.pop() # la cabeza si no comio y si comio no se ejecuta el pop() , la cola se queda donde esta y añade uno en la cabeza
print("Juego terminado ")# Y asi crece la serpiente
if __name__ == "__main__":
    iniciar_juego()