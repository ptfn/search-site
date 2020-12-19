import random
import requests
from bs4 import BeautifulSoup

Symbols = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
Length = random.randrange(1, 3)
Root = ['.com', '.ru', '.org', '.net']
n = 0

while n < 10:
    Domain = ''
    Url = ''
    n += 1

    file = open("site.txt", 'a+', encoding='utf-8')

    for i in range(Length):
        Domain += random.choice(Symbols)

    for i in range(len(Root)):
        url = 'https://' + Domain + Root[i]
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
            print("Domain not exist")

    file.close()
