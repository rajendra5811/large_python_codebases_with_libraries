import requests
import random

image_url = 'https://images.ctfassets.net/2y9b3o528xhq/4swf2qhcelEUWzKHaKne6C/d890de3220ea332fb42e9b8e5f7848fd/real-world-projects.png'

r = requests.get(image_url)
tmp = f'./tmp/{random.randint(0,100000000)}.png'

with open(tmp, 'wb') as img:
    img.write(r.content)

print(tmp)
""" https://images.ctfassets.net/2y9b3o528xhq/4swf2qhcelEUWzKHaKne6C/d890de3220ea332fb42e9b8e5f7848fd/real-world-projects.png
https://images.ctfassets.net/2y9b3o528xhq/5sXS0Rr3MEr66P5elfYX7P/3728cc2d85c0979cb29d5cb291369038/mentor.jpg
https://images.ctfassets.net/2y9b3o528xhq/5p7HANmA1jsw8P9EVOeVso/cbfa17357399d99a76d641c777e81a81/self-paced.png"""

image_url1 ="https://images.ctfassets.net/2y9b3o528xhq/4swf2qhcelEUWzKHaKne6C/d890de3220ea332fb42e9b8e5f7848fd/real-world-projects.png" 

r1 = requests.get(image_url)
tmp1 = f'./tmp/{random.randint(0,100000000)}.png'

with open(tmp1, 'wb') as img:
    img.write(r.content)

print(tmp1)