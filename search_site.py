from random import randrange, choice
from bs4 import BeautifulSoup
import requests


Symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
Length = randrange(3, 15)
Root = ['.com', '.ru', '.org', '.net']

while 1:
    Domain = ''
    Url = ''

    file = open("site.txt", 'a+', encoding='utf-8')

    for i in range(Length):
        Domain += choice(Symbols)

    for i in range(len(Root)):
        url = 'http://' + Domain + Root[i]

        try:
            r = requests.get(url, timeout=5)
            soup = BeautifulSoup(r.content, 'html.parser')
            title = soup.title.string

            if r.status_code in [200, 302, 304]:
                file.write('{}\t|\t{}\n'.format(url, title))
                print(url)

            elif r.status_code in [502, 404, 403]:
                print("Not found or not available")

        except:
            print("Site not exist")

    file.close()
