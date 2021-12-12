
from sys import setrecursionlimit
setrecursionlimit(int(1e9))

import tools as t
import networkx as nx


data = t.read_file("day12/d12_data.txt")
for i in range(len(data)):
  data[i] = data[i][:-1].split('-')


def dfs(u):
	global res
	if u == 'end':
		res += 1
	# print(str(u))
	visited[u] = True
	for v in g[u].keys():
		if not visited[v] or v.isupper():
			dfs(v)
	
	visited[u] = False


g = nx.Graph()
g.add_edges_from(data)
visited = {i: False for i in g.nodes}
visited['start'] = True
res = 0
dfs('start')

print(res)