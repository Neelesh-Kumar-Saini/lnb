arr = [23, 22, 24, 8, 9, 10]
max  =arr[-1]
print(max, end='')
for i in range(1, len(arr)-1):
  if arr[-i]>max:
    max = arr[-i]
    print(", ",arr[-i])
