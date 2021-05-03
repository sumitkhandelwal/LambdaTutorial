import math
import numpy as np
f = open('input.txt', 'r')
data = f.readlines()
f.close()
data = list(map(lambda s: s.strip(), data))
n = len(data) - 1
m = n
a = []
for i in range(1, len(data)):
    new_list = data[i].split(':')
    a.append(new_list)
new_a = []
for i in range(0, len(a)):
  for j in range(0, len(a[0])):
      new_a.append(int(a[j][i]))
array_2d = np.array(new_a).reshape(n,m)
output = data[0].split(':')
output_array = []
for i in output:
    output_array.append(int(i))
a = np.array(array_2d)
b = np.array(output_array)
x = np.linalg.solve(a, b)

for i in range(1, 10):
    if(len(b)== 2):
        c =((b[0] * i), (b[1] * i))
    if (len(b) == 3):
        c = ((b[0] * i), (b[1] * i), (b[2] * i))
    if (len(b) == 4):
        c = ((b[0] * i), (b[1] * i), (b[2] * i), (b[3] * i))
    if (len(b) == 5):
        c = ((b[0] * i), (b[1] * i), (b[2] * i), (b[3] * i), (b[4] * i))
    if (len(b) == 6):
        c = ((b[0] * i), (b[1] * i), (b[2] * i), (b[3] * i), (b[4] * i), (b[5] * i))
    x = np.linalg.solve(a, c)
    count = 0
    inte, deci = divmod(x[count], 1)
    deci = "{:f}".format(float(deci))
    if(float(deci) <= 0):
        f = open('output.txt', 'w')
        for i in range(len(x)):
            f.write(str(int(x[i]))+'\n')
        f.close()
        break


