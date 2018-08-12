
N = int(input())
if N%2!=0:
    print("Weird")
if (N%2==0 and N<=5 and N>=2):
    print("Not Weird")
if (N%2==0 and N<=20 and N>=6):
    print("Weird")
if (N%2==0 and N>=20):
    print("Not Weird")
