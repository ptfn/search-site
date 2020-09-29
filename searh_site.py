import random
import requests
Symbols = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
Length = random.randrange(1,5)
n = 0
Domen = ['.com','.ru','.org','.net']


while n < 10000:
    Password = ''
    Url = ''
    file = open("site.txt",'a+',encoding ='utf-8')

    for i in range(Length):
        Password += random.choice(Symbols)
    
    for i in range(len(Domen)):
        Url = Password + Domen[i]
        Site = 'https://'+ Url
        try:      
            r = requests.get(Site , timeout=10)
            if r.status_code in [200, 302, 304]:
                file.write('{}\n'.format(Url))
                print(Url)
            elif r.status_code in [502, 404, 403]:
                print ("Not Found Or Not Available")
        except:
            print ("Domen Not Exist")
    
    file.close
    n += 1