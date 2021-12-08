import tools as t

data = t.read_file("d8_data.txt")

i = []
o = []

for row in data:
  # print(row)
  a,b = row.split(" | ")
  i.append(a)
  o.append(b[:-1])

count_1 = 0
count_4 = 0
count_7 = 0
count_8 = 0

for row in o:
  for comb in row.split(" "):
    if len(comb) == 2:
      count_1 += 1
    elif len(comb) == 3:
      count_7 += 1
    elif len(comb) == 4:
      count_4 += 1
    elif len(comb) == 7:
      count_8 += 1

print(count_1 + count_4 + count_8 + count_7)
     