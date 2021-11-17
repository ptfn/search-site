from random import randrange, choice
from bs4 import BeautifulSoup
import requests
import datetime
import time
import sys

number = "0123456789"
symbols = "!?@#$%^&*=<>()[]/|,.+-_"
bigchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallchar = "abcdefghijklmnopqrstuvwxyz"


def brut(string):
    str_last = ""
    str_res = ""

    for i in range(len(string)):
        if string[i] not in str_last:

            if string[i] == "b":
                str_res += bigchar
                str_last += "b"

            if string[i] == "c":
                str_res += smallchar
                str_last += "c"

            if string[i] == "n":
                str_res += number
                str_last += "n"

            if string[i] == "s":
                str_res += symbols
                str_last += "s"

    return str_res


def now():
    dt_obj =datetime.datetime.now()
    return dt_obj.strftime("%b %d %H:%M:%S")


def main():
    try:
        maximus = int(sys.argv[1])
    except:
        if maximus < 2 :
            print("Argument must be greater than 1.")
            exit(0)
        else:
            print("Enter password generation length example argument: python3 search_site.py 10 bcns.")
            exit(0)

    try:
        string = sys.argv[2]
    except:
        print("Enter password generation length example argument: python3 search_site.py 10 bcns.")
        exit(0)

    alphabet = brut(string)
    root = ['.com', '.ru', '.org', '.net']

    found = 0
    not_found = 0
    exist = 0
    allsite = 0

    while 1:
        try:
            url = ''
            domain = ''
            length = randrange(1, maximus)
            file = open("site.txt", 'a+', encoding='utf-8')

            for i in range(length):
                domain += choice(alphabet)

            for i in range(len(root)):
                url = 'http://' + domain + root[i]

                try:
                    r = requests.get(url, timeout=10)
                    soup = BeautifulSoup(r.content, 'html.parser')
                    title = soup.title.string

                    if r.status_code in [200, 302, 304]:
                        file.write('{} - {}\n'.format(url, title))
                        found += 1
                        allsite += 1
                        print("{} [{}]: \033[32mfound {}!\033[0m".format(now(), allsite, url))

                    elif r.status_code in [502, 404, 403]:
                        not_found += 1
                        allsite += 1
                        print("{} [{}]: \033[33mnot found or not available!\033[0m".format(now(), allsite))

                except:
                    exist += 1
                    allsite += 1
                    print("{} [{}]: \033[31msite not exist!\033[0m".format(now(), allsite))

                finally:
                    file.close()
                    time.sleep(0.5)

        except KeyboardInterrupt:
            print("\n--- search statistics ---")
            print("all/found/not/exist = {}/{}/{}/{}".format(allsite, found, not_found, exist))
            break


if __name__ == "__main__":
    main()
