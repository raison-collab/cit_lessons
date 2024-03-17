from PIL import Image

img = Image.open('img/osel.png')

new_img = img.resize((70, 50))
new_img.save('img/osel.png')
