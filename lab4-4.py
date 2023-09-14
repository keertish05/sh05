N=input()
count=0
while true:
    num=int(input('enter any number'))
    if num==-999:
        break
    else:
        num%N==0
        count+=1
        print(count)
