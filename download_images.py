# script to download images from google

# example link: https://cdn.mos.cms.futurecdn.net/ntFmJUZ8tw3ULD3tkBaAtf.jpg 

import wget

def downloads():
    value = input("Please enter png image url:")
    image_filename = wget.download(value)
    print(image_filename)
    return "Successfully Downloaded Image"

print(downloads())