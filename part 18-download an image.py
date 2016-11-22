import _random

import urllib.request

def download_image(url):

    name= "ko1"
    full_name=str(name)+".jpg"
    urllib.request.urlretrieve(url, full_name)


download_image("https://images2.alphacoders.com/714/thumb-1920-714923.jpg")