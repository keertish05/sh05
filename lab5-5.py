a=int(input('enter any number'))
b=int(input('enter any number'))
L=max(a,b)
if L%a==0 and L%b==0:
  print(L)
else:
  print('not L')
  L+=1

