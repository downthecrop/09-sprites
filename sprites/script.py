from wand.image import Image

# Open an image file
with Image(filename='sprite_6.png') as img:
  img.format = 'jpeg'
  img.save(filename='sprite_6.jpg')
