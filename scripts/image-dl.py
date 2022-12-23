import requests
import os

image_url = ''
user_ids = ['']

osu = False

if osu:
    for id in user_ids:       
        response = requests.get(f'{image_url}{id}')
        if response.status_code:
            fp = open(f'./output/{id}.jpg', 'wb')
            fp.write(response.content)
            fp.close()
        else:
            print(f'There was an issue downloading the pfp for {id}!')
else:
    response = requests.get(image_url)
    if response.status_code:
        fp = open(f'', 'wb')
        fp.write(response.content)
        fp.close()
    else:
        print('There was a problem downloading this picture.')