#Solution to Hackerrank doormat problem!!
import sys as s
n, m = map(int, input().split())
k = 3
p = 0
st=m-6
for i in range(n):
    j = 0
    while (j < m and i<int(n/2)):
        
        if (j == ((m - k) / 2) and m != k):
            for pivot in range(int((k + 1) / 3)):
                print(".|.", end="")
                j += 3
            k = k + 6
        print("-", end="")
        j += 1
      
    if (i == (int(n / 2))):
        j = 0
        while (j < m):
            if (j == ((m-7)/2)):
                print("WELCOME", end="")
                j += 7
            else:
                print("-", end="")
                j += 1
    j = 0
    
    while (j < m and i>int(n/2)):
        if (j == ((m - st) / 2)):
            for pi in range(int((st + 1) / 3)):
                print(".|.", end="")
                j += 3
            st = st - 6
        print("-", end="")
        j += 1
    print()
