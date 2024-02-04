import random
import eleccion
import threading    # Para trabajar con hilos utilizamos la librería threading
import time    # Para poder utilizar la función sleep, la cual detiene el programa X segundos
#=====Seccion de funciones=========================================
# def segundo_plano(flag_global, jugador, enemigo):
#     while not flag_global.is_set():    # Mientras flag_global sea False
#         eleccion.estado(jugador,enemigo)
#     print("\nEl hilo se detuvo")
    

#===================================================================
class personaje():
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        self.nombre = nombre
        self.vida =vida
        self.ataque = ataque
        self.defensa = defensa
        self.inteligencia = inteligencia
        self.agilidad = agilidad
        self.fuerza = fuerza

    def atacar(self, enemigo):
        pass

    def mostrar_estadisticas(self):
        print(f"\nEstadísticas de {self.nombre}:")
        print(f"Vida: {self.vida}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Agilidad: {self.agilidad}")
        print(f"Fuerza: {self.fuerza}")


class Guerrero(personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 100, 15, 10, 5, 5, 10)

        self.ataque_espada = 15
        self.defensa_escudo = 15
        self.defensa += self.defensa_escudo
    def __str__(self):
        return f"Tu nombre es {self.nombre}. Y tus dos armas exclusivas son una espada y escudo."
    
    def atacar(self, enemigo):
        danio = self.ataque + self.fuerza + self.ataque_espada - enemigo.defensa
        enemigo.vida -= danio
        return danio

class Mago(personaje):
    def __init__(self, nombre):
        super().__init__(nombre,80, 10, 5, 15, 3, 5)

        self.ataque_bolas_fuego = 10
        self.defensa_escudo_invisible = 30
        self.defensa += self.defensa_escudo_invisible
    def __str__(self):
        return f"Tu nombre es {self.nombre}. Y tus dos armas exclusivas son tirar bolas de fuego y un escudo ivisible."
    
    def atacar(self, enemigo):
        danio = self.ataque + self.inteligencia + self.ataque_bolas_fuego - enemigo.defensa
        enemigo.vida -= danio
        return danio

class Arquero(personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 90, 12, 7, 8, 10, 8)

        self.ataque_arco_triple_flecha = 20
        self.defensa_ropa_especial = 18
        self.agilidad += self.defensa_ropa_especial
        self.defensa += self.defensa_ropa_especial
    def __str__(self):
        return f"Tu nombre es {self.nombre}. Y tus dos armas exclusivas es un arco que tira tres flechas a la vez\ny una ropa que aumenta tu agilidad y defensa."

    def atacar(self, enemigo):
        danio = self.ataque + self.agilidad  + self.ataque_arco_triple_flecha - enemigo.defensa
        enemigo.vida -= danio
        return danio
class Asesino(personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 85, 13, 6, 10, 12, 7)

        self.ataque_cuchillo_con_veneno = 20
        self.defensa_zapatillas_agiles = 8
        self.agilidad += self.defensa_zapatillas_agiles
    def __str__(self):
        return f"Tu nombre es {self.nombre}. Y tus dos armas exclusivas es un cuchillo con veneno y unas zapatillas que aumentan la agilidad."
    
    def atacar(self, enemigo):
        danio = self.ataque + self.agilidad + self.inteligencia + self.ataque_cuchillo_con_veneno - enemigo.defensa
        enemigo.vida -= danio
        return danio

class Enemigo(personaje):
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        super().__init__(nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza)

    def atacar(self, jugador,se_cubrio = False):
        danio = 0
        if se_cubrio:
            if jugador.agilidad <= 5:
                danio = self.ataque - (jugador.defensa+1)
                jugador.vida -= danio
            elif jugador.agilidad == 10:
                danio = self.ataque - (jugador.defensa+3)
                jugador.vida -= danio
            elif jugador.agilidad == 12:
                danio = self.ataque - (jugador.defensa+5)
                jugador.vida -= danio
        else:
            # Ataque simple del enemigo
            danio = self.ataque - jugador.defensa
            jugador.vida -= danio
        return danio
#Los enemigos que habra son un Ogro, un Espectro,  un Goblin y como enemigo voador un dragon
class EnemigoVolador(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, 110, 12, 5, 8, 15, 6)

    def esquivar_ataque(self):
        return random.choice([True, False])

#el personaje con mayor agilidad será el primero en atacar.
para_saber_que_personaje_toca_en_turno = ""
validar = True
para_saber_si_te_cubriste = False
def turno_de_ataque(jugador, enemigo):
    eleccion.estado(jugador, enemigo)
    global para_saber_que_personaje_toca_en_turno
    global validar
    global para_saber_si_te_cubriste
    if jugador.agilidad > enemigo.agilidad and validar:
        validar = False  #La varieble validar sirbe para controlar que este if solo
                        #se use en el primer turno.
        para_saber_que_personaje_toca_en_turno = "jugador"
        print(f"{jugador.nombre} es el primero en atacar.")
    if para_saber_que_personaje_toca_en_turno == "jugador":
        para_saber_si_te_cubriste = False
        para_saber_que_personaje_toca_en_turno = "enemigo"
        print(f"{jugador.nombre} es tu turno.")
        while True:
            opcion_elegida = eleccion.main()
            if opcion_elegida == "atacar" or opcion_elegida == "escudo":
                print(f"{jugador.nombre} elijio {opcion_elegida}.")
                break
            print(f"{jugador.nombre} para seguir en el juego tiene que elejir una opcion.")

        if opcion_elegida == "atacar":
            if isinstance(enemigo, EnemigoVolador):
                if enemigo.esquivar_ataque():
                    print(f"{enemigo.nombre} esquiva el ataque de {jugador.nombre}!")
                else:
                    print(f"{jugador.nombre} ataco a {enemigo.nombre}")
                    jugador.atacar(enemigo)
            else:
                print(f"{jugador.nombre} ataco a {enemigo.nombre}")
                jugador.atacar(enemigo)
            
        else:
            para_saber_si_te_cubriste = True
        
        if enemigo.vida <=0:
            print(f"{enemigo.nombre} a muerto_________________")
            return True
    else:
        para_saber_que_personaje_toca_en_turno = "jugador"
        print(f"{enemigo.nombre} es su turno.")
        if para_saber_si_te_cubriste:
            enemigo.atacar(jugador, para_saber_si_te_cubriste)
            print(f"{enemigo.nombre} ataca, pero {jugador.nombre} se cubrio.")
        else:
            enemigo.atacar(jugador)
            print(f"{enemigo.nombre} ataca.")

        if jugador.vida <= 0:
            print(f"{jugador.nombre} a muerto________________________")
            return True
    return False


def main():
    print("Bienvenido al juego RPG")

    # Selección de clase por el jugador
    nombre_jugador = input("Ingresa el nombre de tu personaje: ")
    clase_jugador = input("Selecciona tu clase (Guerrero, Mago, Arquero, Asesino): ").capitalize()

    if clase_jugador not in ["Guerrero", "Mago", "Arquero", "Asesino"]:
        print("Clase no válida. Selecciona una clase válida.")
        return

    jugador = globals()[clase_jugador](nombre_jugador)  # Crear instancia de la clase seleccionada

    # Crear enemigos
    enemigo1 = Enemigo("Orco", 100, 15, 5, 5, 5, 15)
    enemigo2 = Enemigo("Espectro", 80, 10, 5, 15, 3, 5)
    enemigo3 = Enemigo("Goblin", 85, 13, 6, 10, 12, 7)
    enemigo4 = EnemigoVolador("Dragon")

    enemigos = [enemigo1, enemigo2, enemigo3, enemigo4]

    # flag_global = threading.Event()

    for encuentro in range(1, 5):
        print(f"\nEncuentro {encuentro}: {jugador.nombre} vs {enemigos[encuentro - 1].nombre}")
        while True:
            # flag_global.clear()    
            # hilo = threading.Thread(target=segundo_plano, args=(flag_global, jugador, enemigos[encuentro - 1]))
            # hilo.start()
            if turno_de_ataque(jugador, enemigos[encuentro - 1]):
                break

if __name__ == "__main__":
    main()
