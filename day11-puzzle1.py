import tools as t

data = t.read_file("d11_data.txt")
for i in range(len(data)):
  data[i] = data[i][:-1]

new_data = []
for i in range(len(data)):
  temp = []
  for j in range(len(data[i])):
    temp.append(int(data[i][j]))
  new_data.append(temp)

data=new_data
# print(data)

def update(i, j, data, flashed):
  # print(data[i][j], i, j)
  # print(data)
  # print(flashed)
  if (i,j) in flashed:
    return
  if data[i][j] > 8:
    # print('yay')
    data[i][j] = 0
    flashed.add((i,j))
    if i == 0:
      if j == 0:
        data[i][j+1] += 1
        if data[i][j+1] > 9: # right
          update(i, j+1, data, flashed)
        data[i+1][j] += 1
        if data[i+1][j] > 9: # down
          update(i+1, j, data, flashed)
        data[i+1][j+1] += 1
        if data[i+1][j+1] > 9: # right down
          update(i+1, j+1, data, flashed)
      elif j == len(data[i])-1:
        data[i][j-1] += 1
        if data[i][j-1] > 9: # left
          update(i, j-1, data, flashed)
        data[i+1][j] += 1
        if data[i+1][j] > 9: # down
          update(i+1, j, data, flashed)
        data[i-1][j-1] += 1
        if data[i-1][j-1] > 9: # left down
          update(i-1, j-1, data, flashed)
      else:
        data[i][j-1] += 1
        if data[i][j-1] > 9: # left
          update(i, j-1, data, flashed)
        data[i+1][j] += 1
        if data[i+1][j] > 9: # down
          update(i+1, j, data, flashed)
        data[i+1][j-1] += 1
        if data[i+1][j-1] > 9: # down left
          update(i+1, j-1, data, flashed)
        data[i][j+1] += 1
        if data[i][j+1] > 9: # right
          update(i, j+1, data, flashed)
        data[i+1][j+1] += 1
        if data[i+1][j+1] > 9: # down right
          update(i+1, j+1, data, flashed)
    elif i == len(data)-1:
      if j == 0:
        data[i][j+1] += 1
        if data[i][j+1] > 9: # right
          update(i, j+1, data, flashed)
        data[i-1][j] += 1
        if data[i-1][j] > 9: # up
          update(i-1, j, data, flashed)
        data[i-1][j+1] += 1
        if data[i-1][j+1] > 9: # up right
          update(i-1, j+1, data, flashed)
      elif j == len(data[i])-1:
        data[i][j-1] += 1
        if data[i][j-1] > 9: # left
          update(i, j-1, data, flashed)
        data[i-1][j] += 1
        if data[i-1][j] > 9: # up
          update(i-1, j, data, flashed)
        data[i-1][j-1] += 1
        if data[i-1][j-1] > 9: # up left
          update(i-1, j-1, data, flashed)
      else:
        data[i][j-1] += 1
        if data[i][j-1] > 9: # left
          update(i, j-1, data, flashed)
        data[i-1][j] += 1
        if data[i-1][j] > 9: # up
          update(i-1, j, data, flashed)
        data[i-1][j-1] += 1
        if data[i-1][j-1] > 9: # up left
          update(i-1, j-1, data, flashed)
        data[i][j+1] += 1 # right
        if data[i][j+1] > 9:
          update(i, j+1, data, flashed)
        data[i-1][j+1] += 1
        if data[i-1][j+1] > 9: # up right
          update(i-1, j+1, data, flashed)
    else:
      if j == 0:
        data[i][j+1] += 1
        if data[i][j+1] > 9: # right
          update(i, j+1, data, flashed)
        data[i-1][j] += 1
        if data[i-1][j] > 9: # up
          update(i-1, j, data, flashed)
        data[i+1][j] += 1
        if data[i+1][j] > 9: # don
          update(i+1, j, data, flashed)
        data[i-1][j+1] += 1
        if data[i-1][j+1] > 9: # up right
          update(i-1, j+1, data, flashed)
        data[i+1][j+1] += 1
        if data[i+1][j+1] > 9: # down right
          update(i+1, j+1, data, flashed)
      elif j == len(data[i])-1:
        data[i][j-1] += 1
        if data[i][j-1] > 9: # left
          update(i, j-1, data, flashed)
        data[i-1][j] += 1
        if data[i-1][j] > 9: # up 
          update(i-1, j, data, flashed)
        data[i+1][j] += 1
        if data[i+1][j] > 9: # down
          update(i+1, j, data, flashed)
        data[i-1][j-1] += 1
        if data[i-1][j-1] > 9: # up right
          update(i-1, j-1, data, flashed)
        data[i+1][j-1] += 1
        if data[i+1][j-1] > 9: # down right
          update(i+1, j-1, data, flashed)
      else:
        data[i][j-1] += 1
        if data[i][j-1] > 9: # left
          update(i, j-1, data, flashed)
        data[i][j+1] += 1
        if data[i][j+1] > 9: # right
          update(i, j+1, data, flashed)
        data[i-1][j] += 1
        if data[i-1][j] > 9: # up
          update(i-1, j, data, flashed)
        data[i+1][j] += 1
        if data[i+1][j] > 9: # down
          update(i+1, j, data, flashed)
        data[i-1][j-1] += 1
        if data[i-1][j-1] > 9: # left up
          update(i-1, j-1, data, flashed)
        data[i-1][j+1] += 1
        if data[i-1][j+1] > 9: # right up
          update(i-1, j+1, data, flashed)
        data[i+1][j-1] += 1
        if data[i+1][j-1] > 9: # down left
          update(i+1, j-1, data, flashed)
        data[i+1][j+1] += 1
        if data[i+1][j+1] > 9: # down right
          update(i+1, j+1, data, flashed)
  else:
    data[i][j] += 1    


flashes = 0
step = 100
for x in range(step):
  flashed = set()
  for i in range(len(data)):
    for j in range(len(data[i])):
      # print(data[i][j], i, j)
      update(i,j, data, flashed)
  flashes += len(flashed)
  for f in flashed:
    data[f[0]][f[1]] = 0

print(flashes)
print(data)