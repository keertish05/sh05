Y=int(input('enter any number'))
X=int(input('enter any number'))
Z=int(input('enter any number'))
sum=X+Y or Y+Z or Z+X
if(sum>Z or sum>Y or sum>X):
    print('sides of triangle')
else:
        print('invalid')