import random
from tqdm import tqdm 
from time import sleep 
from colorama import Fore

def mostrarTablero(pos):
    print(f"""
---------------------------------------
+--------+--------+--------+
+    {pos[0]}   +    {pos[1]}   +    {pos[2]}   +
+--------+--------+--------+
+    {pos[3]}   +    {pos[4]}   +    {pos[5]}   +
+--------+--------+--------+
+    {pos[6]}   +    {pos[7]}   +    {pos[8]}   +
+--------+--------+--------+
          
---------------------------------------
          """)
def convertirEnMatriz(tableroActual):
    """Para convertir el vector (tableroActual) en
        una matriz"""
    tablero = [[0,1,2],[3,4,5],[6,7,8]]
    indiceFila = 0
    indiceColumna=0
    indice=0
    for i in tablero:
    
        for j in i:
            tablero[indiceColumna][indiceFila] = tableroActual[indice] 
            indiceFila += 1
            indice += 1
            if indiceFila ==3:
                indiceFila=0
            
        indiceColumna += 1
    return tablero
def eleccionDeLaMaquina(tableroActual,turno):
    tablero = convertirEnMatriz(tableroActual)#Usamos esta matriz para el else
    eleccion = 20 #esta variable va a retornar el indice que usa la maquina
    #Pongo un numero fuera del rango (20), para usarlo en el proximo else
    #Porque si despues del else, la variable eleccion queda con el valor
    #20 significa que no se modifico
    if not(turno >=3):

        if tablero[0][0]==Fore.BLUE+"X"+Fore.RESET:
            eleccion = 8
        elif tablero[0][2]==Fore.BLUE+"X"+Fore.RESET:
            eleccion = 6
        elif tablero[2][0]==Fore.BLUE+"X"+Fore.RESET:
            eleccion = 2
        elif tablero[2][2]==Fore.BLUE+"X"+Fore.RESET:
            eleccion = 0
        else:
            eleccion = random.randint(0, 8)
            while tableroActual[eleccion]==Fore.BLUE+"X"+Fore.RESET:
                eleccion = random.randint(0, 8)

    else:#despues de 3 turnos, hay unas condiciones para que la maquina elija

        #Empesamos a ver opcion de poner por fila
        for fila in tablero:
            if fila.count(Fore.BLUE+"X"+Fore.RESET)==2:
                for columna in fila:
                    if not(columna==Fore.BLUE+"X"+Fore.RESET) and not(columna==Fore.BLUE+"X"+Fore.RESET):
                        eleccion=columna

        #Ahora vemos por columna si hay una opcion de poner
        variableParaX = 0
        variableParaO = 0
        for i in range(0,3):
            for j in range(0,3):
                if tablero[j][i] ==Fore.BLUE+"X"+Fore.RESET:
                    variableParaX += 1
                elif tablero[j][i]==Fore.RED+"O"+Fore.RESET:
                    variableParaO += 1
            if variableParaX == 2 and variableParaO == 0:
                for j in range(0,3):
                    if not(tablero[j][i]==Fore.BLUE+"X"+Fore.RESET):
                        eleccion=tablero[j][i]

            variableParaX = 0
            variableParaO = 0
        #ahora vemos la diagonal principal
        for i in range(0,3):
            if tablero[i][i]==Fore.BLUE+"X"+Fore.RESET:
                variableParaX+=1
            elif tablero[i][i]==Fore.RED+"O"+Fore.RESET:
                variableParaO+=1
        if variableParaX == 2 and variableParaO == 0:
            for j in range(0,3):
                if not(tablero[j][j]==Fore.BLUE+"X"+Fore.RESET):
                    eleccion = tablero[j][j]
        variableParaX = 0
        variableParaO = 0
            

        #Ahora verificamos la diagonal secundaria
        for i in range(0,3):
            if i == 0:
                if tablero[i][2]==Fore.BLUE+"X"+Fore.RESET:
                    variableParaX+=1
                elif tablero[i][2]==Fore.RED+"O"+Fore.RESET:
                    variableParaO+=1
            elif i == 2:
                if tablero[i][0]==Fore.BLUE+"X"+Fore.RESET:
                    variableParaX+=1
                elif tablero[i][0]==Fore.RED+"O"+Fore.RESET:
                    variableParaO+=1
            else:
                if tablero[i][i]==Fore.BLUE+"X"+Fore.RESET:
                    variableParaX+=1
                elif tablero[i][i]==Fore.RED+"O"+Fore.RESET:
                    variableParaO+=1
        if variableParaX == 2 and variableParaO == 0:
            if not(tablero[0][2]==Fore.BLUE+"X"+Fore.RESET):
                eleccion = tablero[0][2]
            elif not(tablero[1][1]==Fore.BLUE+"X"+Fore.RESET):
                eleccion = tablero[1][1]
            else:
                eleccion = tablero[2][0]

        #Si la variable eleccion no se modifico con todo lo anterior, va a elejir una posicion al azar
        if eleccion == 20:
            eleccion = random.randint(0, 8)
            while tableroActual[eleccion]==Fore.BLUE+"X"+Fore.RESET:
                eleccion = random.randint(0, 8)
    return eleccion
def verificarSiHayGanador(tableroActual):
    tablero = convertirEnMatriz(tableroActual)
    """A partir de haca se realiza verificacion si hay ganador o no."""
    #Vamos a comprobar fila por fila si hay ganador
    for i in range(0,3):
        if tablero[i].count(Fore.BLUE+"X"+Fore.RESET) == 3:
            return True, "Jugador 1"
        elif tablero[i].count(Fore.RED+"O"+Fore.RESET) == 3:
            return True, "Jugador 2"
    #Vamos a comprovar columna por columna si hay ganador
    variableParaX = 0
    variableParaO = 0
    for i in range(0,3):
        for j in range(0,3):
            if tablero[j][i] ==Fore.BLUE+"X"+Fore.RESET:
                variableParaX += 1
            elif tablero[j][i]==Fore.RED+"O"+Fore.RESET:
                variableParaO += 1
        if variableParaX == 3:
            return True, "Jugador 1"
        elif variableParaO == 3:
            return True, "Jugador 2"
        variableParaX = 0
        variableParaO = 0

    #Ahora verificamos si hay un ganador en la diagonal principal
    variableParaO=0
    variableParaX=0
    for i in range(0,3):
        if tablero[i][i]==Fore.BLUE+"X"+Fore.RESET:
            variableParaX+=1
        elif tablero[i][i]==Fore.RED+"O"+Fore.RESET:
            variableParaO+=1
    if variableParaX == 3:
        return True, "Jugador 1"
    elif variableParaO == 3:
        return True, "Jugador 2"
    variableParaX = 0
    variableParaO = 0

    #Ahora verificamos la diagonal secundaaria
    variableParaX=0
    variableParaO=0
    for i in range(0,3):
        if i == 0:
            if tablero[i][2]==Fore.BLUE+"X"+Fore.RESET:
                variableParaX+=1
            elif tablero[i][2]==Fore.RED+"O"+Fore.RESET:
                variableParaO+=1
        elif i == 2:
            if tablero[i][0]==Fore.BLUE+"X"+Fore.RESET:
                variableParaX+=1
            elif tablero[i][0]==Fore.RED+"O"+Fore.RESET:
                variableParaO+=1
        else:
            if tablero[i][i]==Fore.BLUE+"X"+Fore.RESET:
                variableParaX+=1
            elif tablero[i][i]==Fore.RED+"O"+Fore.RESET:
                variableParaO+=1
    if variableParaX == 3:
        return True, "Jugador 1"
    elif variableParaO == 3:
        return True, "Jugador 2"
    variableParaX = 0
    variableParaO = 0


    return False,""
    
menu = """
-----------------------
Desea jugar con algun amigo o contra la maquina ???:
1- Con amigo
2- Contra maquina
------------------------
Elija respecto al numero (1/2): """

posiciones = [0,1,2,3,4,5,6,7,8]
tableroLibre = [0,1,2,3,4,5,6,7,8]
print("==================================")
print("Tateti")
print("Primero inicia jugando el jugador 1(X), luego el dos (O) y asi van turnando.")
print("==================================")
maquina=False
contador = 0
turno = True #Este bool es para saber si es el turno de la 1ra o 2da persona.
#Este while es para el menu de eleccion de modo de juego
while True:
    maquina_si_o_no = int(input(menu))
    if maquina_si_o_no==2:
        maquina=True
        break
    elif maquina_si_o_no==1:
        break
#print("================================================================")
        
while True:
    contador += 1
    l=""
    for i in posiciones:
        for j in tableroLibre:  #Este bucle corrobora que haya al menos un espacio vacio.
            if i ==j:
                l += "1"
            else:
                l += "0"

    if "1" in l:
        if turno:
            print("================================================================================================")
            print(Fore.GREEN+"""Turno del 1er participante: 
Ingrese el indice del casillero a elejir."""+Fore.RESET)
            mostrarTablero(posiciones)
            while True:
                indice = int(input("Ingrese el indice: "))
                if indice >= 0 and indice <=8 and not(posiciones[indice]=="X" or posiciones[indice]=="O"):
                    break
                print("------------------------Error: Debe ingresar un numero  dentro del rango (0-8) y que no este ocupado.")
            posiciones[indice] = Fore.BLUE+"X"+Fore.RESET
            turno = False
            
            if contador >= 5:
                gano,jugador = verificarSiHayGanador(posiciones)
                if gano:
                    print("----------------------------------------")
                    print(Fore.YELLOW+f"Gano el jugador {jugador}")
                    mostrarTablero(posiciones)
                    break
        else:
            print("================================================================================================")
            if maquina:
                indice = int(eleccionDeLaMaquina(posiciones, contador))
                posiciones[indice] = Fore.RED+"O"+Fore.RESET
                mostrarTablero(posiciones)
                print(Fore.RED+f"La maquina elijio el indice: {indice}"+Fore.RESET)
                for i in tqdm(range(0, 100), desc ="En este tiempo, puede ver lo que elijio la maquina"):
                    sleep(.1)
            else:
                print(Fore.GREEN+"""Turno del 2do participante: 
Ingrese el indice del casillero a elejir."""+Fore.RESET)
                mostrarTablero(posiciones)
                while True:
                    indice = int(input("Ingrese el indice: "))
                    if indice >= 0 and indice <=8 and not(posiciones[indice]=="X" or posiciones[indice]=="O"):
                        break
                    print("------------------------Error: Debe ingresar un numero  dentro del rango (0-8) y que no este ocupado.")
                posiciones[indice] = Fore.RED+"O"+Fore.RESET
            
            
            turno = True

            if contador >= 5:
                gano,jugador = verificarSiHayGanador(posiciones)
                if gano:
                    if maquina:
                        print("----------------------------------------")
                        print(Fore.YELLOW+f"Gano la maquina.")
                        mostrarTablero(posiciones)
                        break
                    print("----------------------------------------")
                    print(Fore.YELLOW+f"Gano el jugador {jugador}")
                    mostrarTablero(posiciones)
                    break
        
            
    else:
        print(Fore.YELLOW+"========================================================================")
        print("Nadie gano, hay empate."+Fore.RESET)
        break
        
    
        
        
    
    

