import re
from DoublyConnectedEdgeList import Vertex, Face, HalfEdge
from TrapezoidalMap import Point, LineSegment
from operator import attrgetter
import random

vertex = []
point = []
face = []
halfedge = []
vertex_x = []
vertex_y = []
point_x = []
point_y = []
segment = []
rand_segment = []
vert_segment = []
bound_box = []
'''dictionnary of line segments as key to corresponding value in list of halfedges'''
seg_edg_dict = dict()


def read_file(inputFile):
	file = open(inputFile, "r")
	input = file.readlines()
	file.close()
	parse_subdivision(input)
	vertex_coord(vertex)
	segment_halfedge_dict(seg_edg_dict)
	rm_dup_line_segment(segment)
	sort_line_segment(segment)
	randomize_line_segment(segment)
	bounding_box(bound_box)
	find_vertical_segment(vertex, segment, vert_segment)
	point_coord(point)

'''find x,y coordinates of vertex for ploting'''
def vertex_coord(vtx):
	for v in vtx:
		vertex_x.append(float(v.x))
		vertex_y.append(float(v.y))
		point.append(v.to_point())

def point_coord(pt):
	pt[:] = pt[len(vertex):]
	for p in pt:
		point_x.append(float(p.x))
		point_y.append(float(p.y))

def find_vertical_segment(vtx, seg, segv):
	for v in vtx:
		pt = v.to_point()
		vertical_segment(pt, seg, segv)

def vertical_segment(pt, seg, segv):
	x = pt.x
	y = pt.y
	dist_top = abs(bound_box[3].pry - y)	#distance to top
	dist_bot = abs(bound_box[3].ply - y)	#distance to bot
	for s in seg:
		if s.plx - s.prx == 0: continue	#handle vertical line
		'''find intersection of vertical line of current point with each line segment
		two point form of line: y-y1 = (y2-y1)/(x2-x1) * (x-x1)'''
		x1 = s.plx
		y1 = s.ply
		x2 = s.prx
		y2 = s.pry
		y_on_s = y1 + ((y2-y1)/(x2-x1)) * (x-x1)

		if y_on_s > y and abs(y_on_s - y) < dist_top and x1 < x < x2:
			dist_top = abs(y_on_s - y)
		elif y_on_s < y and abs(y_on_s - y) < dist_bot and x1 < x < x2:
			dist_bot = abs(y_on_s - y)

	p_top = Point(x, y + dist_top)
	p_top.set_idx(len(point))
	point.append(p_top)
	s_top = LineSegment(pt, p_top)
	s_top.set_idx(pt.idx, p_top.idx)
	segv.append(s_top)
	p_bot = Point(x, y - dist_bot)
	p_bot.set_idx(len(point))
	point.append(p_bot)
	s_bot = LineSegment(p_bot, pt)
	s_bot.set_idx(pt.idx, p_bot.idx)
	segv.append(s_bot)
		
'''
Algorithm RANDOMPERMUTATION(A)
Input. An array A[1···n].
Output. The array A[1···n] with the same elements, but rearranged into a random permutation.
1. for k ← n downto 2
2. 	do rndindex ←RANDOM(k)
3. 	Exchange A[k] and A[rndindex].
'''
def randomize_line_segment(seg):
	rand_segment[:] = seg[::]
	for i in range(len(seg)-1, 1, -1):
		rndIdx = random.randint(0, i)
		rand_segment[i], rand_segment[rndIdx] = rand_segment[rndIdx], rand_segment[i]

def rm_dup_line_segment(seg):
	seen = set()
	result = []
	for item in seg:
		if item not in seen:
			seen.add(item)
			result.append(item)
	seg[:] = result

def sort_line_segment(seg):
	# segment.sort(key = lambda x: (x.plx, x.ply, x.prx, x.pry))
	seg.sort(key = attrgetter('plx', 'ply', 'prx', 'pry'))

def read_vertex(line):
	idx = re.search('v(.+?) ', line).group(1)
	x = re.search(' \((.+?),', line).group(1)
	y = re.search(', (.+?)\)', line).group(1)
	es = re.search(' e(.+?),', line).group(1)
	ee = re.search('e\d,(.+?)\n', line).group(1)
	v = Vertex(idx, x, y)
	# vertex.append(v)
	return v

def read_face(line):
	idx = re.search('f(\d) ', line).group(1)
	f = Face(idx)
	return f

def read_halfedge(line):
	vsi = re.search('e(\d),\d v', line).group(1)
	vei = re.search('e\d,(\d) v', line).group(1)
	fi = re.search('f(\d) ', line).group(1)
	vs = vertex[int(vsi)-1]
	ve = vertex[int(vei)-1]
	f = face[int(fi)-1]
	e = HalfEdge(vs, ve, f)
	# halfedge.append(e)
	return e

def parse_subdivision(input):
	for line in input:
		c = line[0]
		if c == 'v':
			v = read_vertex(line)
			vertex.append(v)
		elif c == 'f':
			f = read_face(line)
			face.append(f)
		elif c == 'e':
			e = read_halfedge(line)
			halfedge.append(e)

'''Append multiple values to a key in the given dictionary'''
def add_values_to_dict(target_dict, key, list_of_values):
	if key not in target_dict:
		target_dict[key] = list()
	target_dict[key].extend(list_of_values)
	return target_dict

def segment_halfedge_dict(s_e_dict):
	for edge in halfedge:
		seg = edge.to_line_segment()
		seg_ = seg.__str__()
		edg_ = edge.__str__()
		segment.append(seg)	#add element to segemtns list
		add_values_to_dict(s_e_dict, seg_, [edg_])

def bounding_box(seg):
	# bounding points
	min_x = min(vertex_x)
	max_x = max(vertex_x)
	min_y = min(vertex_y)
	max_y = max(vertex_y)
	offset = 0.1
	offset_x = (max_x - min_x) * offset
	offset_y = (max_y - min_y) * offset
	topl = Point(min_x-offset_x, max_y+offset_y)
	topl.set_idx(-1)
	topr = Point(max_x+offset_x, max_y+offset_y)
	topr.set_idx(-2)
	botr = Point(max_x+offset_x, min_y-offset_y)
	botr.set_idx(-3)
	botl = Point(min_x-offset_x, min_y-offset_y)
	botl.set_idx(-4)
	# bounding line segments
	boundT = LineSegment(topl, topr)
	boundR = LineSegment(botr, topr)
	boundB = LineSegment(botl, botr)
	boundL = LineSegment(botl, topl)
	# add bounding line segments to box
	seg[len(seg):] = [boundB, boundL, boundT, boundR]
	# sort_line_segment(seg)

