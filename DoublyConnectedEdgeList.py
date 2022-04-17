class HalfEdge:
	pass

class Vertex:
	def __init__(self, idx:int, x:float, y:float, edge:HalfEdge):
		self.x = x
		self.y = y
		self.idx = idx
		self.edge = edge
	
	def move(self, x:float, y:float):
		self.x += x
		self.y += y
	
	def equals(self, other):
		if isinstance(other, Vertex):
			return self.x == other.x and self.y == other.y
		return False

	def toString(self):
		print('v' , self.idx , ' (' , self.x , ', ' , self.y , ')' , ' e' , self.edge)

#  TODO  need to work on the edge list
class Face:
	def __init__(self, idx:int, edgein:HalfEdge, edgeout:HalfEdge):
		self.idx = idx
		self.edgein = edgein
		self.edgeout = edgeout
	# add edge and delete
	def toString(self):
		print('f' , self.idx , ' e' , self.edgein, ' e' , self.edgeout)

class HalfEdge:
	def __init__(self, ps:Vertex, pe:Vertex, next:HalfEdge, prev:HalfEdge, face:Face):
		self.ps = ps
		self.pe = pe
		self.next = next
		self.prev = prev
		self.face = face #TODO add the traversal list

	def __init__(self, psx:float, psy:float, psidx:int, pex:float, pey:float, peidx:int, face:Face):
		self.ps = Vertex(psx, psy, psidx)
		self.pe = Vertex(pex, pey, peidx)
		self.face = face
	
	def twin(self):
		twin = HalfEdge(self.pe, self.ps, self.prev, self.next, self.face.edgeout.face)
		return twin

	def set(self, ps:Vertex, pe:Vertex):
		self.ps = ps
		self.pe = pe
	# def equals(self, edge:HalfEdge):

	def toString(self):
		print('e' , self.ps.x , )

class DCEL:
	pass

# v1 (0, 0) e1,2
# v2 (1, 0) e2,3
# v3 (0, 1) e3,1

# f1 e2,3 nil
# f2 nil e1,3

# e1,2 v1 e2,1 f1 e2,3 e3,1
# e2,1 v2 e1,2 f2 e1,3 e3,2
# e1,3 v1 e3,1 f2 e3,2 e2,1
# e3,1 v3 e1,3 f1 e1,2 e2,3
# e2,3 v2 e3,2 f1 e3,1 e1,2
# e3,2 v3 e2,3 f2 e2,1 e1,3


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

