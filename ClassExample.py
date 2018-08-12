class Robot:
    def __init__(self,  n,c,w):
        self.name=n
        self.color=c
        self.weight=w

    def introduce_self(self):
        print("My name is : "+self.name)

a=Robot("Tom","Red",30)
a.introduce_self()
print(type(True))

a1=[x**2 for x in range(-6,0)]
print(a1)