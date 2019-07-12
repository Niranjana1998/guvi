num = int(input())
sum = 0
nj = num
while nj > 0:
   digit = nj % 10
   sum += digit ** 3
   nj //= 10
if num == sum:
   print("yes")
else:
   print("no")
