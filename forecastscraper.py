import PySimpleGUI as sg
from requests_html import HTMLSession


import PySimpleGUI as sg


def weatherScrape():
    weatherScrapelayout = [
                [sg.Text('Select your city')],
                [sg.Radio("Minneapolis", 1, key='minneapolis', enable_events=True)],
                [sg.Radio("St Paul", 2, key='stpaul', enable_events=True)],
                [sg.Radio("Eden Prairie", 3, key='ep', enable_events=True)],
                [sg.Radio("Apple Valley", 4, key='av', enable_events=True)],
                [sg.Button('Ok')],[sg.Button('Reset')]]

    window = sg.Window('Forecast Scraper', weatherScrapelayout, size=(500, 300))

    while True:                  # the event loop
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Reset':
            window["minneapolis"].reset_group()
            window["stpaul"].reset_group()
            window["ep"].reset_group()
            window["av"].reset_group()
        if event == 'Ok':
            if values['stpaul'] == True:
                sessionStPaul = HTMLSession()
                urlStPaul = 'https://forecast.weather.gov/MapClick.php?lat=44.97902000000005&lon=-93.26493999999997'
                rStPaul = sessionStPaul.get(urlStPaul)
                CSSStPaul = rStPaul.html.find('div.row-odd:nth-child(1) > div:nth-child(2)', first=True)
                sg.popup_ok_cancel("St Paul forecast is: " + CSSStPaul.text,title="Forecast")
            if values['minneapolis'] == True:
                sessionMinn = HTMLSession()
                urlMinn = 'https://forecast.weather.gov/MapClick.php?lat=44.9434&lon=-93.0965'
                rMinn = sessionMinn.get(urlMinn)
                CSSMinn = rMinn.html.find('div.row-odd:nth-child(1) > div:nth-child(2)', first=True)
                sg.popup_ok_cancel("Minneapolis forecast is: " + CSSMinn.text, title="Forecast")
            if values['ep'] == True:
                sessionEP = HTMLSession()
                urlEP = 'https://forecast.weather.gov/MapClick.php?lat=44.8587&lon=-93.4601'
                rEP = sessionEP.get(urlEP)
                CSSEP = rEP.html.find('div.row-odd:nth-child(1) > div:nth-child(2)', first=True)
                sg.popup_ok_cancel("Eden Prairie forecast is: " + CSSEP.text, title="Forecast")
            if values['av'] == True:
                sessionAV = HTMLSession()
                urlAV = 'https://forecast.weather.gov/MapClick.php?lat=44.7436&lon=-93.2176'
                rAV = sessionAV.get(urlAV)
                CSSAV = rAV.html.find('div.row-odd:nth-child(1) > div:nth-child(2)', first=True)
                sg.popup_ok_cancel("Apple Valley forecast is: " + CSSAV.text, title="Forecast")
    window.close()

weatherScrape()