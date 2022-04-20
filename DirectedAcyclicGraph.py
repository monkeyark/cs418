# Algorithm TRAPEZOIDALMAP(S)
# Input. A set S of n non-crossing line segments.
# Output. The trapezoidal map T(S) and a search structure D for T(S) in a bounding box.
# 1. Determine a bounding box R that containims all segments of S, and initialize the trapezoidal map structure T and search structure D for it.
# 2. Compute a random permutation s1,s2,...,sn of the elements of S.
# 3. for i ← 1 to n
# 4. do Find the set ∆0,∆1,...,∆k of trapezoids in T properly intersected by si.
# 5. Remove ∆0,∆1,...,∆k from T and replace them by the new trapezoids that appear because of the insertion of si.
# 6. Remove the leaves for ∆0,∆1,...,∆k from D, and create leaves for the new trapezoids. Link the new leaves to the existing inner nodes by adding some new inner nodes, as explained below.


# Algorithm FOLLOWSEGMENT(T,D,si)
# Input. A trapezoidal map T, a search structure D for T, and a new segment si.
# Output. The sequence ∆0,...,∆k of trapezoids intersected by si.
# 1. Let p and q be the left and right endpoint of si.
# 2. Search with p in the search structure D to find ∆0.
# 3. j ← 0;
# 4. while q lies to the right of rightp(∆j)
# 5. do if rightp(∆j) lies above si
# 6. then Let ∆j+1 be the lower right neighbor of ∆j.
# 7. else Let ∆j+1 be the upper right neighbor of ∆j.
# 8. j ← j +1
# 9. return ∆0,∆1,...,∆j


# Algorithm RANDOMPERMUTATION(A)
# Input. An array A[1···n].
# Output. The array A[1···n] with the same elements, but rearranged into a random permutation.
# 1. for k ← n downto 2
# 2. do rndindex ←RANDOM(k)
# 3. Exchange A[k] and A[rndindex].

class Point:
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)

	def __str__(self):
		return 'p (' + str(self.x) + ', ' + str(self.y) + ')'

class LineSegment:
	def __init__(self, pl:Point, pr:Point):
		self.pl = pl
		self.pr = pr

	def __str__(self):
		return str(self.pl) + ' ' + str(self.pr)