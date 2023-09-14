X=int(input('enter a number '))
Y=int(input('enter a number '))
N=int(input('enetr a number '))
i=X
while(i<=Y):
    if(i%N==0):
        print(i,"is divisible by",N)
    i=i+1