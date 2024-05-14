from bs4 import BeautifulSoup
import re
from playwright.sync_api import sync_playwright
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

def selectedOption(option):
    if option == 1:
        validUrl = 'false'
        while(validUrl != 'true'):
            url = str(input('Ingresa la URL: '))
            if isUrlValid(url):
                validUrl = 'true'
                content = get_dynamic_soup(url)
                video_url = content.video.get('src')
                name = content.title
                if downloadVideo(video_url,'video'):
                    return print("Video Descargado Exitosamente")
                else:
                    return print("Error al Descargar Video")
            else:
                continue
    elif option == 2:
        return print('hello 2')
    elif option == 3:
        return print('hello 3')
    
def get_dynamic_soup(url: str) -> BeautifulSoup:
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=False) 
        browser = p.chromium.launch()
        context = browser.new_context(extra_http_headers=headers)
        page = context.new_page()
        page.goto(url)
        page.wait_for_load_state('networkidle')
        soup = BeautifulSoup(page.content(), "lxml")
        browser.close()
        return soup


def isUrlValid(url):
    regex = r"^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(\/[a-zA-Z0-9-._~:/?#[\]@!$&'()*+,;=]*)?$"
    return bool(re.match(regex,url))


def downloadVideo(url,title):
    video = requests.get(url)
    try:
        with open(title+'.mp4','wb') as f:
            f.write(video.content)
            return True
    except:
        return False
        
         
    
option = selectedOption(int(input('1.- Descargar Un Reel, 2.-Descargar Multiples Reels, 3.- Descargar Reels de un perfil: ')));
