from sys import setrecursionlimit
setrecursionlimit(int(1e9))

import tools as t
from graph import Graph
import networkx as nx

data = t.read_file("day12/d12_data.txt")
for i in range(len(data)):
  data[i] = data[i][:-1].split('-')

def dfs(u, b):
	global res
	if u == 'end':
		res += 1
		return
	
	visited[u] += 1

	for v in g[u].keys():
		if v.isupper():
			dfs(v, b)
		elif visited[v] == 0:
			dfs(v, b)
		elif visited[v] == 1 and not b:
			dfs(v, True)
	
	visited[u] -= 1

g = nx.Graph()
g.add_edges_from(data)
visited = {i: 0 for i in g.nodes}
visited['start'] = 2
res = 0
dfs('start', False)

print(res)