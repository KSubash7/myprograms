n=int(input("Enter the nth number:"))
if(n==0):
    print("you entered 0")
else:
    sum=0
    for i in range(1,n+1):
        sum=sum+i
print(sum)
