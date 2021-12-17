import tools as t

data = t.read_file("day17/input.txt")
for i in range(len(data)):
  data[i] = data[i][:-1]

print(data)
values = data[0].split('=')[-1]
y = int(values.split('..')[0])
n = abs(y)-1
print(int((n+(n**2))/2))