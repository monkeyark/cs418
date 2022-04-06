from PIL import Image
from PIL import ImageDraw
import random as rnd
import numpy as np
import matplotlib.pyplot as plt

N = 60000
s = (500, 500)

im = Image.new('RGBA', s, (255,255,255,255))
draw = ImageDraw.Draw(im)

for i in range(N):
	x1 = rnd.random() * s[0]
	y1 = rnd.random() * s[1]
	x2 = rnd.random() * s[0]
	y2 = rnd.random() * s[1]
	alpha = rnd.random()
	color  = (int(rnd.random() * 256), int(rnd.random() * 256), int(rnd.random() * 256), int(alpha * 256)) 
	draw.line(((x1,y1),(x2,y2)), fill=color, width=1)

plt.imshow(np.asarray(im),
		origin='lower')
plt.show()