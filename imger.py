import glob
from bs4 import BeautifulSoup, Tag # type: ignore
import requests

files = glob.glob('species/*.html')
imgs = glob.glob('species/imgs/*')
imgs = [img.split('/')[-1] for img in imgs]

for file in files:
    f = open(file, 'r')
    soup = BeautifulSoup(f, 'html.parser')
    f.close()
    img = soup.find('img')
    if img is not None and isinstance(img, Tag):
        src = img.get('src')
        # print(src)
        name = file.split('/')[-1].split('.')[0]
        candidates = [img for img in imgs if name in img]
        if len(candidates) == 1:
            img['src'] = f'/species/imgs/{candidates[0]}'
        else:
            # set img['src'] to candidate that is not .png
            for candidate in candidates:
                if '.png' not in candidate:
                    img['src'] = f'/species/imgs/{candidate}'
                    break
        with open(f'test/{file}', 'w') as f:
            f.write(str(soup))