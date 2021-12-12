import tools as t

data = t.read_file("d10_data.txt")
for i in range(len(data)):
  data[i] = data[i][:-1]

print(data)

incorrect = {')': 0, '}': 0, ']': 0, '>': 0}
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
          incorrect[c] += 1
          break
  if flag == False:
    complete.append(i)



ans = incorrect[')']*3 + incorrect[']']*57 + incorrect['}']*1197 + incorrect['>']*25137

print(ans)