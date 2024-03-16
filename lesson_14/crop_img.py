from PIL import Image

img = Image.open('img/back.jpg')

new_img = img.resize((800, 600))
new_img.save('img/back1.jpg')
