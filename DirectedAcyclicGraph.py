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
from copy import copy, deepcopy
from collections import OrderedDict

class Node:
	def __init__(self):
		pass

class DirectedAcyclicGraph:
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

	def delete_node(self, node_name, graph=None):
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