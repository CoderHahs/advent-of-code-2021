import tools as t

data = t.read_file("d7_data.txt")
data = data[0].split(',')

d = t.defaultdict()

for i in range(0, len(data)):
    data[i] = int(data[i])

for i in range(min(data), max(data)+1):
  t_fuel = 0 
  for j in data:
    if (abs(i-j) > 0):
      y = abs(i-j)
      t_fuel += y*(y+1) / 2
  d[i] = t_fuel

min = 100
min_value = 1000000000000000000000000
for key, value in d.items():
  if value < min_value:
    min = key
    min_value = value

print(min_value)