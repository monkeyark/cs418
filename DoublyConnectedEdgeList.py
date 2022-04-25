from TrapezoidalMap import Point, LineSegment

class HalfEdge:
	pass

class Vertex:
	def __init__(self, idx, x, y):
		self.idx = int(idx)
		self.x = float(x)
		self.y = float(y)

	def __call__(self, edge:HalfEdge):
		self.edge = edge
	
	def move(self, x, y):
		self.x += x
		self.y += y
	
	def to_point(self):
		pt = Point(self.x, self.y)
		pt.set_idx(self.idx)
		return pt

	def equals(self, other):
		if isinstance(other, Vertex):
			return self.x == other.x and self.y == other.y
		return False

	def __str__(self):
		return 'v' + str(self.idx) + ' (' + str(self.x) + ', ' + str(self.y) + ')' + ' e'


class Face:
	def __init__(self, idx):
		self.idx = int(idx)

	def __call__(self, edgeout:HalfEdge):
		self.edgeout = edgeout
	
	#TODO edgein should be a list to handle holes
	def __call__(self, edgein:HalfEdge):
		self.edgein = edgein

	def __str__(self):
		return 'f' + str(self.idx) + ' e'

class HalfEdge:
	def __init__(self, vs:Vertex, ve:Vertex, face:Face):
		self.vs = vs
		self.ve = ve
		self.vsx = vs.x
		self.vsy = vs.y
		self.vex = ve.x
		self.vey = ve.y
		self.face = face

	def __call__(self, next:HalfEdge, prev:HalfEdge):
		self.next = next
		self.prev = prev
	
	def twin(self):
		twin = HalfEdge(self.ve, self.vs, self.prev, self.next, self.face.edgeout.face)
		return twin
	
	def left_pt(self):
		pt = Point(self.vex, self.vey)
		pt.set_idx(self.ve.idx)
		if self.vsx < self.vex:
			pt = Point(self.vsx, self.vsy)
			pt.set_idx(self.vs.idx)
		elif self.vsx == self.vex:
			if self.vsy <= self.vey:
				pt = Point(self.vsx, self.vsy)
				pt.set_idx(self.vs.idx)
		return pt
		
	def right_pt(self):
		pt = Point(self.vsx, self.vsy)
		pt.set_idx(self.vs.idx)
		if self.vsx < self.vex:
			pt = Point(self.vex, self.vey)
			pt.set_idx(self.ve.idx)
		elif self.vsx == self.vex:
			if self.vsy <= self.vey:
				pt = Point(self.vex, self.vey)
				pt.set_idx(self.ve.idx)
		return pt

	def to_line_segment(self):
		lp = self.left_pt()
		rp = self.right_pt()
		seg = LineSegment(lp, rp)
		seg.set_idx(self.vs.idx, self.ve.idx)
		return seg

	def set(self, vs:Vertex, ve:Vertex):
		self.vs = vs
		self.ve = ve

	def __str__(self):
		return 'e' + str(self.vs.idx) + ',' + str(self.ve.idx)


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

