import requests

def scan():
    site = input('$>: ')
    show = requests.get(site)

    print(show.status_code)  
    print(show.headers)       
    print(show.text)          
    print(show.cookies)       
    print(show.url)      