# %%
import parse

parse.read_file("data/subdivision2.txt")

from parse import segment, rand_segment, vert_segment, bound_box, seg_edg_dict, vertex_x, vertex_y, vertex, point, point_x, point_y

# %%
# print(seg_edg_dict)
seg_str = [*seg_edg_dict]
# print(seg_str[0].__ne__)

for s in segment:
	print(s, s.print_endpoints())
print()
for sv in vert_segment:
	print(sv)

ss=str(1,'v')

# use vertical segment find trapezoid
# use new nodes(vertex) and segments to build the dag

# %%
from TrapezoidalMap import Point, LineSegment, Trapezoid, Geometry
from DirectedAcyclicGraph import Node

box_t = bound_box[0]
box_b = bound_box[1]
box_l = bound_box[2]
box_r = bound_box[3]
box_trap = Trapezoid(box_t, box_b, box_t.pl, box_b.pr)
n1 = Node(data = box_trap, parent = segment[0])

print(n1.data, '\n', n1.parent, '\n', n1.left)


# %%
from TrapezoidalMap import Point, LineSegment, Trapezoid, Geometry
import networkx as nx

box_t = bound_box[0]
box_b = bound_box[1]
box_l = bound_box[2]
box_r = bound_box[3]
box_trap = Trapezoid(box_t, box_b, box_t.pl, box_b.pr)

map = nx.DiGraph()
map.add_node(box_trap)

n = [n for n,d in map.in_degree() if d==0]
print(isinstance(n[0], Trapezoid))

# def full_tree_pos(G):
# 	n = G.number_of_nodes()
# 	if n == 0 : return {}
# 	# Set position of root
# 	pos = {0:(0.5,0.9)}
# 	if n == 1:
# 		return pos
# 	# Calculate height of tree
# 	i = 1
# 	while(True):
# 		if n >= 2**i and n<2**(i+1):
# 			height = i 
# 			break
# 		i+=1
# 	# compute positions for children in a breadth first manner
# 	p_key = 0
# 	p_y = 0.9
# 	p_x = 0.5
# 	l_child = True # To indicate the next child to be drawn is a left one, if false it is the right child
# 	for i in xrange(height):
# 		for j in xrange(2**(i+1)):
# 			if 2**(i+1)+j-1 < n:
# 				print 2**(i+1)+j-1
# 				if l_child == True:
# 					pos[2**(i+1)+j-1] = (p_x - 0.2/(i*i+1) ,p_y - 0.1)
# 					G.add_edge(2**(i+1)+j-1,p_key)
# 					l_child = False
# 				else:
# 					pos[2**(i+1)+j-1] = (p_x + 0.2/(i*i+1) ,p_y - 0.1)
# 					l_child = True
# 					G.add_edge(2**(i+1)+j-1,p_key)
# 					p_key += 1
# 					(p_x,p_y) = pos[p_key]

# 	return pos

import matplotlib.pyplot as plt
pos = nx.nx_agraph.graphviz_layout(map, prog="dot")
nx.draw_networkx(map, pos=pos, with_labels=True)
plt.show()



# %%
import networkx as nx
import matplotlib.pyplot as plt

map = nx.DiGraph()

for n in rand_segment:
	map.add_node(n)

# from TrapezoidalMap import Point, LineSegment, Trapezoid, Geometry
from TrapezoidalMap import Trapezoid as Trap
box_t = bound_box[0]
box_b = bound_box[1]
box_l = bound_box[2]
box_r = bound_box[3]
box_trap = Trap(box_t, box_b, box_t.pl, box_b.pr)
map.add_node(box_trap)

for i in range(len(rand_segment)-1):
	map.add_edge(rand_segment[i], rand_segment[i+1])


leaf = [x for x in map.nodes() if map.out_degree(x)==0]
print(leaf[0])
pred = map.predecessors(leaf[0])
print(list(pred)[0])

# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.add_edge(3, 4)
# g.add_edge(1, 4)
# g.add_edge(1, 5)
# g.add_edge(5, 6)
# g.add_edge(5, 7)
# g.add_edge(4, 8)
# g.add_edge(3, 8)

# g.add_edge(5, 6)
# g.remove_node(6)
# g.add_node(6)
pos = nx.nx_agraph.graphviz_layout(map, prog="dot")
nx.draw_networkx(map, pos=pos, with_labels=True)
plt.show()


# %%
import pylab as pl
import matplotlib.pyplot as plt
import matplotlib.collections as mc

fig, ax = pl.subplots()

segment_vertical_plot = []
'''vertical lines'''
for s in vert_segment:
	stt = (s.plx, s.ply)
	end = (s.prx, s.pry)
	segment_vertical_plot.append([stt, end])
ax.add_collection(mc.LineCollection(segment_vertical_plot, linestyles='dashed', colors=('black')))

'''line segments'''
segment_plot = []
for s in segment:
	stt = (s.plx, s.ply)
	end = (s.prx, s.pry)
	segment_plot.append([stt, end])
ax.add_collection(mc.LineCollection(segment_plot, colors=('blue')))

'''bounding box'''
bound_box_plot = []
for s in bound_box:
	stt = (s.plx, s.ply)
	end = (s.prx, s.pry)
	bound_box_plot.append([stt, end])
ax.add_collection(mc.LineCollection(bound_box_plot, colors=('black')))

ax.set_xlim(0, 10)
ax.autoscale()
ax.margins(0.1)

for v in parse.vertex:
	plt.text(v.x-0.015, v.y+0.25, "v"+str(v.idx))
plt.scatter(vertex_x, vertex_y, color="red", s=50)

for p in parse.point:
	plt.text(p.x-0.15, p.y-0.5, "p"+str(p.idx))
plt.scatter(point_x, point_y, color="green", s=20)

# plt.savefig('trapzodialMap.png', dpi=1000)
plt.show()

# %%
import networkx as nx
import matplotlib.pyplot as plt

def create_DAG(dag):
	graph = nx.DiGraph()
	for v in dag.keys():
		graph.add_node(v)
	for n in dag.items():
		for w in n[1]:
			# print("n[0]: ", n[0], " | n[1]:", n[1], "w: ", w)
			graph.add_edge(n[0], w)
	return graph

dag = {
	's1': ['v', 't1','w'],
	's2': ['t1','s1'],
	's3': ['v','w'],
	's4': ['x','y'],
	'x': ['v','w'],
	'v': ['t1', 'w'],
	'w': ['y','t1','t2'],
	'y': ['v','t1','t2'],
	't1': [],
	't2': []
	}

map = create_DAG(dag)
pos = nx.nx_agraph.graphviz_layout(map, prog="dot")
nx.draw_networkx(map, pos=pos, with_labels=True)
plt.show()

# leaf = [x for x in map.nodes() if map.out_degree(x)==0 and map.in_degree(x)==2]
leaf = [x for x in map.nodes() if map.out_degree(x)==0]

print(leaf)




