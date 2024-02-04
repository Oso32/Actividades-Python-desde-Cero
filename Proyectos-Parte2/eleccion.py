import PySimpleGUI as sg
from PantallaEleccion import *
import time
def main():
    sg.theme('DarkAmber')
    ventana_1 = menu_1()

    while True:
        evento, valores = ventana_1.read()
        if evento == sg.WIN_CLOSED:
            ventana_1.close()
            break
        if evento == 'ATACAR':
            ventana_1.close()
            return "atacar"
            break
        if evento == 'ESCUDO':
            ventana_1.close()
            return "escudo"
            break

def estado(jugador, enemigo):
    
    #crear ventana 2con el mmenu de estado y mantener actualizado datos, usando como refferencia pru2.py
    sg.theme('DarkAmber')
    ventana_2 = menu_estado()

    while True:
        evento, valores = ventana_2.read(timeout=100)
        if evento == sg.WIN_CLOSED:
            ventana_2.close()
            break
        ventana_2.Element("HORA").update("Horario: " + time.strftime("%H:%M:%S"))
        #Datos de Jugador
        ventana_2.Element("NOMBREJ").update(f"Nombre: {jugador.nombre}")
        ventana_2.Element("VIDAJ").update(f"Vida: {jugador.vida}")
        ventana_2.Element("ATAQUEJ").update(f"Ataque: {jugador.ataque}")
        ventana_2.Element("DEFENSAJ").update(f"Defensa: {jugador.defensa}")
        ventana_2.Element("INTELIGENCIAJ").update(f"Inteligencia: {jugador.inteligencia}")
        ventana_2.Element("AGILIDADJ").update(f"Agilidad: {jugador.agilidad}")

        #Datos de enemigo
        ventana_2.Element("NOMBREN").update(f"Nombre: {enemigo.nombre}")
        ventana_2.Element("VIDAN").update(f"Vida: {enemigo.vida}")
        ventana_2.Element("ATAQUEN").update(f"Ataque: {enemigo.ataque}")
        ventana_2.Element("DEFENSAN").update(f"Defensa: {enemigo.defensa}")
        ventana_2.Element("INTELIGENCIAN").update(f"Inteligencia: {enemigo.inteligencia}")
        ventana_2.Element("AGILIDADN").update(f"Agilidad: {enemigo.agilidad}")
        if evento == "Continuar":
            ventana_2.close()
            break



