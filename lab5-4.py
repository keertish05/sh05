N=input(input('enter any number'))
divisible_count=0
non_dividible_count=0
while True:
    num=int(input('enter any number'))
    if num==-999:
        break
    if  num%N==0:
         divisible_count+=1
    else:
        non_dividible_count+=1
    print(divisible_count)
    print(non_dividible_count)