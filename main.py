v = input()
c = int(v,2)
print(c)#задание 1

a = int(input(""))
b = bin(a)
print(b)#задание 2

N = int(input())
M = int(input())
T = int(input())
h = (N + (M + T) // 60) % 24
m = (M + T) % 60
print(f'{h}:{m}')
