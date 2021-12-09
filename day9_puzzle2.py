import tools as t
from scipy import ndimage

data = t.read_file("d9_data.txt")

for i in range(len(data)):
  data[i] = data[i][:-1]


for i in range(len(data)):
  data[i] = list(data[i])
  for j in range(len(data[i])):
    # print(data[i][j])
    if (data[i][j] == '9'):
      data[i][j] = 0
    else:
      data[i][j] = 1

# def lookup(s1,s2,s3, i, r: False, l: False):
#   if r == False and l == False:
#     if s1 == None:
#       a = [s2[i-1], s2[i+1], s3[i]]
#       if (a.count(0) == 2):
#         return 1
#       return  s2[i-1]  + s2[i+1] + s3[i]
#     elif s3 == None:
#       a = [s2[i-1],s2[i+1],s1[i]]
#       if (a.count(0) == 2):
#         return 1
#       return s2[i-1]  + s2[i+1] + s1[i]
#     else:
#       a = [s2[i-1],s2[i+1],s3[i]]
#       if (a.count(0) == 2):
#         return 1
#       return s2[i-1]  + s2[i+1] + s3[i] 
#   elif r==True:
#     if s1 == None:
#       if (s2[i-1] == 0 or s3[i] == 0):
#         return 1
#       return  s2[i-1]  + s3[i]
#     elif s3 == None:
#       if (s2[i-1] == 0 or s1[i] == 0):
#         return 1
#       return s2[i-1]  + s1[i]
#     else:
#       a = [s2[i-1], s1[i], s3[i]]
#       if (a.count(0) == 2):
#         return 1
#       return  s2[i-1]  + s1[i] + s3[i]
#   elif l==True:
#     if s1 == None:
#       if (s2[i+1] == 0 or s3[i] == 0):
#         return 1
#       return s2[i+1] + s3[i]
#     elif s3 == None:
#       if (s2[i+1] == 0 or s1[i] == 0):
#         return 1
#       return s2[i+1] + s1[i]
#     else:
#       a = [s3[i],s2[i+1],s1[i]]
#       if (a.count(0) == 2):
#         return 1
#       return s3[i]  + s2[i+1] + s1[i]

# # data = []
# # for i in range(len(data)):
# #   arr = []
# #   for j in range(len(data[i])):
# #     arr.append(0)
# #   new_data.append(arr)

# for i in range (len(data)):
#   if (i == 0):
#     top = None
#     mid = data[i]
#     bot = data[i+1]
#   elif (i == len(data)-1):
#     top = data[i-1]
#     mid = data[i]
#     bot = None
#   else:
#     top = data[i-1]
#     mid = data[i]
#     bot = data[i+1]
#   for j in range(len(data[i])):
#     # print(mid[i])
#     r = False
#     l = False
#     if (j == 0):
#       l = True
#     elif (j == len(mid)-1):
#       r = True
#     if (data[i][j] != 0):
#       data[i][j] = lookup(top, mid, bot, j, r, l)

# print (data)
data = t.np.array(data)
# print(data)

label, num_label = ndimage.label(data == 1)
size = t.np.bincount(label.ravel())
# print(size)
three = sorted(size[1:], reverse=True)[:3]
print(t.np.prod(three))
 