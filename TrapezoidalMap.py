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

	def is_left(self, other:Point):
		return other.x < self.x

	def is_right(self, other:Point):
		return self.x < other.x
		
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

	def is_above(self, pt:Point):
		y_on_s = Geometry.y_on_line_segment(self, pt.x)
		return y_on_s < pt.y

	def is_below(self, pt:Point):
		y_on_s = Geometry.y_on_line_segment(self, pt.x)
		return pt.y < y_on_s

	def __str__(self):
		return 's' + self.idx

	def __eq__(self, other):
		return self.pl == other.pl and self.pr == other.pr

	def __hash__(self):
		return hash(('left endpoint', self.pl, 'right endpoint', self.pr))


class Trapezoid:
	def __init__(self, top:LineSegment, bot:LineSegment, left:LineSegment, right:LineSegment):
		self.top = top
		self.bot = bot
		self.right = right
		self.left = left
		self.tl = top.pl
		self.tr = top.pr
		self.bl = bot.pl
		self.br = bot.pr
		# Neighbors of this trapezoid
		self.nbrUL = None
		self.nbrUR = None
		self.nbrLL = None
		self.nbrLR = None

	def set_lower_left_neighbor(self, nbr:Trapezoid):
		self.nbrLL = nbr

	def __str__(self):
		return 't ' + str(self.top) + 'b ' + str(self.bot)

	def __eq__(self, other):
		return self.top == other.top and self.bot == other.bot and \
				self.right == other.right and self.left == other.left

	def __hash__(self):
		return hash(('top', self.top, 'bot ', self.bot, 'right ', self.right, 'left ', self.left))


class Geometry:
	'''find intersection of vertical line of current point with each line segment
	two point form of line: y-y1 = (y2-y1)/(x2-x1) * (x-x1)'''
	def y_on_line_segment(s:LineSegment, x):
		x1 = s.plx
		y1 = s.ply
		x2 = s.prx
		y2 = s.pry
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