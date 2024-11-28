import login
import PySimpleGUI as sg 
from variables import *

name_returned = login.login(layoutRegister=layoutRegister, key=key, layoutLogin=layoutLogin, layoutPopup=layoutPopup)

if name_returned[0] == 'simbullar' and name_returned[1] == 'impostor1234':
    main = sg.Window(title="Main menu",layout=layoutMain, size=(300,350))
    while True:
                event, values = main.read()
                if event == sg.WIN_CLOSED:
                    exit()
                elif event == "Account settings":
                    settings = sg.Window(title="System settings", layout=acc_settings(name_returned[0], name_returned[1]), size=(250,300))
                    while True:
                        event, values = settings.read()
                        if event == sg.WIN_CLOSED:
                            exit()
                            