import re
from DoublyConnectedEdgeList import Vertex, Face, HalfEdge

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

	# the face outside bounding box
	face_out = Face(str(len(face)))
	# bounding vertice
	min_x = min(x_values)
	max_x = max(x_values)
	min_y = min(y_values)
	max_y = max(y_values)
	offset_x = (max_x - min_x) * 0.2
	offset_y = (max_y - min_y) * 0.2
	topl = Vertex(len(vertex)+1, min_x-offset_x, max_y+offset_y)
	topr = Vertex(len(vertex)+2, max_x+offset_x, max_y+offset_y)
	botr = Vertex(len(vertex)+3, max_x+offset_x, min_y-offset_y)
	botl = Vertex(len(vertex)+4, min_x-offset_x, min_y-offset_y)

	# bounding edges
	boundT = HalfEdge(topl, topr, face_out)
	boundR = HalfEdge(topr, botr, face_out)
	boundB = HalfEdge(botr, botl, face_out)
	boundL = HalfEdge(botl, topl, face_out)

	halfedge[len(halfedge):] = [boundT, boundR, boundB, boundL]

	segment_halfEdge_dict()
	print('dictionary in parse', seg_edg_dict)
	# getSegment()
	segment.append([*seg_edg_dict])


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

def segment_halfEdge_dict():
	for edge in halfedge:
		seg = edge.toLineSegment()
		seg_ = seg.__str__()
		edg_ = edge.__str__()
		add_values_to_dict(seg_edg_dict, seg_, [edg_])
