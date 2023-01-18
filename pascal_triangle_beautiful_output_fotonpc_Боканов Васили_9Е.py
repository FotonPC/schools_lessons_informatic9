n = int(input())
if n%2==0:
    print("n должно быть четным")
    exit()

def format(x, le):
    if (le-len(str(x))) % 2==0:
        return ((le-len(str(x)))//2) *' ' + str(x) + ((le-len(str(x)))//2) *' '
    else:
        return ((le-len(str(x)))//2) *' ' + str(x) + ((le-len(str(x)))//2+1) *' '

def calc_new(m, sp):
    res = [0 for i in range(m+1)]
    for i in range(1, m):
        res[i-1] = sp[i] + sp[i - 1]
    #print(res)
    return res

c = [0 for i in range(n)]
c[-1] = 1
#print(c)
l = calc_new(n, c)

f = 5
f2 = 2

for j in l:
    if j != 0:
        print(' '*(n-2+f2//2)*f2 + format(j, f), end=' ')
print()
for i in range(1, n-1):
    l = calc_new(n, l)
    print(' '*((n-1-i)*f2), end='')
    for j in l:
        if j != 0:
            print(format(j, f), end='')
    print()
