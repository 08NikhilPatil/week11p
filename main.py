M=[[1,2,3],[3,4,5],[5,6,7]]
sums=[]
'''sums=[sum(row) for row in M]
print(sums)
m, n = len(M), len(M[0])
rsums = []
for i in range(m):
    val = 0
    for j in range(n):
        val += M[i][j]
    rsums.append(val)
print(rsums)
for r in M:
  sums.append(sum(r))

print(sums)
triplets = [(x, y, z) for x in range(1, 100) 
                      for y in range(x + 1, 100)
                      for z in range(y + 1, 100)
                      if x ** 2 + y ** 2 == z ** 2]
print(triplets)

triplets = [(x, y, z) for x in range(1, 100) 
                      for y in range(1, 100)
                      for z in range(1, 100)
                      if x ** 2 + y ** 2 == z ** 2 and x < y < z]
print(triplets)
'''
R=[]
L=[1,2,3]
A=[3,4,5]
'''for x,y in zip(L,M):
  R.append(x+y)
print(type(R))
V=[L[i]+M[i] for i in range(len(M))]
print(V)
M_t = [ ]

n = len(M)
for i in range(n):
    M_t.append([ ])
    for j in range(n):
        M_t[-1].append(M[j][i])
print(M_t)'''


for x in range(n):
  if x%n==0:
    print(x)
