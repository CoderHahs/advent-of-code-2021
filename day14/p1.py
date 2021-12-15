import tools as t

data = t.read_file("day14/test_input.txt")
for i in range(len(data)):
  data[i] = data[i][:-1]



rules = t.defaultdict()

for i in range(1, len(data)):
  r = data[i].split(" -> ")
  rules[(r[0][0], r[0][1])] = r[1]

step = 3
polymer = data[0]
for i in range(step):
  print(i)
  comb = list(polymer)
  pairs = []
  for j in range(len(comb)-1):
    pairs.append((comb[j], comb[j+1]))
  new_polymer = ""
  for p in range(len(pairs)):
    r = pairs[p]
    v = rules[r]
    # print(r, v, r[0] + v)
    if p != len(pairs)-1:
      new_polymer += r[0] + v
    else:
      new_polymer += r[0] + v + r[1]
  polymer = new_polymer
  print(polymer)

all_freq = {} 
for i in polymer:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# print(polymer)
print(all_freq)
mx = max(all_freq, key=all_freq.get)
mn = min(all_freq, key=all_freq.get)

print(mx, all_freq[mx], mn, all_freq[mn])
print(max(all_freq.values())-min(all_freq.values()))