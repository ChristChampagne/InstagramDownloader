from bs4 import BeautifulSoup
import requests

# https://www.instagram.com/reel/Czv13Z-tqwh/

def selectedOption(option):
    if option == 1:
        url = str(input('Ingresa la URL: '))
        return print('hello 1')
    elif option == 2:
        return print('hello 2')
    elif option == 3:
        return print('hello 3')
    
option = selectedOption(int(input('1.- Descargar Un Reel, 2.-Descargar Multiples Reels, 3.- Descargar Reels de un perfil: ')));

    