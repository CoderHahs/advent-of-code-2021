import tools as t

data = t.read_file("d6_data.txt")
data = data[0].split(',')

d = t.defaultdict(lambda: 0)

for i in range (len(data)):
  data[i] = int(data[i])
  d[data[i]] += 1

for n in range(1,257):
  temp_d = t.defaultdict(lambda:0)
  for key,value in sorted(d.items(), reverse=True):
    if key != 0:
      temp_d[key-1] = d[key]
    else:
      temp_d[6] += d[0]  
      temp_d[8] = d[0]
  d = temp_d
  # print(d)

sum = 0
for key in d.keys():
  sum += d[key]
print(sum)