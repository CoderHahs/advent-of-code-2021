import tools as t

data = t.read_file("d9_data.txt")

for i in range(len(data)):
  data[i] = data[i][:-1]

def lookup(s1,s2,s3, i, r: False, l: False):
  if r == False and l == False:
    if s1 == None:
      return int(s2[i-1]) > int(s2[i]) and int(s2[i+1]) > int(s2[i]) and int(s3[i]) > int(s2[i])
    elif s3 == None:
      return int(s2[i-1]) > int(s2[i]) and int(s2[i+1]) > int(s2[i]) and int(s1[i]) > int(s2[i])
    else:
      return int(s2[i-1]) > int(s2[i]) and int(s2[i+1]) > int(s2[i]) and int(s1[i]) > int(s2[i]) and int(s3[i]) > int(s2[i])
  elif r==True:
    if s1 == None:
      return int(s2[i-1]) > int(s2[i]) and int(s3[i]) > int(s2[i])
    elif s3 == None:
      return int(s2[i-1]) > int(s2[i]) and int(s1[i]) > int(s2[i])
    else:
      return int(s2[i-1]) > int(s2[i]) and int(s1[i]) > int(s2[i]) and int(s3[i]) > int(s2[i])
  elif l==True:
    if s1 == None:
      return int(s2[i+1]) > int(s2[i]) and int(s3[i]) > int(s2[i])
    elif s3 == None:
      return int(s2[i+1]) > int(s2[i]) and int(s1[i]) > int(s2[i])
    else:
      return int(s2[i+1]) > int(s2[i]) and int(s1[i]) > int(s2[i]) and int(s3[i]) > int(s2[i])

arr = []
for i in range(len(data)):
  if (i == 0):
    top = None
    mid = data[i]
    bot = data[i+1]
  elif (i == len(data)-1):
    top = data[i-1]
    mid = data[i]
    bot = None
  else:
    top = data[i-1]
    mid = data[i]
    bot = data[i+1]

  for i in range(len(mid)):
    # print(mid[i])
    r = False
    l = False
    if (i == 0):
      l = True
    elif (i == len(mid)-1):
      r = True
    if (lookup(top, mid, bot, i, r, l)):
      arr.append(int(mid[i])+1)

print(sum(arr))
