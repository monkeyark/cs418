class Point:
	pass
class LineSegment:
	pass
class Trapezoid:
	pass
class TrapezoidMap:
	pass

class Point:
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)
		self.idx = None
		
	# def __init__(self, x, y, idx=None, **kwargs):
	# 	self.x = float(x)
	# 	self.y = float(y)
	# 	if idx:
	# 		self.idx = idx
	# 	else:
	# 		self.idx = None
	# 	self.update(kwargs)

	def equals(self, other):
		if (self.__class__ == other.__class__):
			return self.__dict__ == other.__dict__
		return False

	def __same__(self, other):
		if (isinstance(other, Point)):
			return self.x == other.x and self.y == other.y
		return False

	def is_left_of(self, other:Point):
		return self.x < other.x

	def is_right_of(self, other:Point):
		return other.x < self.x
		
	def set_idx(self, idx):
		self.idx = idx

	def __str__(self):
		return '(' + str(self.x) + ', ' + str(self.y) + ')'

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __hash__(self):
		return hash(('x', self.x, 'y', self.y))

class LineSegment:
	def __init__(self, pl:Point, pr:Point):
		self.pl = pl
		self.pr = pr
		self.plx = pl.x
		self.ply = pl.y
		self.prx = pr.x
		self.pry = pr.y
		self.idx = None
		self.parent = None

	def set_parent(self, p:LineSegment):
		self.parent = p

	def set_idx(self, sidx, eidx):
		if sidx < eidx:
			self.idx = str(sidx) + ',' + str(eidx)
		else:
			self.idx = str(eidx) + ',' + str(sidx)

	def print_endpoints(self):
		return str(self.pl) + ' ' + str(self.pr)

	def intersect(self, pt:Point):
		x = pt.x
		x1 = self.plx
		y1 = self.ply
		x2 = self.prx
		y2 = self.pry
		y = y1 + ((y2-y1)/(x2-x1)) * (x-x1)
		return y

	def is_above(self, pt:Point):
		y_on_s = self.intersect(self, pt)
		return y_on_s < pt.y

	def is_below(self, pt:Point):
		y_on_s = self.intersect(self, pt)
		return pt.y < y_on_s

	def __str__(self):
		return 's' + self.idx

	def __eq__(self, other):
		return self.pl == other.pl and self.pr == other.pr

	def __hash__(self):
		return hash(('left endpoint', self.pl, 'right endpoint', self.pr))


class Trapezoid:
	def __init__(self, 
				top:LineSegment, bot:LineSegment, 
				leftp:Point, rightp:Point,
				nbUL = None, nbUR = None, nbLL = None, nbLR = None,
				**kwargs
				):
		self.top = top
		self.bot = bot
		self.rightp = rightp
		self.leftp = leftp
		self.tl = top.pl
		self.tr = top.pr
		self.bl = bot.pl
		self.br = bot.pr
		# Neighbors of this trapezoid
		self.nbUL = kwargs.get('nbUL')
		self.nbUR = kwargs.get('nbUR')
		self.nbLL = kwargs.get('nbLL')
		self.nbLR = kwargs.get('nbLR')

	def set_lower_left_neighbor(self, nbr:Trapezoid):
		self.nbrLL = nbr
	def set_upper_left_neighbor(self, nbr:Trapezoid):
		self.nbrUL = nbr
	def set_lower_right_neighbor(self, nbr:Trapezoid):
		self.nbrLR = nbr
	def set_upper_right_neighbor(self, nbr:Trapezoid):
		self.nbrUR = nbr
	
	def __str__(self):
		return 't ' + str(self.top) + '\nb ' + str(self.bot)

	def __eq__(self, other):
		return self.top == other.top and self.bot == other.bot and \
				self.right == other.right and self.left == other.left

	def __hash__(self):
		return hash(('top', self.top, 'bot ', self.bot, 'rightp ', self.rightp, 'leftp ', self.leftp))

# import networkx as nx
from DirectedAcyclicGraph import Graph
class TrapezoidMap:
	'''
	Algorithm FOLLOWSEGMENT(T,D,si)
	Input. A trapezoidal map T, a search structure D for T, and a new segment si.
	Output. The sequence ∆0,...,∆k of trapezoids intersected by si.
	1. Let p and q be the left and right endpoint of si.
	2. Search with p in the search structure D to find ∆0.
	3. j ← 0;
	4. while q lies to the right of rightp(∆j)
	5. 	do if rightp(∆j) lies above si
	6. 		then Let ∆j+1 be the lower right neighbor of ∆j.
	7. 		else Let ∆j+1 be the upper right neighbor of ∆j.
	8. 	j ← j +1
	9. return ∆0,∆1,...,∆j
	'''
	def follow_segment(graph:Graph, seg:LineSegment):
		trapezoids = []
		pt = seg.pl
		previous = graph.find_point(pt)	#TODO check data type
		trapezoids.append(previous)

		while seg.prx > previous.leftp.x:
			# choose the next trapezoid in the sequence
			if seg.is_above(previous.rightp):	#TODO check condition
				previous = previous.nbLR	#lower right neighbor
			else:
				previous = previous.nbUR	#upper right neighbor
			trapezoids.append(previous)

		return trapezoids


	'''
	Algorithm TRAPEZOIDALMAP(S)
	Input. A set S of n non-crossing line segments.
	Output. The trapezoidal map T(S) and a search structure D for T(S) in a bounding box.
	1. Determine a bounding box R that contains all segments of S, and initialize the trapezoidal map structure T and search structure D for it.
	2. Compute a random permutation s1,s2,...,sn of the elements of S.
	3. for i ← 1 to n
	4. 	do Find the set ∆0,∆1,...,∆k of trapezoids in T properly intersected by si.
	5. 	Remove ∆0,∆1,...,∆k from T and replace them by the new trapezoids that appear because of the insertion of si.
	6. 	Remove the leaves for ∆0,∆1,...,∆k from D, and create leaves for the new trapezoids. Link the new leaves to the existing inner nodes by adding some new inner nodes, as explained below.
	'''
	def build_trapezoid_map(rand_seg, graph, ):
		pass



class Geometry:
	'''find intersection of vertical line of current point with each line segment
	two point form of line: y-y1 = (y2-y1)/(x2-x1) * (x-x1)'''
	def intersect_segment(s:LineSegment, x):
		x1 = s.plx
		y1 = s.ply
		x2 = s.prx
		y2 = s.pry
		y = y1 + ((y2-y1)/(x2-x1)) * (x-x1)
		return y

	def intersect_points(pt1:Point, pt2:Point, x):
		x1 = pt1.x
		y1 = pt1.y
		x2 = pt2.x
		y2 = pt2.y
		y = y1 + ((y2-y1)/(x2-x1)) * (x-x1)
		return y
	
	def sine_theata(stt:Point, end:Point, pt:Point):
		ax = end.x - stt.x
		ay = end.y - stt.y
		bx = pt.x - stt.x
		by = pt.y - stt.y
		sine = ax * by - ay * bx
		return sine

	def is_inside_trapezoid(trap:Trapezoid, pt:Point):
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