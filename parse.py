import re
from DoublyConnectedEdgeList import Vertex, Face, HalfEdge
from TrapezoidalMap import Point, LineSegment
from operator import attrgetter

vertex = []
face = []
halfedge = []
# find x,y cordinates of vertex for ploting
x_values = []
y_values = []
segment = []
rand_segment = []
seg_edg_dict = dict()	# dictionnary of line segments as key to corresponding value in list of halfedges


def readFile(inputFile):
	file = open(inputFile, "r")
	input = file.readlines()
	file.close()

	parseSubDivision(input)

	segment_halfEdge_dict(seg_edg_dict)
	removeDupSegment(segment)
	# segment.sort(key = attrgetter('plx', 'ply', 'prx', 'pry'))
	addBoundingBox(segment)
	sortSegment(segment)

def removeDupSegment(seg):
	seen = set()
	result = []
	for item in seg:
		if item not in seen:
			seen.add(item)
			result.append(item)
	segment[:] = result

def sortSegment(seg):
	# segment.sort(key = lambda x: (x.plx, x.ply, x.prx, x.pry))
	segment.sort(key = attrgetter('plx', 'ply', 'prx', 'pry'))


def readVertex(line):
	idx = re.search('v(.+?) ', line).group(1)
	x = re.search(' \((.+?),', line).group(1)
	y = re.search(', (.+?)\)', line).group(1)
	es = re.search(' e(.+?),', line).group(1)
	ee = re.search('e\d,(.+?)\n', line).group(1)
	v = Vertex(idx, x, y)
	# vertex.append(v)
	return v

def readFace(line):
	idx = re.search('f(\d) ', line).group(1)
	f = Face(idx)
	return f

def readHalfEdge(line):
	vsi = re.search('e(\d),\d v', line).group(1)
	vei = re.search('e\d,(\d) v', line).group(1)
	fi = re.search('f(\d) ', line).group(1)

	vs = vertex[int(vsi)-1]
	ve = vertex[int(vei)-1]
	f = face[int(fi)-1]
	e = HalfEdge(vs, ve, f)
	# halfedge.append(e)
	return e

def parseSubDivision(input):
	for line in input:
		c = line[0]
		if c == 'v':
			v = readVertex(line)
			x_values.append(float(v.x))
			y_values.append(float(v.y))
			vertex.append(v)
		elif c == 'f':
			f = readFace(line)
			face.append(f)
		elif c == 'e':
			e = readHalfEdge(line)
			halfedge.append(e)

'''Append multiple values to a key in the given dictionary'''
def add_values_to_dict(target_dict, key, list_of_values):
	if key not in target_dict:
		target_dict[key] = list()
	target_dict[key].extend(list_of_values)
	return target_dict

def segment_halfEdge_dict(s_e_dict):
	for edge in halfedge:
		seg = edge.toLineSegment()
		seg_ = seg.__str__()
		edg_ = edge.__str__()
		segment.append(seg)	#add element to segemtns list
		add_values_to_dict(s_e_dict, seg_, [edg_])

def addBoundingBox(seg):
	# bounding points
	min_x = min(x_values)
	max_x = max(x_values)
	min_y = min(y_values)
	max_y = max(y_values)
	offset_x = (max_x - min_x) * 0.2
	offset_y = (max_y - min_y) * 0.2
	topl = Point(min_x-offset_x, max_y+offset_y)
	topr = Point(max_x+offset_x, max_y+offset_y)
	botr = Point(max_x+offset_x, min_y-offset_y)
	botl = Point(min_x-offset_x, min_y-offset_y)
	# bounding line segments
	boundT = LineSegment(topl, topr)
	boundR = LineSegment(topr, botr)
	boundB = LineSegment(botr, botl)
	boundL = LineSegment(botl, topl)
	# add bounding line segments to segments list
	# seg[len(seg):] = [boundT, boundR, boundB, boundL]
	seg[len(seg):] = [boundB, boundL, boundT, boundR]