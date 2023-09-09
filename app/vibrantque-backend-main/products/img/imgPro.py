from rembg  import remove
from PIL import Image

img = Image.open ('C:\PravinJ\vividobots\Backend\vividobots\products\img\img.png')
R=remove(img)
R.save("img1.png")

