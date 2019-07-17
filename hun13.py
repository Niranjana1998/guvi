nj = input()
stack = []
for k in nj:
    stack.append(k)
if nj == ''.join([x for x in nj[::-1]]):
    print('YES')
else:
    print('NO')
