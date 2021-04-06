import os
import requests

from bs4 import BeautifulSoup

"""""""""""""""""""""""""""""""""
    DOWNLOAD IMAGES TO FOLDER
"""""""""""""""""""""""""""""""""

def image_download(search, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass

    os.chdir(os.path.join(os.getcwd(), folder))

    topic = search.replace(' ', '+')

    x = 1
    page_number = 0

    while True:
        url = 'https://imgur.com/search/score/all/page/' + str(page_number) + '?scrolled&q=' + topic + '&q_size_is_mpx=off'

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        images = soup.find_all('img')
        page_number = page_number + 1

        if images:
            print('----------------------------------------------------------------------------------------------')
            print('[PAGE #' + str(page_number) + '] ' + url)
            print('----------------------------------------------------------------------------------------------')

            for image in images:
                img_source = image['src']

                if img_source == '//s.imgur.com/images/loaders/ddddd1_181817/48.gif':
                    continue

                with open(str(x) + '.jpg', 'wb') as f:
                    im = requests.get('https:' + img_source + '?')
                    f.write(im.content)
                    print('DOWNLOADING IMG #' + str(x) + '... [' + img_source + ']')
                    x = int(x) + 1
        else:
            break
    
    print('----------------------------------------------------------------------------------------------')
    print('DOWNLOAD COMPLETE')
    print('----------------------------------------------------------------------------------------------')

image_download(input('Search: '), input('Folder Name: '))