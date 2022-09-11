import math
x=0.8
y=0.1
z=4
print('x=',x)
print('y=',y)
print('z=',z)
r=x-7*y
c=math.acos(r)/math.asin(r)
a=1-x+c
b=4*x*z-math.pow(math.log(y),2)
print(math.pow((a/b),1/5))
