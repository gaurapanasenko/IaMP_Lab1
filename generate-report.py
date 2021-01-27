#!/usr/bin/env python3
import os
import base64

dirs = [str(i) for i in os.listdir() if any([i.startswith(j) for j in ('photo', 'screen')])]

dirs.sort()
subdirs = {i: sorted(os.listdir(i)) for i in dirs}

for d, files in subdirs.items():
    for f in files:
        path = os.path.join(d, f)
        with open(path, 'rb') as img:
            print('<h3 id="h3-%s">Файл "%s"</h3><figure>' % (f, f))
            format = f.split('.')[-1]
            data = img.read()
            base = base64.b64encode(data).decode()
            if format == "tiff":
#                print('<div class="tiffy" data-data="%s"></div>' % base)
                print('<div class="tiffy" data-url="%s"></div>' % path)
            else:
#                continue
                print('<img class="image"')
#                print('src="data:image/%s;base64,%s">' % (format, base))
                print('src="%s">' % path)
            print('<figcaption>Файл "%s"; Розмір файлу: %.2f KiB, %s B</figcaption>' % (f, len(data) / 1024, len(data)))
            print("</figure>")
