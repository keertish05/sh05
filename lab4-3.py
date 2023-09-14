N=int(input("enter a number "))
sum=0
if n>0:
    while n>0:
        num=N%10
        sum+=num
        N=N//10
        print(sum)
else:
    print("enter a positive number")