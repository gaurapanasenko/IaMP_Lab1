#!/usr/bin/env python3
import os
import base64
from collections import defaultdict

dirs = [i for i in os.listdir() if any([i.startswith(j) for j in ('photo', 'screen')])]

subdirs = {i: os.listdir(i) for i in dirs}

quality = {'photo_bin.bmp': 1,
 'photo_bin.gif': 1,
 'photo_bin.jpg': 1,
 'photo_bin.png': 1,
 'photo_bin_25.jpg': 1,
 'photo_bin_75.jpg': 1,
 'photo_bin_85.jpg': 1,
 'photo_bin_lzw.tiff': 1,
 'photo_bin_none.tiff': 1,
 'photo_gray.bmp': 4,
 'photo_gray.gif': 4,
 'photo_gray.jpg': 4,
 'photo_gray.png': 4,
 'photo_gray_16.bmp': 2,
 'photo_gray_16.gif': 2,
 'photo_gray_16.jpg': 2,
 'photo_gray_16.png': 2,
 'photo_gray_16_25.jpg': 1,
 'photo_gray_16_75.jpg': 1,
 'photo_gray_16_85.jpg': 1,
 'photo_gray_16_indexed.png': 2,
 'photo_gray_16_lzw.tiff': 2,
 'photo_gray_16_none.tiff': 2,
 'photo_gray_25.jpg': 3,
 'photo_gray_64.bmp': 3,
 'photo_gray_64.gif': 3,
 'photo_gray_64.jpg': 3,
 'photo_gray_64.png': 3,
 'photo_gray_64_25.jpg': 1,
 'photo_gray_64_75.jpg': 2,
 'photo_gray_64_85.jpg': 2,
 'photo_gray_64_indexed.png': 3,
 'photo_gray_64_lzw.tiff': 3,
 'photo_gray_64_none.tiff': 3,
 'photo_gray_75.jpg': 3,
 'photo_gray_85.jpg': 3,
 'photo_gray_indexed.png': 4,
 'photo_gray_lzw.tiff': 4,
 'photo_gray_none.tiff': 4,
 'photo_true.bmp': 5,
 'photo_true.gif': 4,
 'photo_true.jpg': 5,
 'photo_true.png': 5,
 'photo_true_16.bmp': 2,
 'photo_true_16.gif': 2,
 'photo_true_16.jpg': 2,
 'photo_true_16.png': 2,
 'photo_true_16_25.jpg': 1,
 'photo_true_16_75.jpg': 1,
 'photo_true_16_85.jpg': 1,
 'photo_true_16_indexed.png': 2,
 'photo_true_16_lzw.tiff': 2,
 'photo_true_16_none.tiff': 2,
 'photo_true_25.jpg': 1,
 'photo_true_64.bmp': 3,
 'photo_true_64.gif': 3,
 'photo_true_64.jpg': 3,
 'photo_true_64.png': 3,
 'photo_true_64_25.jpg': 1,
 'photo_true_64_75.jpg': 1,
 'photo_true_64_85.jpg': 2,
 'photo_true_64_indexed.png': 3,
 'photo_true_64_lzw.tiff': 3,
 'photo_true_64_none.tiff': 3,
 'photo_true_75.jpg': 3,
 'photo_true_85.jpg': 4,
 'photo_true_indexed.png': 4,
 'photo_true_lzw.tiff': 5,
 'photo_true_none.tiff': 5,
 'screen_bin.bmp': 3,
 'screen_bin.gif': 3,
 'screen_bin.jpg': 3,
 'screen_bin.png': 3,
 'screen_bin_25.jpg': 1,
 'screen_bin_75.jpg': 2,
 'screen_bin_85.jpg': 2,
 'screen_bin_indexed.png': 3,
 'screen_bin_lzw.tiff': 3,
 'screen_bin_none.tiff': 3,
 'screen_gray.bmp': 5,
 'screen_gray.gif': 5,
 'screen_gray.jpg': 5,
 'screen_gray.png': 5,
 'screen_gray_16.bmp': 5,
 'screen_gray_16.gif': 5,
 'screen_gray_16.jpg': 5,
 'screen_gray_16.png': 5,
 'screen_gray_16_25.jpg': 1,
 'screen_gray_16_75.jpg': 2,
 'screen_gray_16_85.jpg': 3,
 'screen_gray_16_indexed.png': 5,
 'screen_gray_16_lzw.tiff': 5,
 'screen_gray_16_none.tiff': 5,
 'screen_gray_25.jpg': 1,
 'screen_gray_64.bmp': 5,
 'screen_gray_64.gif': 5,
 'screen_gray_64.jpg': 5,
 'screen_gray_64.png': 5,
 'screen_gray_64_25.jpg': 1,
 'screen_gray_64_75.jpg': 2,
 'screen_gray_64_85.jpg': 3,
 'screen_gray_64_indexed.png': 5,
 'screen_gray_64_lzw.tiff': 5,
 'screen_gray_64_none.tiff': 5,
 'screen_gray_75.jpg': 2,
 'screen_gray_85.jpg': 2,
 'screen_gray_indexed.png': 5,
 'screen_gray_lzw.tiff': 5,
 'screen_gray_none.tiff': 5,
 'screen_true.bmp': 5,
 'screen_true.gif': 5,
 'screen_true.jpg': 5,
 'screen_true.png': 5,
 'screen_true_25.jpg': 1,
 'screen_true_75.jpg': 2,
 'screen_true_85.jpg': 3,
 'screen_true_indexed.png': 5,
 'screen_true_lzw.tiff': 5,
 'screen_true_none.tiff': 5}

def def_value():
    return defaultdict(tuple)

def header_template(names):
    print("""<tr>
    <th rowspan=2>Формат</th>
    <th colspan=2>%s</th>
    <th colspan=2>%s</th>
    <th colspan=2>%s</th>
</tr>
<tr>
    <th>розмір</th><th>якість</th><th>розмір</th>
    <th>якість</th><th>розмір</th><th>якість</th>
</tr>""" % names)

info = defaultdict(def_value)

for d, files in subdirs.items():
    for f in files:
        path = os.path.join(d, f)
        sufix = f[len(d):]
        with open(path, 'rb') as img:
            info[sufix][d] = ("h3-%s" % f, len(img.read()) / 1024, quality[f])
            

def print_table(info, photos):
    for sufix, files in info.items():
        print('<tr><th>%s</th>' % sufix)
        for i in photos:
            if files[i]:
                print('<td><a href="#%s">%0.2f</a></td><td>%s</td>' % files[i])
            else:
                print('<td></td><td></td>')
        print("</tr>")

print('<h3 id="photo_true_table">Повноколірне фото</h3><table border=1 width=100%>')
header_template(("Всі відтінки", "64 відтінка", "16 відтінка"))
print_table(info, ["photo_true", "photo_true_64", "photo_true_16"])
print("</table>")
print('<h3 id="photo_gray_table">Фото у відтінках сірого</h3><table border=1 width=100%>')
header_template(("Всі відтінки", "64 відтінка", "16 відтінка"))
print_table(info, ["photo_gray", "photo_gray_64", "photo_gray_16"])
print("</table>")
print('<h3 id="screen_gray_table">Зображення першої сторінки у відтінках сірого</h3><table border=1 width=100%>')
header_template(("Всі відтінки", "64 відтінка", "16 відтінка"))
print_table(info, ["screen_gray", "screen_gray_64", "screen_gray_16"])
print("</table>")
print('<h3 id="other_table">Інші зображення</h3><table border=1 width=100%>')
header_template(("Бінарне фото", "Повноколірний скрін", "Бінарний скрін"))
print_table(info, ["photo_bin", "screen_true", "screen_bin"])
print("</table>")
print('<h3 id="photo_table">Порівняння фото</h3><table border=1 width=100%>')
header_template(("Повноколірне фото", "У відтінках сірого", "Бінарне фото"))
print_table(info, ["photo_true", "photo_gray", "photo_bin"])
print("</table>")
print('<h3 id="sreen_table">Порівняння скріну</h3><table border=1 width=100%>')
header_template(("Повноколірний скрін", "У 16 відтінках сірого", "Бінарний скрін"))
print_table(info, ["screen_true", "screen_gray_16", "screen_bin"])
print("</table>")


