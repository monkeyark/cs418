class Point:
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)

	def equals(self, other):
		if (self.__class__ == other.__class__):
			return self.__dict__ == other.__dict__
		return False

	def __same__(self, other):
		if (isinstance(other, Point)):
			return self.x == other.x and self.y == other.y
		return False

	def __str__(self):
		return '(' + str(self.x) + ', ' + str(self.y) + ')'

class LineSegment:
	def __init__(self, pl:Point, pr:Point):
		self.pl = pl
		self.pr = pr
		self.plx = pl.x
		self.ply = pl.y
		self.prx = pr.x
		self.pry = pr.y

	def equals(self, other):
		if (self.__class__ == other.__class__):
			return self.pl.equals(other.pl) and self.pr.equals(other.pr)
		return False

	def __str__(self):
		return str(self.pl) + ' ' + str(self.pr)

class Trapezoid:
	pass


class TrapezoidMap:
	pass

