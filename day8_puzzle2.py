import tools as t

import string

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

dx = []
for x in range(len(i)):
  d = t.defaultdict(lambda: None)
  while len(d.keys()) != 10:
    # print(len(d.keys()))
    # print(d)
    if len(d.keys()) <= 3:
      for comb in i[x].split(" "):
        if len(comb) == 2:
          d[1] = set(comb)
        elif len(comb) == 3:
          d[7] = set(comb)
        elif len(comb) == 4:
          d[4] = set(comb)
        elif len(comb) == 7:
          d[8] = set(comb)
    # print(i[x])
    for comb in i[x].split(" "):
      # print(comb)
      if comb == d[1] or comb == d[7] or comb == d[4] or comb == d[8]:
        continue
      else:
        s = set(comb)
        if len(comb) == 5:
          if d[7] <= s:
            d[3] = s
          if d[6] != None:
            # print('yat', s <= (d[6]), s, d[6])
            if s <= d[6]:
              # print('yat', )
              d[5] = s
        if len(comb) == 6:
          if (d[7] <= s) == False:
            d[6] = s
    d[9] = d[7] | d[3] | d[4]
    d[0] = d[8] - d[3] | d[7] | (d[9] - d[4] - d[7])
    d[2] = d[8] - d[0] | d[7] - d[6] | d[7] - d[4] | d[6] - d[9] | d[3] - d[4]
  dx.append(d)



def find(s, time):
  for key, value in time.items():
    # print(s, key, value)
    if s == value:
      return key

arr = []
for x in range(len(o)):
  st = ""
  for comb in o[x].split(" "):
    # print(comb)
    # print(d)
    n = find(set(comb), dx[x])
    st += (str(n))
  arr.append(int(st))

print(sum(arr))
  