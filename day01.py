with open('input1.txt') as f:
    lines = f.readlines()

data = [int(line.strip())for line in lines]

result1 = sum(1 for n in range(1,len(data)) if data[n] > data[n - 1])
print(result1)

result2 = sum(1 for n in range(1, len(data) - 2) if sum(data[n : n + 3]) > sum(data[n - 1 : n + 2]))
print(result2)
