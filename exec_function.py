

N = int(input("N: "))
arr = []

for _ in range(N):
   s = input()
   if s == 'print':
       print(arr)
   else:
       f, *args = s.split()
       exec(f'arr.{f}({",".join(args)})')
