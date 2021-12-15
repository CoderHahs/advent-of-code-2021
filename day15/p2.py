from operator import ne
from numpy.lib.nanfunctions import nanargmax
import tools as t

data = t.read_file("day15/input.txt")
for i in range(len(data)):
  data[i] = data[i][:-1]

g = t.nx.DiGraph()

mat = t.np.genfromtxt('day15/input.txt', delimiter=1)

new_mat = t.np.vstack([t.np.hstack([
            (mat + i + j) - 9 * ((mat + i + j) > 9)
            for i in range(5)
            ])
            for j in range(5)
            ])

print(len(mat))
print(len(new_mat))

mat = new_mat

edges = []
for x in range(len(mat)):
  for y in range(len(mat[0])):
    # print(x,y)
    box = t.np.s_[max(0, x - 1):x + 2, max(0, y - 1):y + 2]
    # print(box[0], box[1])
    # print(mat[box])
    # print(mat[x][y])
    stop1 = box[0].stop
    stop2 = box[1].stop
    # print(box[0], box[1])
    if box[0].stop > len(mat):
      stop1 = x+1
    if box[1].stop > len(mat[0]):
      stop2 = y+1
    # print(stop1, stop2)
    for i in range(box[0].start, stop1):
      for j in range(box[1].start, stop2):
        # print(x,y,i,j)
        g.add_node((x,y), value=mat[x][y])
        if (not(x == i and y == j)):
          if (abs(x-i) + abs(y-j) == 1):
            edges.append([(x,y), (i,j), mat[i][j]])

for e in edges:
  g.add_edge(e[0], e[1])
  g.add_edge(e[1], e[0])

# print(edges[-1])

for u, v in g.edges():
  # print(u,v)
  g.edges[u, v]['weight'] = mat[v[0], v[1]]


print(g)
path = t.nx.dijkstra_path(g, (0, 0), (499, 499))

v = 0
# print(path)
# print(g['(0, 0)'].value)
for i in range(1,len(path)):
  v += mat[path[i][0]][path[i][1]]

print(v)