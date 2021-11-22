A,B,C=input().split(" ")
maior = (int(A) + int(B) + abs(int(A) - int(B)))  / 2
result = (int(maior) + int(C) + abs(int(maior) - int(C)))/2
print("%d eh o maior" %result)
