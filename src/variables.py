# This is a general hub for variables. 
# I use this to make the code more organized
import PySimpleGUI as sg 
from cryptography.fernet import Fernet

key = Fernet.generate_key()

layoutRegister = [  
                        [sg.Text('Create a username:', size=(16,1)), sg.In(k='-USERNAME-', size=(10,1))],
                        [sg.Text('Create a password:', size=(16,1)), sg.In(k='-PASS-', size=(10,1))],
                        [sg.Ok(), sg.Cancel()] ]

layoutPopup = [
                [sg.Text("COPY THIS", size=(9,1))],
                [sg.Text(str(key),size=(20,4))],
                [sg.Button('Copy')]]

layoutLogin= [  [sg.Text('Username:', size=(18,1)), sg.In(k='-USERNAME-', size=(10,1))],   
                        [sg.Text('Password:', size=(18,1)), sg.In(k='-PASS-', size=(10,1))],
                        [sg.Text('Key:', size=(18,1)), sg.In(k='-KEY-', size=(10,1))],
                        [sg.Ok(), sg.Cancel(),sg.Button("New account")] ]

layoutMain= [
    [sg.Push(), sg.Text('Welcome back!', font=('Arial', 22)), sg.Push(),sg.Button("Account settings")],
    [sg.Push(), sg.Text('*'*65), sg.Push()]]

def acc_settings(username, password):
    thing = [
        [sg.Text("Username:"), sg.Text(username)],
        [sg.Text("Password:"), sg.Text(password)],
        [sg.Text("Key:"), sg.Button("Copy key")],
        [sg.Button("Delete account")]
    ]
    return thing