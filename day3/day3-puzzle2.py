import tools as t




rows = t.read_file("d3_data.txt");
# print(len(rows))

def calculate_ratios(rows):
    d = {"0": [0,0],
      "1": [0,0],
      "2": [0,0],
      "3": [0,0],
      "4": [0,0],
      "5": [0,0],
      "6": [0,0],
      "7": [0,0],
      "8": [0,0],
      "9": [0,0],
      "10": [0,0],
      "11": [0,0],}

    for row in rows:
        if (row[0]) == "0":
            d["0"][0] += 1
        else:
            d["0"][1] += 1
        
        if (row[1]) == "0":
            d["1"][0] += 1
        else:
            d["1"][1] += 1
        
        if (row[2]) == "0":
            d["2"][0] += 1
        else:
            d["2"][1] += 1
            
        if (row[3]) == "0":
            d["3"][0] += 1
        else:
            d["3"][1] += 1
            
        if (row[4]) == "0":
            d["4"][0] += 1
        else:
            d["4"][1] += 1
            
        if (row[5]) == "0":
            d["5"][0] += 1
        else:
            d["5"][1] += 1
            
        if (row[6]) == "0":
            d["6"][0] += 1
        else:
            d["6"][1] += 1
            
        if (row[7]) == "0":
            d["7"][0] += 1
        else:
            d["7"][1] += 1
            
        if (row[8]) == "0":
            d["8"][0] += 1
        else:
            d["8"][1] += 1
            
        if (row[9]) == "0":
            d["9"][0] += 1
        else:
            d["9"][1] += 1
            
        if (row[10]) == "0":
            d["10"][0] += 1
        else:
            d["10"][1] += 1
            
        if (row[11]) == "0":
            d["11"][0] += 1
        else:
            d["11"][1] += 1
        
    return d
        
ox = ""
co = ""

keep_ox = rows
keep_co = rows

for n in range(11):
    n = str(n)
    d = calculate_ratios(keep_ox)
    if d[n][1] >= len(keep_ox)/2:
        i = "1"
    else:
        i = "0"
    temp = []
    for row in keep_ox:
        if row[int(n)] == i:
            temp.append(row)
    keep_ox = temp
    if (len(keep_ox) == 1):
        break
    
for n in range(11):
    n = str(n)
    d = calculate_ratios(keep_co)
    if d[n][0] <= len(keep_co)/2:
        i = "0"
    else:
        i = "1"
    temp = []
    for row in keep_co:
        if row[int(n)] == i:
            temp.append(row)
    keep_co = temp
    if (len(keep_co) == 1):
        break

print(int(keep_ox[0], 2))
print(int(keep_co[0], 2))
        
print(int(keep_ox[0], 2)*int(keep_co[0], 2))
