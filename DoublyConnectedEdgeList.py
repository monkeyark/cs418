class HalfEdge:
	pass

class Vertex:
	def __init__(self, idx:int, x:float, y:float):
		self.x = x
		self.y = y
		self.idx = idx

	def __call__(self, edge:HalfEdge):
		self.edge = edge
	
	def move(self, x:float, y:float):
		self.x += x
		self.y += y
	
	def equals(self, other):
		if isinstance(other, Vertex):
			return self.x == other.x and self.y == other.y
		return False

	def __str__(self):
		return 'v' + self.idx + ' (' + self.x + ', ' + self.y + ')' + ' e'

class Face:
	def __init__(self, idx:int):
		self.idx = idx

	def __call__(self, edgeout:HalfEdge):
		self.edgeout = edgeout
	
	#TODO edgein should be a list to handle holes
	def __call__(self, edgein:HalfEdge):
		self.edgein = edgein

	def __str__(self):
		return 'f' + self.idx + ' ' + 'e'

class HalfEdge:
	def __init__(self, vs:Vertex, ve:Vertex, face:Face):
		self.vs = vs
		self.ve = ve
		self.face = face

	def __call__(self, face:Face):
		self.face = face

	def __call__(self, next:HalfEdge, prev:HalfEdge):
		self.next = next
		self.prev = prev

	# def __call__(self, psx:float, psy:float, psidx:int, pex:float, pey:float, peidx:int, face:Face):
	# 	self.ps = Vertex(psx, psy, psidx)
	# 	self.pe = Vertex(pex, pey, peidx)
	# 	self.face = face
	
	def twin(self):
		twin = HalfEdge(self.ve, self.vs, self.prev, self.next, self.face.edgeout.face)
		return twin

	def set(self, vs:Vertex, ve:Vertex):
		self.vs = vs
		self.ve = ve

	# def equals(self, edge:HalfEdge):

	def __str__(self):
		return 'e' + self.vs.idx + ',' + self.ve.idx


class DCEL:
	pass

# class Trapezoid:
# 	# starting counterclockwise at the upper left corner top, right, bot, left
# 	def __init__(self, tl:Vertex, tr:Vertex, br:Vertex, bl:Vertex, idx:int, face:Face):
# 		self.top = HalfEdge(tl, tr, face)
# 		self.right = HalfEdge(tr, br, face)
# 		self.bot = HalfEdge(br, bl, face)
# 		self.left = HalfEdge(bl, tl, face)
# 		self.idx = idx
# 		self.face = face

# 	def __init__(self, top:HalfEdge, bot:HalfEdge, right:HalfEdge, left:HalfEdge, face:Face):
# 		self.top = top
# 		self.bot = bot
# 		self.right = right
# 		self.left = left
# 		self.face = face
	
# 	def toString(self):
# 		print('t' , self.idx)

