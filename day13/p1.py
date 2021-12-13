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

for f in fold[:1]:
  for x, y in co:
    if f[0] == 'y' and y > f[1]:
      dots.add((x, 2*f[1] - y))
    elif f[0] == 'x' and x > f[1]:
      dots.add((2*f[1]-x, y))
    else:
      dots.add((x,y))

print(dots)
print(len(dots))