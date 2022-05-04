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

	def is_letf_of(self, pt:Vertex):
		return self.x < pt.x

	def is_right_of(self, pt:Vertex):
		return self.x > pt.x

	def equals(self, other):
		return isinstance(other, Vertex) and self.x == other.x and self.y == other.y

	def __eq__(self, other):
		return isinstance(other, Vertex) and self.x == other.x and self.y == other.y \
			and self.idx == other.idx #and self.edge == other.edge

	def __hash__(self):
		return hash(('v', self.idx, 'x', self.x, 'y', self.y))

	def __str__(self):
		# return 'v' + str(self.idx) + ' (' + str(self.x) + ', ' + str(self.y) + ')'
		return 'v' + str(self.idx) + ' (' + "{:.1f}".format(self.x) + ', ' + "{:.1f}".format(self.y) + ')'


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
	def __init__(self, vs:Vertex, ve:Vertex, face=None, next:HalfEdge=None, prev:HalfEdge=None, twin=None):
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
	
	def set_twin(self, twin:HalfEdge):
		self.twin = twin

	# def left_vtx(self):
	# 	vtx = Vertex(self.vex, self.vey, self.ve.idx)
	# 	if self.vsx < self.vex:
	# 		vtx = Vertex(self.vsx, self.vsy, self.vs.idx)
	# 	elif self.vsx == self.vex:
	# 		if self.vsy <= self.vey:
	# 			vtx = Vertex(self.vsx, self.vsy, self.vs.idx)
	# 	return vtx
		
	# def right_vtx(self):
	# 	vtx = Vertex(self.vsx, self.vsy, self.vs.idx)
	# 	# vtx = Vertex(self.vex, self.vey, self.ve.idx)
	# 	if self.vsx < self.vex:
	# 		vtx = Vertex(self.vex, self.vey, self.ve.idx)
	# 	elif self.vsx == self.vex:
	# 		if self.vsy <= self.vey:
	# 			vtx = Vertex(self.vex, self.vey, self.ve.idx)
	# 	return vtx

	def left_vtx(self):
		vtx = self.ve
		if self.vsx < self.vex:
			vtx = self.vs
		elif self.vsx == self.vex:
			if self.vsy <= self.vey:
				self.vs
		return vtx
		
	def right_vtx(self):
		vtx = self.vs
		if self.vsx < self.vex:
			vtx = self.ve
		elif self.vsx == self.vex:
			if self.vsy <= self.vey:
				vtx = self.ve
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
		y_on_s = self.intersect(pt)
		return y_on_s < pt.y

	def is_below(self, pt:Vertex):
		y_on_s = self.intersect(pt)
		return pt.y < y_on_s

	def is_twin(self, other):
		return isinstance(other, HalfEdge) and self.vs == other.ve and self.ve == other.vs

	def __eq__(self, other):
		return isinstance(other, HalfEdge) and self.vs == other.vs and self.ve == other.ve

	def __hash__(self):
		return hash(('start vertx', self.vs, 'end vertex', self.ve, 'index', self.idx))

	def __str__(self):
		# return 'e' + str(self.vs.idx) + ',' + str(self.ve.idx)
		return 'e' + self.idx

class Trapezoid:
	def __init__(self, 
				top:HalfEdge, bot:HalfEdge, leftp:Vertex, rightp:Vertex,
				nbUL = None, nbUR = None, nbLL = None, nbLR = None,
				**kwargs
				):
		self.top = top
		self.bot = bot
		self.leftp = leftp
		self.rightp = rightp
		# Neighbors of this trapezoid
		self.nbUL = nbUL
		self.nbUR = nbUR
		self.nbLL = nbLL
		self.nbLR = nbLR

	def set_lower_left_neighbor(self, nbr:Trapezoid):
		self.nbrLL = nbr
	def set_lower_right_neighbor(self, nbr:Trapezoid):
		self.nbrLR = nbr
	def set_upper_left_neighbor(self, nbr:Trapezoid):
		self.nbrUL = nbr
	def set_upper_right_neighbor(self, nbr:Trapezoid):
		self.nbrUR = nbr
	def is_zero_width(self):
		return self.leftp.x == self.rightp.x
	def is_zero_height_left(self):
		return self.top.ply == self.bot.ply
	def is_zero_height_right(self):
		return self.top.pry == self.bot.pry

	def __eq__(self, other):
		return isinstance(other, Trapezoid) and self.top == other.top and self.bot == other.bot and \
				self.rightp == other.rightp and self.leftp == other.leftp

	def __hash__(self):
		return hash(('top', self.top, 'bot ', self.bot, 'rightp ', self.rightp, 'leftp ', self.leftp))
	
	def __str__(self):
		return '(t: ' + str(self.top) + ', ' + 'b: ' + str(self.bot) + ')\n' + '(l: v' + str(self.leftp.idx) + ', ' + 'r: v' + str(self.rightp.idx) + ')'

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

class Node:
	pass
class Graph:
	pass

class Node:
	def __init__(self, parent=None, left=None, right=None, data=None):
		self.parent = parent
		self.left = left
		self.right = right
		self.data = data
		self.path = list()
	
	def set_parent(self, parent:Node):
		self.parent = parent
		self.path.append(parent)
	
	def set_children(self, l:Node, r:Node):
		self.left = l
		self.right = r
		l.set_parent(self)
		r.set_parent(self)

	def set_left_child(self, l:Node):
		self.left = l
		l.set_parent(self)

	def set_right_child(self, r:Node):
		self.right = r
		r.set_parent(self)

	def add_to_path(self, node:Node):
		self.path.append(node)

	def set_data(self, data):
		self.data = data

	def __eq__(self, other):
		return isinstance(other, Node) and self.data == other.data

	def __hash__(self):
		return hash(('parent', self.parent, 'left', self.left, 'right', self.right, 'data', self.data))

	def __str__(self):
		# if isinstance(self.data, Trapezoid):
		# 	return 'node: ' + str(type(self.data)) + '\n' + str(self.data)
		# else:
		# 	return 'node: ' + str(type(self.data)) + '\n' + str(self.data)
		return 'node: ' + str(type(self.data)) + '\n' + str(self.data)
			# return 'node:\n' + str(self.data) + '\n' + 'lchild ' + str(self.left) + ' rchild ' + str(self.right) + '\n'

		# return 'node:\n' + str(self.data) + '\n' + 'lchild ' + str(self.left) + ' rchild ' + str(self.right) + '\n'
