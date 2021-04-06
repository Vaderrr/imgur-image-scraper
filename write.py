import os
import requests

from bs4 import BeautifulSoup

"""""""""""""""""""""""""""""""""
    WRITE LINK  TO .TXT FILE
"""""""""""""""""""""""""""""""""

def image_write_text(search, folder):
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

            text_file = open(topic + '.txt', 'a')

            for image in images:
                img_source = image['src']

                if img_source == '//s.imgur.com/images/loaders/ddddd1_181817/48.gif':
                    continue

                text_file.write(img_source + '\n')
                print('WRITING IMG #' + str(x) + ' [' + img_source + '] TO FILE ...')
                x = int(x) + 1
        else:
            break

    print('----------------------------------------------------------------------------------------------')
    print('WRITING COMPLETE')
    print('----------------------------------------------------------------------------------------------')

image_write_text(input('Search: '), input('Folder Name: '))