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

	def set_idx(self, sidx, eidx):
		if sidx < eidx:
			self.idx = str(sidx) + ',' + str(eidx)
		else:
			self.idx = str(eidx) + ',' + str(sidx)

	def print_endpoints(self):
		return str(self.pl) + ' ' + str(self.pr)

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

	def __str__(self):
		return 't ' + str(self.top) + 'b ' + str(self.bot)

	def __eq__(self, other):
		return self.top == other.top and self.bot == other.bot and \
				self.right == other.right and self.left == other.left

	def __hash__(self):
		return hash(('top', self.top, 'bot ', self.bot, 'right ', self.right, 'left ', self.left))

	def is_inside(self, pt:Point):
		is_inside = True
		on_side = None

		ax = self.top.prx - self.top.plx
		ay = self.top.pry - self.top.ply
		bx = pt.x - self.top.plx
		by = pt.y - self.top.ply
		sine = ax * by - ay * bx
		is_inside = is_inside and (sine <= 0)
		if (sine == 0):
			on_side = 't'
		print(is_inside, sine)

		ax = self.bot.plx - self.bot.prx
		ay = self.bot.ply - self.bot.pry
		bx = pt.x - self.bot.prx
		by = pt.y - self.bot.pry
		sine = ax * by - ay * bx
		is_inside = is_inside and (sine <= 0)
		print(is_inside, sine)

		ax = self.left.prx - self.left.plx
		ay = self.left.pry - self.left.ply
		bx = pt.x - self.left.plx
		by = pt.y - self.left.ply
		sine = ax * by - ay * bx
		is_inside = is_inside and (sine <= 0)
		print(is_inside, sine)

		ax = self.right.plx - self.right.prx
		ay = self.right.ply - self.right.pry
		bx = pt.x - self.right.prx
		by = pt.y - self.right.pry
		sine = ax * by - ay * bx
		is_inside = is_inside and (sine <= 0)
		print(is_inside, sine)

		return is_inside


class TrapezoidMap:
	pass

