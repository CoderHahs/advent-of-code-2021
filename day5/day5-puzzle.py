import tools as t

data = t.read_file("d5_data.txt")

# h_v = []

# for row in data:
#   c = row.split(" -> ")
#   x1, y1 = c[0].split(',')
#   x2, y2 = c[1].split(',')
#   if (int(x1) == int(x2)):
#     h_v.append([int(x1),int(y1),int(y2), 'x'])
#   elif (int(y1)==int(y2)):
#     h_v.append([int(x1), int(x2), int(y2), 'y'])

# print(h_v)

# points = {}

# for line in h_v:
#   if line[3] == 'x':
#     if (line[1] < line[2]):
#       for i in range(line[1], line[2]+1):
#         key = str(line[0])+str(i)
#         if key in points:
#           points[key] += 1
#         else:
#           points[key] = 1
#     else:
#       for i in range(line[1], line[2]-1, -1):
#         key = str(line[0])+str(i)
#         if key in points:
#           points[key] += 1
#         else:
#           points[key] = 1
#   elif line[3] == 'y':
#     if (line[0] < line[1]):
#       for i in range(line[0], line[1]+1):
#         key = str(i)+str(line[2])
#         if key in points:
#           points[key] += 1
#         else:
#           points[key] = 1
#     else:
#       for i in range(line[0], line[1]-1, -1):
#         key = str(i)+str(line[2])
#         if key in points:
#           points[key] += 1
#         else:
#           points[key] = 1

# print(points)

# count = 0
# for key in points.keys():
#   if points[key] > 1:
#     print(key)
#     count+=1

# print(count)


def myrange(x1, y1, x2, y2):
    while True:
        yield(x1, y1)
        if x1 == x2 and y1 == y2:
            return
        if x1 != x2:
            x1 += (1 if x1 <= x2 else -1)
        if y1 != y2:
            y1 += (1 if y1 <= y2 else -1)

# def point_range(x1,y1,x2,y2):
#     co = []
#     while True:
#         if x1 == x2 and y1 == y2:
#             return co
#         if x1!=x2:
#             x1 += (1 if x1 <= x2 else -1)
#         if y1!=y2:
#             y1 += (1 if y1 <= y2 else -1)
#         co.append((x1,y1))

    

points = t.defaultdict(lambda: 0)

for line in data:
    p1, p2 = line.split(" -> ")

    x1, y1 = p1.split(",")
    x2, y2 = p2.split(",")

    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    # if x1 == x2 or y1 == y2:
    for xr, yr in myrange(x1, y1, x2, y2):
        points[(xr, yr)] += 1
        # temp1.append((xr,yr))

count = 0

for point, ol in points.items():
    if ol > 1:
        count += 1

print(count)