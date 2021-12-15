import tools as t

data = t.read_file("day14/input.txt")
for i in range(len(data)):
  data[i] = data[i][:-1]

rules = t.defaultdict()

for i in range(1, len(data)):
  r = data[i].split(" -> ")
  rules[(r[0][0], r[0][1])] = r[1]

step = 41
polymer = data[0]
count = t.defaultdict(lambda:0)
comb = list(polymer)
pairs = []
for j in range(len(comb)-1):
  p = (comb[j], comb[j+1])
  pairs.append((comb[j], comb[j+1]))
  count[p] += 1

for i in range(step-1):
  new_count = t.defaultdict(lambda:0)
  for key in list(count.keys()):
    v = rules[key]
    o = count[key]
    comb1 = (key[0], v)
    comb2 = (v, key[1])
    new_count[comb1] += o
    new_count[comb2] += o
  count = new_count.copy()

def get_letter_count(template: str, result_dict):
    letter_count = t.defaultdict(int)
    for k, v in result_dict.items():
        letter_count[k[0]] += v
        letter_count[k[1]] += v
    letter_count[template[0]] += 1
    letter_count[template[-1]] += 1
    letter_count.update((k, v // 2) for k, v in letter_count.items())
    return sorted(letter_count.values())

arr = get_letter_count(polymer, count)
print(arr[-1] - arr[0])