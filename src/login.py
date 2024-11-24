import PySimpleGUI as sg 
from cryptography.fernet import Fernet
import pyperclip
import os


def login():
    key = Fernet.generate_key()
    #* everything inside the windows

    layoutRegister = [  
                        [sg.Text('Create a username:', size=(16,1)), sg.In(k='-USERNAME-', size=(10,1))],
                        [sg.Text('Create a password:', size=(16,1)), sg.In(k='-PASS-', size=(10,1))],
                        [sg.Ok(), sg.Cancel()] ]
    layoutPopup = [
                    [sg.Text("COPY THIS", size=(9,1))],
                    [sg.Text(str(key),size=(20,7))],
                    [sg.Button('Copy')]
    ]
    layoutLogin= [  [sg.Text('Username:', size=(18,1)), sg.In(k='-USERNAME-', size=(10,1))],   
                        [sg.Text('Password:', size=(18,1)), sg.In(k='-PASS-', size=(10,1))],
                        [sg.Text('Key:', size=(18,1)), sg.In(k='-KEY-', size=(10,1))],
                        [sg.Ok(), sg.Cancel(),] ]


    files = os.listdir(os.path.expanduser("~/Documents/python/project /src/accounts"))
    if str(files) == '[]' :
        print('no accounts found')
    else:
        print(str(files))
        for file in files: 
            with open(os.path.expanduser("~/Documents/python/project /src/accounts/"+file), 'r') as file_:
                contents=file_.read()
                if contents == '':
                    os.remove(os.path.expanduser("~/Documents/python/project /src/accounts/"+file))

    try:
        files = os.listdir(os.path.expanduser("~/Documents/python/project /src/accounts"))
        with open(os.path.expanduser("~/Documents/python/project /src/accounts/"+file), "r") as file:
            content = file.read()

    except IsADirectoryError:
            register = sg.Window('Registration', layoutRegister)

            while True:
                event, values = register.read()

                if event == 'Ok':
                    username = values['-USERNAME-']
                    password = values['-PASS-']
                    register.close()
                    popup=sg.Window('Key', layoutPopup)
                    while True:
                        event, values = popup.read()
                        if event =='Copy':
                            pyperclip.copy(key)
                            break
                        elif event == sg.WIN_CLOSED:
                            exit()
                    popup.close()
                    break

                elif event == sg.WIN_CLOSED or 'Cancel':
                    register.close()
                    exit()
            with open(os.path.expanduser("~/Documents/python/project /src/accounts/"+username), 'w') as file:
                file.write(str(Fernet(key).encrypt(bytes(username, 'utf-8') + b"\n" + bytes(password, 'utf-8'))))


    window = sg.Window('Log In', layoutLogin)
    while True:
        event, values = window.read()


        if event == 'Ok':
            key2 = eval(values['-KEY-'].encode('utf-8'))
            username2 =  values['-USERNAME-']
            password2 =  values['-PASS-']
            content2 = eval(str(bytes(username2+'\n'+password2, 'utf-8')))
            for file in files:
                file = open(os.path.expanduser("~/Documents/python/project /src/accounts/"+file), 'r')
                content = file.read()
                dec_cont = Fernet(key2).decrypt(eval(content))
                print(content2)
                print(dec_cont)
                print(type(content2))
                print(type(dec_cont))
                if dec_cont == content2:
                    break
                elif content != content2:
                    sg.popup("Incorrect data")
        elif event == sg.WIN_CLOSED or event == 'Cancel':
            exit()

    window.close()

    return True