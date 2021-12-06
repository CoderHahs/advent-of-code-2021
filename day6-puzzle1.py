import tools as t

data = t.read_file("d6_data.txt")
data = data[0].split(',')

for i in range (len(data)):
  data[i] = int(data[i])

print(data)

for n in range(1,257):
  print(n)
  for i in range(len(data)):
    if (data[i] == 0):
      data.append(8)
      data[i] = 6
    else:
      data[i] -= 1
  # print(data)

print(len(data))