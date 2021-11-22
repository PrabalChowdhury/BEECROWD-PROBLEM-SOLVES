import math
A,B=list(map(float,input().split()))                              
C,D=list(map(float,input().split()))
D= math.sqrt(pow(C-A,2)+pow(D-B,2))
print(f'{D:0.4f}')
