num = int(input())
arr = list(map(int, input().split()))
operator = ['*'] * (num - 1)
possible = [[None] * 101 for i in range(num)]
possible[0][arr[0]] = True
end = num - 1
for i in range(num - 1):
  if possible[i][0]:
    end = i
    break
  for x in range(101):
    if possible[i][x]:
      possible[i + 1][(x + arr[i + 1]) % 101] = ('+', x)
      possible[i + 1][(x + 101 - arr[i + 1]) % 101] = ('-', x)
      possible[i + 1][(x * arr[i + 1]) % 101] = ('*', x)
x = 0
for i in range(end, 0, -1):
  operator[i - 1] = possible[i][x][0]
  x = possible[i][x][1]
print(''.join(str(x) for t in zip(arr, operator) for x in t) + str(arr[-1]))