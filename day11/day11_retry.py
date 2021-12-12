import tools as t

data = t.read_file("d11_data.txt")
# for i in range(len(data)):
#   data[i] = list(map(int, data[i].strip()))

mat = t.np.genfromtxt('d11_data.txt', delimiter=1)
print(mat)
total = 0
step = 0
while t.np.any(mat):
  step += 1
  mat += 1
  flashing = t.np.argwhere(mat > 9)
  while len(flashing):
    for x, y in flashing:
      box = t.np.s_[max(0, x - 1):x + 2, max(0, y - 1):y + 2]
      mat[box] += mat[box] > 0
      mat[x,y] = 0

    flashing = t.np.argwhere(mat > 9)

  total += t.np.count_nonzero(mat == 0)

  if step == 100:
      print(f'Part 1: {total}')

print(f'Part 2: {step}')