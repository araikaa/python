import math
x=float(input("Enter quantity: "))
y=float(input("Enter quantity: "))
a=math.cos(2*y)+math.sin(4*y)
b=math.sqrt(math.exp(x)+(1/math.exp(x)))
c=math.pow((1/math.exp(x))+(math.exp(x)),3)
d=math.sin(4*y)+math.cos(2*y)-2
g=math.pow(d,2)
print(math.sqrt(a+b)/(c*g))

