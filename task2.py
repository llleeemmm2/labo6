with open('input1.txt', 'r') as file:
    n = list(map(int, file.read().split()))

def insertionSort(n):
    a = len(n)
    for i in range(1, a):
        for j in range(i, 0, -1):
            if n[j] < n[j - 1]:
                n[j], n[j - 1] = n[j - 1], n[j]
            else:
                break

insertionSort(n)
with open('output1.txt', 'w') as file:
    for i in range(len(n)):
        file.write(str(n[i]) + '\n')