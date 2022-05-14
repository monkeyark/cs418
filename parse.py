from DoublyConnectedEdgeList import Vertex, Face, HalfEdge, Trapezoid
from DirectedAcyclicGraph import Node, Graph
import re
from operator import attrgetter
import random
from copy import copy, deepcopy

vertex = []
face = []
halfedge = []
segment = []
point = []
vertex_x = []
vertex_y = []
point_x = []
point_y = []
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
	segment[:] = find_twin_halfedge(halfedge)
	vertex_coord(vertex)
	# segment_halfedge_dict(seg_edg_dict)
	# rm_dup_line_segment(segment)
	sort_line_segment(segment)
	rand_segment[:] = randomize_line_segment(segment)
	bounding_box(bound_box)
	find_vertical_segment(vertex, segment, vert_segment)
	point_coord(point)

def face_to_edge(face, edg):
	pass

'''find x,y coordinates of vertex for ploting'''
def vertex_coord(vtx):
	for v in vtx:
		vertex_x.append(float(v.x))
		vertex_y.append(float(v.y))
		point.append(v)

def point_coord(pt):
	pt[:] = pt[len(vertex):]
	for p in pt:
		point_x.append(float(p.x))
		point_y.append(float(p.y))

def find_vertical_segment(vtx, seg, segv):
	for v in vtx:
		vertical_segment(v, seg, segv)

def vertical_segment(pt, seg, segv):
	x = pt.x
	y = pt.y
	dist_top = abs(bound_box[3].pry - y)	#distance to top
	dist_bot = abs(bound_box[3].ply - y)	#distance to bot
	for s in seg:
		if s.plx - s.prx == 0: continue	#handle vertical line
		# y_on_s = Geometry.y_on_line_segment(s, x)
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

	p_top = Vertex(x, y + dist_top, idx=len(point))
	point.append(p_top)
	s_top = HalfEdge(pt, p_top)
	segv.append(s_top)

	p_bot = Vertex(x, y - dist_bot, idx=len(point))
	point.append(p_bot)
	s_bot = HalfEdge(p_bot, pt)
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
	rand_seg = seg[::]
	for i in range(len(seg)-1, 1, -1):
		rndIdx = random.randint(0, i)
		rand_seg[i], rand_seg[rndIdx] = rand_seg[rndIdx], rand_seg[i]
	return rand_seg

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

'''remove twin of all halfedge'''
def find_twin_halfedge(edg):
	tem = deepcopy(edg)
	for i in range(0, len(edg)):
		for j in range(i+1, len(edg)):
			if edg[i].is_twin(edg[j]):
				edg[i].set_twin(edg[j])
				edg[j].set_twin(edg[i])
				tem.remove(edg[j])
	return tem

def read_vertex(line):
	index = re.search('v(.+?) ', line).group(1)
	x = re.search(' \((.+?),', line).group(1)
	y = re.search(', (.+?)\)', line).group(1)
	# es = re.search(' e(.+?),', line).group(1)
	# ee = re.search('e\d,(.+?)\n', line).group(1)
	v = Vertex(x, y, idx=index)
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
	e = HalfEdge(vs, ve, face=f)
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

def bounding_box(box):
	# bounding points
	min_x = min(vertex_x)
	max_x = max(vertex_x)
	min_y = min(vertex_y)
	max_y = max(vertex_y)
	offset = 0.2
	offset_x = (max_x - min_x) * offset
	offset_y = (max_y - min_y) * offset
	topl = Vertex(min_x-offset_x, max_y+offset_y, idx=-1)
	topr = Vertex(max_x+offset_x, max_y+offset_y, idx=-2)
	botr = Vertex(max_x+offset_x, min_y-offset_y, idx=-3)
	botl = Vertex(min_x-offset_x, min_y-offset_y, idx=-4)
	# bounding line segments
	boundT = HalfEdge(topl, topr)
	boundR = HalfEdge(topr, botr)
	boundB = HalfEdge(botr, botl)
	boundL = HalfEdge(botl, topl)
	# add bounding line segments to box
	box[:] = [boundT, boundB, boundL, boundR]
	# sort_line_segment(seg)
	global root
	print(boundT.pl, boundB.pr)
	root_data = Trapezoid(boundT, boundB, boundT.pl, boundB.pr)
	root = Node(data=root_data)


'''Append multiple values to a key in the given dictionary'''
def add_values_to_dict(target_dict, key, list_of_values):
	if key not in target_dict:
		target_dict[key] = list()
	target_dict[key].extend(list_of_values)
	return target_dict

def segment_halfedge_dict(s_e_dict, seg, edg):
	for e in edg:
		seg = e
		seg_ = seg.__str__()
		edg_ = e.__str__()
		add_values_to_dict(s_e_dict, seg_, [edg_])