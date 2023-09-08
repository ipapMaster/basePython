# PIL - Python Imaging Library:
# pip install pillow

from PIL import Image, ImageFilter

try:
    original = Image.open('python.png')
except FileNotFoundError:
    print('Файл не найден')

# pixels = original.load()  # получили массив с пикселями
w, h = original.size  # получили размер в переменных w и h

resized = original.resize((w//2, h//2))
resized.save('thumb.png')


# for x in range(w):
#     for y in range(h):
#         r, g, b = pixels[x, y]
#         pixels[x, y] = g, b, r
#
# original.save('inverted.png')

# contour = original.filter(ImageFilter.CONTOUR)
# contour.save('contour.png')
# cropped = original.crop((195 // 2, 0, 195, 113))
# cropped.save('crop.png')
# blur = original.filter(ImageFilter.BLUR)
# boxblur = original.filter(ImageFilter.BoxBlur(20))
# gaussblur = original.filter(ImageFilter.GaussianBlur(20))
# blur.save('python_blur.png')
# boxblur.save('python_box.png')
# gaussblur.save('python_gauss.png')

print('Параметры изображения:')
print('Формат:', original.format)
print('Размер:', original.size)
print('Цветовая схема:', original.mode)
