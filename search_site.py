from random import randrange, choice
from bs4 import BeautifulSoup
import requests
import sys


def main():
    try:
        Max = int(sys.argv[1])
    except:
        print("Enter password generation length example argument: python3 search_site.py 10  ")
        exit(0)

    try:
        Length = randrange(1, Max)
    except:
        print("Argument must be greater than 1")
        exit(0)

    Symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Root = ['.com', '.ru', '.org', '.net'] 

    while 1:
        Domain = ''
        Url = ''

        file = open("site.txt", 'a+', encoding='utf-8')

        for i in range(Length):
            Domain += choice(Symbols)

        for i in range(len(Root)):
            Url = 'http://' + Domain + Root[i]

            try:
                r = requests.get(Url, timeout=2.5)
                soup = BeautifulSoup(r.content, 'html.parser')
                title = soup.title.string

                if r.status_code in [200, 302, 304]:
                    file.write('{}\t|\t{}\n'.format(Url, title))
                    print(Url)

                elif r.status_code in [502, 404, 403]:
                    print("Not found or not available")

            except:
                print("Site not exist")

        file.close()

if __name__ == "__main__":
    main()
