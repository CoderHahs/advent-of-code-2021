import tools as t

data = t.read_file("d7_data.txt")
data = data[0].split(',')

d = t.defaultdict()
  

for i in data:
  i = int(i)
  t_fuel = 0 
  for j in data:
    j = int(j)
    if (abs(i-j) > 0):
      t_fuel += abs(i-j)
  d[i] = t_fuel

min = 100
min_value = 1000000000000000000000000
for key, value in d.items():
  if value < min_value:
    min = key
    min_value = value

print(min_value)