a = int(input(' Write a number: '))
s = 0
for i in range(a):
    s, a = s + a % 10, a//10
    s = s + a % 10
    a = a//10
print('Result = ', s)
