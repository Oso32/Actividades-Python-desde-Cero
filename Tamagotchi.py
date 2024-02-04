from tqdm import tqdm 
from time import sleep 

class Tamagotchi():

    def __init__(self, nombre, nivel_energia, nivel_hambre,nivel_felicidad, humor, esta_vivo):
        self.nombre = nombre
        self.energia = nivel_energia
        self.hambre = nivel_hambre
        self.felicidad = nivel_felicidad
        self.humor = humor
        self.estado = esta_vivo

    def __str__(self):
        return f"Hola mi nombre es {self.nombre}"

    def mostrar_estado(self):
        """Muestra en consola el nombre del Tamagotchi
        y sus niveles actuales de energía, hambre 
        y estado de humor.
        """
        if self.verificar_estado()==False:
            return
        if self.hambre>=20:
            self.energia-=20
            self.felicidad-=30
            if self.energia < 0: #Esto lo hago para que los atrivutos no se salgan del rango 0-100
                self.energia=0
                return
            if self.felicidad <0:
                self.felicidad=0
        if self.felicidad == 100 and self.energia == 100:
            self.humor = "Euforico"
        elif self.felicidad > 50 and self.energia > 50:
            self.humor =  "Feliz"
        elif self.felicidad == 50 and (self.energia >= 45 and self.energia <= 55):
            self.humor = "Indiferente"
        elif (self.felicidad < 50 and self.felicidad > 30) and (self.energia >= 30 and self.energia <= 44):
            self.humor = "Enojado"
        elif (self.felicidad <= 30 and self.felicidad >= 0) and (self.energia > 0 and self.energia < 30):
            self.humor = "Triste"

        mostrar = f"""=====================
--Mi nombre es: {self.nombre}
--Mis niveles de:
-Energia: {self.energia}
-Hambre: {self.hambre}
-Humor:  {self.humor}
=========================================
"""
        return mostrar

    def alimentar(self):
        """ Disminuye el nivel de hambre 
        en 10 y disminuye el nivel de energía en 15."""
        if self.verificar_estado()==False:
            return
        self.hambre -= 10
        self.energia -= 15
        if self.hambre < 0:
            self.hambre=0   #Esto lo hago para que los atrivutos no se salgan del rango 0-100
        if self.energia < 0:
            self.energia=0
            return
        for i in tqdm(range(0, 100), desc =f"Se esta alimentando {self.nombre}"):
            sleep(.1)
        

    def jugar(self):
        """Aumenta el nivel de felicidad en 20, 
        disminuye el nivel de 
        energía en 18 y aumenta el nivel de hambre en 10."""
        if self.verificar_estado()==False:
            return
        if self.hambre>=20:
            self.energia-=20
            self.felicidad-=30
        else:
            self.felicidad += 20
            self.energia -= 18
        self.hambre += 10

        if self.felicidad < 0:
            self.felicidad=0
        elif self.felicidad >100: #hago esto para que felicidad no se salga del rango 0-100
            self.felicidad=100
        if self.energia<0:
            self.energia = 0 #esto para que energia no se salga del rango
            return
        if self.hambre>100:
            self.hambre=100
        for i in tqdm(range(0,100), desc=f"{self.nombre} esta jugando"):
            sleep(.1)

    def dormir(self):
        """Aumenta el nivel de energía en 40 y
        aumenta el nivel de hambre en 5."""
        if self.verificar_estado()==False:
            return
        if self.hambre>=20:
            self.energia-=20 
            self.felicidad-=30
        else:
            self.energia += 40
        self.hambre += 5

        if self.energia < 0:
            self.energia=0
            return
        elif self.energia >100: #hago esto para que energia no se salga del rango 0-100
            self.energia=100

        if self.felicidad<0:
            self.felicidad=0
        if self.hambre>100:
            self.hambre=100
        for i in tqdm(range(0,100), desc=f"{self.nombre} esta durmiendo"):
            sleep(.1)

    def verificar_estado(self):
        """revisa si el Tamagotchi está vivo"""
        if self.energia>0:
            return True
        else:
            return False
        

inicio = """=============================
Ingrese el nombre de su Tamagotchi: """
nombre = input(inicio)
print("=============================")
inicio_energia = 100
inicio_hambre = 0
inicio_felicidad= 50
"""Estado de humor:
-euforico: si felicidad == 100 and energia == 100
-feliz: si felicidad > 50 and energia > 50
-indiferente: si felicidad == 50 and (energia >= 45 and energia <= 55)
-enojado: si (felicidad < 50 and felicidad > 30) and (energia >= 30 and energia <= 44)
-triste: si (felicidad <= 30 and felicidad >= 0) and (energia > 0 and energia < 30)
"""
inicio_humor = "feliz"
inicio_vivo = True

tu_tamagotchi = Tamagotchi(nombre, inicio_energia, inicio_hambre, inicio_felicidad, inicio_humor, inicio_vivo)
#Inicia el juego
menu = f"""
===================
Que quiere que haga {nombre} ???
1-Mostrar su estado
2-Alimentarse
3-Jugar
4-Dormir
Elija por el numero correspondiente: """
while True:
    while True:
        eleccion = int(input(menu))
        if eleccion >= 1 and eleccion <= 4:
            break
    if tu_tamagotchi.verificar_estado() == False:
        print(f"🪦-{nombre} a muerto  :(")
        break
    if eleccion == 1:
        mostrar = tu_tamagotchi.mostrar_estado()
        print(mostrar)
    elif eleccion == 2:
        alimentarce = tu_tamagotchi.alimentar()
    elif eleccion == 3:
        jugar = tu_tamagotchi.jugar()
    elif eleccion == 4:
        dormir = tu_tamagotchi.dormir()


    
