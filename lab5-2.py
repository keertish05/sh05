N=  int(input('enter any number'))
i=1
while i<=1000:
    if N%i!=0:
        continue
    else:
        print('please enter any number between 1 and 1000')
    N+=1
         