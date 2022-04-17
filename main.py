# from PIL import Image
# from PIL import ImageDraw
# import random as rnd
# import numpy as np
# import matplotlib.pyplot as plt

inputFile = "subdivision1.txt"
f = open(inputFile, "r")

print(f.readlines())
f.close()

from DoublyConnectedEdgeList import Vertex, Face, HalfEdge

v1 = Vertex(1, 2, 0, 'e1')
v2 = Vertex(2, 3, 1, 4)
# v1.toString()
# v2.toString()

# N = 60000
# s = (500, 500)

# im = Image.new('RGBA', s, (255,255,255,255))
# draw = ImageDraw.Draw(im)

# for i in range(N):
# 	x1 = rnd.random() * s[0]
# 	y1 = rnd.random() * s[1]
# 	x2 = rnd.random() * s[0]
# 	y2 = rnd.random() * s[1]
# 	alpha = rnd.random()
# 	color  = (int(rnd.random() * 256), int(rnd.random() * 256), int(rnd.random() * 256), int(alpha * 256)) 
# 	draw.line(((x1,y1),(x2,y2)), fill=color, width=1)

# plt.imshow(np.asarray(im),
# 		origin='lower')
# plt.show()


# xs = np.linspace(-np.pi, np.pi, 30)
# ys = np.sin(xs)
# markers_on = [12, 17, 18, 19]
# plt.plot(xs, ys, '-gD', markevery=markers_on, label='line with select markers')
# plt.legend()
# plt.show()