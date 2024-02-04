import PySimpleGUI as sg

def menu_1():
    #MLINE_KEY = '-MLINE-'+sg.WRITE_ONLY_KEY
    layout_1 = [
    [sg.Text('Es tu turno, deseas atacar al eneigo o cubrirte con tu escudo?:',font=('Helvetica', 20))],
    [sg.Text("Si elijes el escudo, al ataque del enemigo se le resta, ademas de tu defensa,\nun intento de esquivarlo (en el caso de no tener un escudo).")],
    [sg.Text("Si no tienes escudo, poder esquivar el ataque va a variar segun tu Agilidad.")],
    [sg.Button('ATACAR'), sg.Button('ESCUDO')]
    ]
    return sg.Window('Eleccion', layout_1, finalize=True)

def menu_estado():

    #Armar el menu donde se muestre el estado de los dos personajes

    layout_2 = [
        [sg.Text("",key="HORA")],
        [sg.Text("Jugador:",font=('Helvetica', 40))],
        [sg.Text("Nombre: ", key="NOMBREJ")],
        [sg.Text("Vida: ", key="VIDAJ")],
        [sg.Text("Ataque: ", key="ATAQUEJ")],
        [sg.Text("Defensa: ", key="DEFENSAJ")],
        [sg.Text("Inteligencia: ", key="INTELIGENCIAJ")],
        [sg.Text("Agilidad: ", key="AGILIDADJ")],
        [sg.Text("Enemigo:",font=('Helvetica', 40))],
        [sg.Text("Nombre: ", key="NOMBREN")],
        [sg.Text("Vida: ", key="VIDAN")],
        [sg.Text("Ataque: ", key="ATAQUEN")],
        [sg.Text("Defensa: ", key="DEFENSAN")],
        [sg.Text("Inteligencia: ", key="INTELIGENCIAN")],
        [sg.Text("Agilidad: ", key="AGILIDADN")],
        [sg.Text("Para continuar apreta 'continuar' o cierra ventana",font=('Helvetica', 15))],
        [sg.Button("Continuar")]
        
    ]
    return sg.Window('Estado', layout_2, finalize=True)


