import PySimpleGUI as sg 


#TODO basically a test of my idea of autheticating trough a txt 
#TODO so create a txt with username and password
#if you are wondering what purpose did the progress bar serve 
# idk actually 




#* everything inside the window 
layoutRegister = [  [sg.Text('Type a username:', size=(16,1)), sg.In(k='-USERNAME-', size=(10,1))],
                    [sg.Text('Type a password:', size=(16,1)), sg.In(k='-PASS-', size=(10,1))],
                    [sg.Ok(), sg.Cancel()] ]

layoutLogin= [  [sg.Text('Type your username:', size=(18,1)), sg.In(k='-USERNAME-', size=(10,1))],
                    [sg.Text('Type your password:', size=(18,1)), sg.In(k='-PASS-', size=(10,1))],

                    [sg.Ok(), sg.Cancel()] ]

try:

    with open("auth_info.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    with open("auth_info.txt", "w") as file:
        register = sg.Window('Registration', layoutRegister)

        while True:
            event, values = register.read()

            if event == 'Ok':
                username = values['-USERNAME-']
                password = values['-PASS-']
                break

            elif event == sg.WIN_CLOSED or 'Cancel':
                exit()
        register.close()
        file.write(str(username)+" /n "+str(password))


window = sg.Window('Log In', layoutLogin)
while True:
    event, values = window.read()

    #* if user closes window 
    if event == sg.WIN_CLOSED:
        break



window.close()