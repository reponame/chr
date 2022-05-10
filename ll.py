from lxml import html
from requests import get
from random import choice
from PIL import Image

def getRandomImage():
	search = ('дебил', 'придурок', 'ебанутый', 'дегенерат', 'еблан')

	tree = html.fromstring(get('https://yandex.kz/images/search?text=' + choice(search)).content)
	with open('image.jpg', 'wb') as f:
		f.write(get('http://' + choice(tree.xpath('//img/@src')).split('//')[1]).content)

getRandomImage()
Image.open('image.jpg').resize((15000, 15000), Image.ANTIALIAS).save('image.png', 'PNG')