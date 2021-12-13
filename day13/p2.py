import tools as t

data = t.read_file("day13/input.txt")
for i in range(len(data)):
  data[i] = data[i][:-1]

# print(data)

# x_max, y_max = 0,0
dots = set()
co = []
fold = []
for row in data:
  if ',' in row:
    co.append(list(map(int, row.split(','))))
  else:
    fold.append([row.split('=')[0][-1:],int(row.split('=')[1])])

for f in fold:
  for x, y in co:
    if f[0] == 'y' and y > f[1]:
      dots.add((x, 2*f[1] - y))
    elif f[0] == 'x' and x > f[1]:
      dots.add((2*f[1]-x, y))
    else:
      dots.add((x,y))

# print(dots)
# print(len(dots))

def render(dots):
    w = max( k[0] for k in dots )+1
    h = max( k[1] for k in dots )+1
    layout = [ [' ' for _ in range(w)] for _ in range(h)]
    for pt in dots:
        layout[pt[1]][pt[0]] = '#'
    return '\n'.join( ''.join(k) for k in layout )

print(dots)


# grid = []
# for i in range(y_max+1):
#   row = []
#   for j in range(x_max+1):
#     row.append('.')
#   grid.append(row)

# for row in data[:-12]:
#   co = list(map(int, row.split(',')))
#   grid[co[1]][co[0]] = '#'

# grid1 = []
# grid2 = []
# for row in data[-2:-1]:
#   line = int(row.split('fold along y=')[1])
#   grid1 = grid[:line]
#   grid2 = grid[line+1:][::-1]
# # print(grid1)
# # print(grid2)

# second_part = grid1[len(grid1)-len(grid2):]
# first_part = grid1[:len(grid1)-len(grid2)]
# print(len(grid2), len(second_part), len(first_part), len(grid1))
# print(grid2)
# for i in range(len(grid2)):
#   for j in range(len(grid2[i])):
#     if grid2[i][j] == '#':
#       second_part[i][j] = '#'

# new_grid = first_part + second_part
# print(new_grid)

# count = 0
# for i in range(len(new_grid)):
#   for j in range(len(new_grid[i])):
#     if new_grid[i][j] == '#':
#       count+=1

# print(count)