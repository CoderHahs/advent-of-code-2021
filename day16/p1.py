import tools as t

data = t.read_file("day16/input.txt")
for i in range(len(data)):
  data[i] = data[i][:-1]

print(data[0])

scale = 16 ## equals to hexadecimal

num_of_bits = 8

# bits = bin(int(data[0], scale))[2:].zfill(num_of_bits)
bits = "".join(bin(c)[2:].zfill(8) for c in bytes.fromhex(data[0]))
print(bits)

class Packet:
  def __init__(self, version, tid, n, subpackets):
    self.version = version
    self.tid = tid
    self.n = n
    self.subpackets = subpackets

  def sum_versions(self):
    return self.version + sum(v.sum_versions() for v in self.subpackets)

  def eval(self):
    if self.tid == 4:
        return self.n
    elif self.tid == 0:
        return sum(v.eval() for v in self.subpackets)
    elif self.tid == 1:
        return t.math.prod(v.eval() for v in self.subpackets)
    elif self.tid == 2:
        return min(v.eval() for v in self.subpackets)
    elif self.tid == 3:
        return max(v.eval() for v in self.subpackets)
    elif self.tid == 5:
        return self.subpackets[0].eval() > self.subpackets[1].eval()
    elif self.tid == 6:
        return self.subpackets[0].eval() < self.subpackets[1].eval()
    elif self.tid == 7:
        return self.subpackets[0].eval() == self.subpackets[1].eval()


def parse_one():
  global bits

  version, bits = int(bits[:3], 2), bits[3:]
  tid, bits = int(bits[:3], 2), bits[3:]
  n = None
  subpackets = []

  if tid == 4:
    n = ""
    while bits[0] == "1":
      n, bits = n + bits[1:5], bits[5:]
    n, bits = n + bits[1:5], bits[5:]

    n = int(n, 2)
  else:
    lid, bits = bits[0], bits[1:]
    if lid == "0":
      length, bits = int(bits[:15], 2), bits[15:]

      fmt_len = len(bits)
      while (fmt_len - len(bits)) < length:
        subpackets.append(parse_one())
    else:
      number, bits = int(bits[:11], 2), bits[11:]

      for n in range(number):
        subpackets.append(parse_one())

  return Packet(version=version, tid=tid, n=n, subpackets=subpackets)

x = parse_one()

print(x)

print(x.sum_versions())
print(x.eval())