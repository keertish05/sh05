num_1=int(input('enter any number'))
num_2=int(input('enter any number'))
range=min(num_1,num_2)
i=1
while i<=range:
    if num_1%i==0 and num_2%i==0:
        hcf=i
        i+=1
        print(hcf)