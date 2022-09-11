import math
 
AB = input("Length of the first leg: ")
AC = input("Second leg length: ")
 
AB = float(AB)
AC = float(AC)
 
BC = math.sqrt(AB**2 + AC**2)
 
S = (AB * AC) / 2
P = AB + AC + BC
 
print('Triangle area:',S)
print('Perimeter of triangle:',P)
