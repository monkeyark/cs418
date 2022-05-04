# Algorithm TRAPEZOIDALMAP(S)
# Input. A set S of n non-crossing line segments.
# Output. The trapezoidal map T(S) and a search structure D for T(S) in a bounding box.
# 1. Determine a bounding box R that containims all segments of S, and initialize the trapezoidal map structure T and search structure D for it.
# 2. Compute a random permutation s1,s2,...,sn of the elements of S.
# 3. for i ← 1 to n
# 4. do Find the set ∆0,∆1,...,∆k of trapezoids in T properly intersected by si.
# 5. Remove ∆0,∆1,...,∆k from T and replace them by the new trapezoids that appear because of the insertion of si.
# 6. Remove the leaves for ∆0,∆1,...,∆k from D, and create leaves for the new trapezoids. Link the new leaves to the existing inner nodes by adding some new inner nodes, as explained below.


from copy import copy, deepcopy

from DoublyConnectedEdgeList import Vertex, Face, HalfEdge, Trapezoid
import networkx as nx

class Node:
	pass
class Graph:
	pass

class Node:
	def __init__(self, parent=None, left=None, right=None, data=None):
		self.parent = parent
		self.left = left
		self.right = right
		self.data = data
		self.path = list()
	
	def set_parent(self, parent:Node):
		self.parent = parent
		self.path.append(parent)
	
	def set_children(self, l:Node, r:Node):
		self.left = l
		self.right = r
		l.set_parent(self)
		r.set_parent(self)

	def set_left_child(self, l:Node):
		self.left = l
		l.set_parent(self)

	def set_right_child(self, r:Node):
		self.right = r
		r.set_parent(self)

	def add_to_path(self, node:Node):
		self.path.append(node)

	def set_data(self, data):
		self.data = data

	def __eq__(self, other):
		return isinstance(other, Node) and self.data == other.data

	def __hash__(self):
		return hash(('parent', self.parent, 'left', self.left, 'right', self.right, 'data', self.data))

	def __str__(self):
		# if isinstance(self.data, Trapezoid):
		# 	return 'node: ' + str(type(self.data)) + '\n' + str(self.data)
		# else:
		# 	return 'node: ' + str(type(self.data)) + '\n' + str(self.data)
		return 'node: ' + str(type(self.data)) + '\n' + str(self.data)
			# return 'node:\n' + str(self.data) + '\n' + 'lchild ' + str(self.left) + ' rchild ' + str(self.right) + '\n'

		# return 'node:\n' + str(self.data) + '\n' + 'lchild ' + str(self.left) + ' rchild ' + str(self.right) + '\n'


# class Graph(nx.DiGraph):
# 	def __init__(self):
# 		super.__init__(self)

# 	def find_point(graph:nx.DiGraph, pt:Vertex):
# 		#TODO find the trapezoid in the current graph
# 		n = [n for n,d in graph.in_degree() if d==0]
# 		node = n[0]
# 		while isinstance(node, Trapezoid) == False:
# 			if isinstance(node, Vertex):
# 				if pt.is_letf_of(node):
# 					#go to left child
# 					node = node.left
# 					pass
# 				elif pt.is_right_of(node):
# 					#go to right child
# 					node = node.right
# 					pass
# 				else:
# 					print(pt, node, ' has same x-value')
# 					#TODO
# 			elif isinstance(node, HalfEdge):
# 				if node.is_below(pt):
# 					node = node.left
# 					pass
# 				elif node.is_above(pt):
# 					node = node.right
# 					pass
# 				else:
# 					print(pt, ' lies on ', node)
# 		# the return should be a Trapezoid type
# 		return node

from collections import OrderedDict
class DAG:
	def __init__(self):
		self.graph = OrderedDict()

	def add_node(self, node_name, graph=None):
		if not graph:
			graph = self.graph
		if node_name in graph:
			raise KeyError('node %s already exists' % node_name)
		graph[node_name] = set()

	def add_node_if_not_exists(self, node_name, graph=None):
		try:
			self.add_node(node_name, graph=graph)
		except KeyError:
			pass

	def remove_node(self, node_name, graph=None):
		if not graph:
			graph = self.graph
		if node_name not in graph:
			raise KeyError('node %s does not exist' % node_name)
		graph.pop(node_name)

		for node, edges in graph.items:
			if node_name in edges:
				edges.remove(node_name)

	def rename_edges(self, old_task_name, new_task_name, graph=None):
		""" Change references to a task in existing edges. """
		if not graph:
			graph = self.graph
		for node, edges in graph.items():

			if node == old_task_name:
				graph[new_task_name] = copy(edges)
				del graph[old_task_name]

			else:
				if old_task_name in edges:
					edges.remove(old_task_name)
					edges.add(new_task_name)