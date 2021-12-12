import tools as t

data = t.read_file("d10_data.txt")
for i in range(len(data)):
  data[i] = data[i][:-1]

complete = []

open = ['(', '{', '[', '<']
close = [')', '}', ']', '>']

for i in range(len(data)):
  stack = []
  flag = False
  for c in data[i]:
    if c in open:
      stack.append(c)
    else:
      last = stack.pop()
      x = -1
      if (c == ')'):
        x = 0
      elif (c == '}'):
        x = 1
      elif (c == ']'):
        x = 2
      elif (c == '>'):
        x = 3
      if x != -1:
        if last != open[x]:
          flag = True
          break
  if flag == False:
    complete.append(i)

# print(complete)

scores = []
scoring = {')': 1, ']': 2, '}': 3, '>': 4}

for i in complete:
  stack = []
  for c in data[i]:
    if c in open:
      stack.append(c)
    else:
      stack.pop()
  s = []
  for c in stack[::-1]:
    x = -1
    if (c == '('):
      x = 0
    elif (c == '{'):
      x = 1
    elif (c == '['):
      x = 2
    elif (c == '<'):
      x = 3
    s.append(close[x])
  sc = 0
  for c in s:
    sc = sc*5 + scoring[c]
  scores.append(sc)

print(sorted(scores)[len(scores)//2])