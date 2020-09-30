import random
import requests

Symbols = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
Length = random.randrange(1,5)
Root = ['.com', '.ru', '.org', '.net']
n = 0

while n < 100:
    Domain = ''
    Url = ''
    n += 1
    
    file = open("site.txt", 'a+', encoding = 'utf-8')

    for i in range(Length):
        Domain += random.choice(Symbols)

    for i in range(len(Root)):
        Url = 'https://' + Domain + Root[i]
        try:      
            r = requests.get(Url, timeout = 10)
            if r.status_code in [200, 302, 304]:
                file.write('{}\n'.format(Url))
                print(Url)
            elif r.status_code in [502, 404, 403]:
                print ("Not found or not available")
        except:
            print ("Domain not exist")

    file.close()
