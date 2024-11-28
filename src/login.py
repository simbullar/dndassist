# This is the login sequence. 
import PySimpleGUI as sg 
from cryptography.fernet import Fernet
import pyperclip
import os

def create_account(register, key, layoutPopup):
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
                            with open(os.path.expanduser("~/Documents/python/project /src/accounts/"+username), 'w') as file:
                                file.write(str(Fernet(key).encrypt(bytes(username, 'utf-8') + b"\n" + bytes(password, 'utf-8'))))
                                break
                elif event == sg.WIN_CLOSED:
                            exit()
                elif event == sg.WIN_CLOSED or 'Cancel':
                    register.close()
                    exit()

def login(layoutRegister, layoutPopup, layoutLogin, key):


    files = os.listdir(os.path.expanduser("~/Documents/python/project /src/accounts"))
    print(str(files))
    if str(files) == '[]' :
        print('no accounts found')
    else:
        print(str(files))
        for file in files: 
            if file.endswith('.DS_Store') != True:
                with open(os.path.expanduser("~/Documents/python/project /src/accounts/"+file), 'r') as file_:
                    contents=file_.read()
                    if contents == '':
                        os.remove(os.path.expanduser("~/Documents/python/project /src/accounts/"+file))
            else:
                pass

    try:
        files = os.listdir(os.path.expanduser("~/Documents/python/project /src/accounts"))
        file2 = files[0]
        print(file2)
        for file in files:
            if file.endswith('.DS_Store') != True:
                with open(os.path.expanduser("~/Documents/python/project /src/accounts/"+file), "r") as file:
                    content = file.read()
            else: 
                pass

    except IndexError:
            register = sg.Window('Registration', layoutRegister)
            create_account(register=register, key=key, layoutPopup=layoutPopup)


    window = sg.Window('Log In', layoutLogin)
    while True:
        event, values = window.read()
        if event == 'Ok':
            key2 = eval(values['-KEY-'].encode('utf-8'))
            username2 =  values['-USERNAME-']
            password2 =  values['-PASS-']
            content2 = eval(str(bytes(username2+'\n'+password2, 'utf-8')))
            for file in files:
                if file.endswith('.DS_Store') != True:
                    file = open(os.path.expanduser("~/Documents/python/project /src/accounts/"+file), 'r')
                    content = file.read()
                    dec_cont = Fernet(key2).decrypt(eval(content))
                    if dec_cont == content2:
                        username_final = username2
                        window.close()
                        return username_final
                    elif content != content2:
                        print('incorrect')
                        sg.popup("Incorrect data")
                else:
                    pass
        elif event == "New account":
            register = sg.Window('Registration', layoutRegister)
            create_account(register=register, key=key, layoutPopup=layoutPopup)

        elif event == sg.WIN_CLOSED or event == 'Cancel':
            exit()
