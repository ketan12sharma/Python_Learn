#print(list(range(1,100)))
sum=0
for i in range(100):
    if(i%3==0 or i%5==0):
        sum+=i
    
print(sum)