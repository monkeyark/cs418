class Vertex:
	pass
class HalfEdge:
	pass
class Face:
	pass
class Trapezoid:
	pass

class Vertex:
	def __init__(self, x, y, idx=None, edge:HalfEdge=None):
		self.x = float(x)
		self.y = float(y)
		self.idx = int(idx)
		self.edge = edge

	def equals(self, other):
		return isinstance(other, Vertex) and self.x == other.x and self.y == other.y

	def __eq__(self, other):
		return isinstance(other, Vertex) and self.x == other.x and self.y == other.y \
			and self.idx == other.idx #and self.edge == other.edge

	def __hash__(self):
		return hash(('v', self.idx, 'x', self.x, 'y', self.y))

	def __str__(self):
		return 'v' + str(self.idx) + ' (' + str(self.x) + ', ' + str(self.y) + ')' + ' e'

class Face:
	def __init__(self, idx, edgeout:HalfEdge=None, edgein:HalfEdge=None):
		self.idx = int(idx)
		self.edgeout = edgeout
		self.edgein = edgein
		#TODO edgein should be a list to handle holes

	def __eq__(self, other):
		return isinstance(other, HalfEdge) and self.idx == other.idx

	def __hash__(self):
		return hash(('index', self.idx))

	def __str__(self):
		return 'f' + str(self.idx)

class HalfEdge:
	def __init__(self, vs:Vertex, ve:Vertex, face:Face=None, next:HalfEdge=None, prev:HalfEdge=None, twin=None):
		self.vs = vs
		self.ve = ve
		self.idx = str(vs.idx) + ',' + str(ve.idx)
		self.vsx = vs.x
		self.vsy = vs.y
		self.vex = ve.x
		self.vey = ve.y
		self.pl = self.left_vtx()
		self.pr = self.right_vtx()
		self.plx = self.pl.x
		self.ply = self.pl.y
		self.prx = self.pr.x
		self.pry = self.pr.y
		self.face = face
		self.next = next
		self.prev = prev
		self.twin = twin
	
	def twin_edge(self):
		twin = HalfEdge(self.ve, self.vs)
		twin.idx = str(self.ve.idx) + ',' + str(self.ve.idx)
		twin.vsx = self.ve.x
		twin.vsy = self.ve.y
		twin.vex = self.vs.x
		twin.vey = self.vs.y
		twin.prx = self.pl.x
		twin.pry = self.pl.y
		twin.plx = self.pr.x
		twin.ply = self.pr.y
		twin.pl = self.right_vtx()
		twin.pr = self.left_vtx()
		twin.next = self.prev
		twin.prev = self.next
		twin.twin = self
		return twin

	def left_vtx(self):
		vtx = Vertex(self.vex, self.vey, self.vs.idx)
		if self.vsx < self.vex:
			vtx = Vertex(self.vsx, self.vsy, self.vs.idx)
		elif self.vsx == self.vex:
			if self.vsy <= self.vey:
				vtx = Vertex(self.vsx, self.vsy, self.vs.idx)
		return vtx
		
	def right_vtx(self):
		vtx = Vertex(self.vsx, self.vsy, self.vs.idx)
		if self.vsx < self.vex:
			vtx = Vertex(self.vex, self.vey, self.vs.idx)
		elif self.vsx == self.vex:
			if self.vsy <= self.vey:
				vtx = Vertex(self.vex, self.vey, self.vs.idx)
		return vtx

	def intersect(self, pt:Vertex):
		x = pt.x
		x1 = self.plx
		y1 = self.ply
		x2 = self.prx
		y2 = self.pry
		y = y1 + ((y2-y1)/(x2-x1)) * (x-x1)
		return y

	def is_above(self, pt:Vertex):
		y_on_s = self.intersect(self, pt)
		return y_on_s < pt.y

	def is_below(self, pt:Vertex):
		y_on_s = self.intersect(self, pt)
		return pt.y < y_on_s

	def is_twin(self, other):
		return isinstance(other, HalfEdge) and self.vs == other.ve and self.ve == other.vs

	def __eq__(self, other):
		return isinstance(other, HalfEdge) and self.vs == other.vs and self.ve == other.ve

	def __hash__(self):
		return hash(('start vertx', self.vs, 'end vertex', self.ve, 'index', self.idx))

	def __str__(self):
		return 'e' + str(self.vs.idx) + ',' + str(self.ve.idx)

class Trapezoid:
	def __init__(self, 
				top:HalfEdge, bot:HalfEdge, 
				leftp:Vertex, rightp:Vertex,
				nbUL = None, nbUR = None, nbLL = None, nbLR = None,
				**kwargs
				):
		self.top = top
		self.bot = bot
		self.rightp = rightp
		self.leftp = leftp
		# Neighbors of this trapezoid
		self.nbUL = nbUL
		self.nbUR = nbUR
		self.nbLL = nbLL
		self.nbLR = nbLR

	def set_lower_left_neighbor(self, nbr:Trapezoid):
		self.nbrLL = nbr
	def set_upper_left_neighbor(self, nbr:Trapezoid):
		self.nbrUL = nbr
	def set_lower_right_neighbor(self, nbr:Trapezoid):
		self.nbrLR = nbr
	def set_upper_right_neighbor(self, nbr:Trapezoid):
		self.nbrUR = nbr

	def __eq__(self, other):
		return isinstance(other, Trapezoid) and self.top == other.top and self.bot == other.bot and \
				self.rightp == other.rightp and self.leftp == other.leftp

	def __hash__(self):
		return hash(('top', self.top, 'bot ', self.bot, 'rightp ', self.rightp, 'leftp ', self.leftp))
	
	def __str__(self):
		return 't ' + str(self.top) + '\nb ' + str(self.bot)

class Geometry:
	'''find intersection of vertical line of current point with each line segment
	two point form of line: y-y1 = (y2-y1)/(x2-x1) * (x-x1)'''
	def intersect_segment(s:HalfEdge, x):
		x1 = s.plx
		y1 = s.ply
		x2 = s.prx
		y2 = s.pry
		y = y1 + ((y2-y1)/(x2-x1)) * (x-x1)
		return y

	def intersect_points(pt1:Vertex, pt2:Vertex, x):
		x1 = pt1.x
		y1 = pt1.y
		x2 = pt2.x
		y2 = pt2.y
		y = y1 + ((y2-y1)/(x2-x1)) * (x-x1)
		return y
	
	def sine_theata(stt:Vertex, end:Vertex, pt:Vertex):
		ax = end.x - stt.x
		ay = end.y - stt.y
		bx = pt.x - stt.x
		by = pt.y - stt.y
		sine = ax * by - ay * bx
		return sine

	def is_inside_trapezoid(trap:Trapezoid, pt:Vertex):
		is_inside = True

		sine = Geometry.sine_theata(trap.tl, trap.tr, pt)	#top
		is_inside = is_inside and sine <= 0
		print(is_inside, sine)

		sine = Geometry.sine_theata(trap.br, trap.bl, pt)	#bot
		is_inside = is_inside and sine <= 0
		print(is_inside, sine)

		sine = Geometry.sine_theata(trap.bl, trap.tl, pt)	#left
		is_inside = is_inside and sine <= 0
		print(is_inside, sine)

		sine = Geometry.sine_theata(trap.tr, trap.br, pt)	#right
		is_inside = is_inside and sine <= 0
		print(is_inside, sine)

		return is_inside