from random import randrange, choice
from bs4 import BeautifulSoup
import requests
import sys

BigChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SmallChar = "abcdefghijklmnopqrstuvwxyz"
Number = "0123456789"
Symbols = "!?@#$%^&*=<>()[]/|,.+-_"


def brut_alph(string):
    str_last = ""
    str_res = ""

    for i in range(len(string)):
        if string[i] not in str_last:
            if string[i] == "b":
                str_res += BigChar
                str_last += "b"
            if string[i] == "c":
                str_res += SmallChar
                str_last += "c"
            if string[i] == "n":
                str_res += Number
                str_last += "n"
            if string[i] == "s":
                str_res += Symbols
                str_last += "s"
    return str_res


def main():
    try:
        Max = int(sys.argv[1])
    except:
        if Max <= 1:
            print("Argument must be greater than 1")
            exit(0)
        else:    
            print("Enter password generation length example argument: python3 search_site.py 10 bcns")
            exit(0)
    
    try:
        Strings = sys.argv[2]
    except:
        print("Enter password generation length example argument: python3 search_site.py 10 bcns")
        exit(0)

    Root = ['.com', '.ru', '.org', '.net'] 
    Alphabet = brut_alph(Strings)

    while 1:
        Domain = ''
        Url = ''
        file = open("site.txt", 'a+', encoding='utf-8')
        Length = randrange(1, Max)

        for i in range(Length):
            Domain += choice(Alphabet)

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
            finally:
                file.close()

if __name__ == "__main__":
    main()