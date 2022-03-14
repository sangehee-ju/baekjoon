b = input()
ap = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
      'u', 'v', 'w', 'x', 'y', 'z']
res = [0]*len(ap)

for i in range(len(ap)):
    res[i] = b.find(ap[i])

for i in res:
    print(i, end=' ')
