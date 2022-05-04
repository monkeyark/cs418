# import networkx as nx
from DoublyConnectedEdgeList import Vertex, Face, HalfEdge, Trapezoid
from DirectedAcyclicGraph import Node, Graph
# import parse
# parse.read_file("data/subdivision2.txt")
# from parse import segment, halfedge, rand_segment, vert_segment, bound_box, vertex_x, vertex_y, vertex, point, point_x, point_y


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
	def __init__(self, root):
		self.root = root
		self.leaf = []

	def follow_segment(self, seg:HalfEdge):
		trapezoids = []
		pt = seg.pl	#find with the left point
		previous = TrapezoidMap.find_point(self.root, pt)
		trapezoids.append(previous)
		#TODO
		# print('prev: ', previous)
		# print('data: ', previous.data)

		
		while seg.prx > previous.data.rightp.x:
			# choose the next trapezoid in the sequence
			if seg.is_above(previous.data.rightp):	#TODO check condition
				previous.data = previous.data.nbLR	#lower right neighbor
			else:
				previous.data = previous.data.nbUR	#upper right neighbor
			trapezoids.append(previous)
		# print(trapezoids)
		return trapezoids

	def find_point(start:Node, pt:Vertex):
		node = start
		while isinstance(node.data, Trapezoid) == False:
			if isinstance(node.data, Vertex):
				if pt.is_letf_of(node.data):	#go to left child
					node = node.left
				elif pt.is_right_of(node.data):	#go to right child
					node = node.right
				else:
					print(pt, node, ' has same x-value')
			elif isinstance(node.data, HalfEdge):
				if node.data.is_below(pt):
					node = node.left
				elif node.data.is_above(pt):
					node = node.right
				else:
					print(pt, ' lies on ', node)
			else:	# we find the Trapezoid
				pass
		# print('we find the Trapezoid: ', node)
		return node

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
	def build_trapezoid_map(self, seg):
		# seg = rand_seg[:idx]
		vertex = []
		for s in seg:
			vertex.append(s.vs)
			vertex.append(s.ve)

			leaf = TrapezoidMap.follow_segment(self, s)
			if len(leaf) == 1:	#the segment lies within a trapezoid, no intersetction
				old_node = leaf[0]
				old_trap = old_node.data
				new_trap_t = Trapezoid(old_trap.top, s, s.pl, s.pr)
				new_trap_b = Trapezoid(s, old_trap.bot, s.pl, s.pr)
				new_trap_l = Trapezoid(old_trap.top, old_trap.bot, old_trap.leftp, s.pl)
				new_trap_r = Trapezoid(old_trap.top, old_trap.bot, s.pr, old_trap.rightp)
				#create node for new trapezoids
				node_t = Node(data=new_trap_t)
				node_b = Node(data=new_trap_b)
				node_l = Node(data=new_trap_l)
				node_r = Node(data=new_trap_r)
				#create node for inserted segment itself and its left, rigth endpoint
				node_ss = Node(data=s)
				node_sl = Node(data=s.pl)
				node_sr = Node(data=s.pr)
				#link nodes for the trapezoids map
				if (node_t.data.is_zero_width() == False) and (node_r.data.is_zero_width() == False):
					node_sl.set_children(node_l, node_sr)
					node_sr.set_children(node_ss, node_r)
					node_ss.set_children(node_t, node_b)
					if old_node.parent == None:
						self.root = node_sl
					else:
						path = old_node.path
						for p in path:
							if p.left == old_node:
								p.set_left_child(node_sl)
							else:
								p.set_right_child(node_sl)

				# print('------------find 1 leaf:   ', self.root.left, "\n======\n", self.root.right, '------------')
				TrapezoidMap.set_upper_link(old_trap.nbUL, new_trap_t)
				TrapezoidMap.set_upper_link(new_trap_t, old_trap.nbUR)
				TrapezoidMap.set_lower_link(old_trap.nbLL, new_trap_b)
				TrapezoidMap.set_lower_link(new_trap_b, old_trap.nbLR)
			else:	#the segment intersects multiple trapezoids
				top_intersect_trap = []
				bot_intersect_trap = []
				for i in range(0, len(leaf)):
					if i == 0:
						# first trapezoid divided to 3 part
						pass
					elif i == len(leaf)-1:
						# last trapezoid divided to 3 part
						pass
					else:
						# trapezoid divided to 2 part, upper and lower
						pass
					pass
				for i in range(0, len(leaf)):
					# merge 
					pass
		return vertex
		


	def set_upper_link(l:Trapezoid, r:Trapezoid):
		if l != None:
			l.set_upper_right_neighbor(r)
		if r != None:
			r.set_upper_left_neighbor(l)

	def set_lower_link(l:Trapezoid, r:Trapezoid):
		if l != None:
			l.set_lower_right_neighbor(r)
		if r != None:
			r.set_lower_left_neighbor(l)


import pylab as pl
import matplotlib.pyplot as plt
import matplotlib.collections as mc
# from parse import root, segment, halfedge, rand_segment, vert_segment, bound_box, vertex_x, vertex_y, vertex, point, point_x, point_y

class display:
	def show_map(vertex, segment, bound_box):
		fig, ax = pl.subplots()

		'''bounding box'''
		bound_box_plot = []
		for s in bound_box:
			stt = (s.vsx, s.vsy)
			end = (s.vex, s.vey)
			bound_box_plot.append([stt, end])
		ax.add_collection(mc.LineCollection(bound_box_plot, colors=('black')))

		'''line segments'''
		segment_plot = []
		for s in segment:
			stt = (s.vsx, s.vsy)
			end = (s.vex, s.vey)
			segment_plot.append([stt, end])
		ax.add_collection(mc.LineCollection(segment_plot, colors=('blue')))

		# segment_vertical_plot = []
		# '''vertical lines'''
		# for s in vert_segment:
		# 	stt = (s.vsx, s.vsy)
		# 	end = (s.vex, s.vey)
		# 	segment_vertical_plot.append([stt, end])
		# ax.add_collection(mc.LineCollection(segment_vertical_plot, linestyles='dashed', colors=('black')))

		ax.set_xlim(0, 10)
		ax.autoscale()
		ax.margins(0.1)

		vertex_x = []
		vertex_y = []
		for v in vertex:
			vertex_x.append(float(v.x))
			vertex_y.append(float(v.y))
			plt.text(v.x-0.015, v.y+0.25, "v"+str(v.idx))
		plt.scatter(vertex_x, vertex_y, color="red", s=50)

		# for p in point:
		# 	plt.text(p.x-0.15, p.y-0.5, "p"+str(p.idx))
		# plt.scatter(point_x, point_y, color="green", s=20)

		# plt.savefig('trapzodialMap.png', dpi=1000)
		plt.show()
