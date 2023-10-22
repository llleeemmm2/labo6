with open('input.txt', 'r') as file:
    n = list(map(int, file.read().split()))

s = 1
for i in n:
    s *= i

with open('output.txt', 'w') as file:
    file.write(str(s))