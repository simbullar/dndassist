import PySimpleGUI as sg 
import time 

# everything inside the window 
layout = [  [sg.ProgressBar(100, key='-PROGRESS_BAR-')],
            [sg.Button('Cancel')] ]

count = 0

window = sg.Window('Hello Example', layout)


while True:
    event, values = window.read()

    # if user closes window or presses cancel
    if event == sg.WIN_CLOSED or sg.Cancel:
        break
#?    count = ++1
#?    window['-PROGRESS_BAR-'].update(current_count=count)
    time.wait(1)


window.close()