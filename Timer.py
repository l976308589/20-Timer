from time import sleep

import PySimpleGUI as sg
import arrow as ar
import requests as req

layout = [[sg.Text('', size=(10, 2), font=('Comic Sans MS', 20), justification='center', key='Timer')]]

window = sg.Window('TIME', layout)

count = 0
while True:
    if count == 0:
        res = req.get('https://www.baidu.com/').headers['Date']
        time_diff = ar.get(res[4:-4], 'DD MMM YYYY HH:mm:ss') - ar.now().floor('second')
    elif count > 10 * 3600 * 24:
        count = 0
    else:
        count += 1
    event, values = window.Read(timeout=10)  # Please try and use a timeout when possible
    if event is None or event == 'Exit':
        break
    window.Element('Timer').Update((ar.now() + time_diff).format('YYYY-MM-DD HH:mm:ss.SSS'))
    sleep(0.1)
