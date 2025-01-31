n=int(input("Enter the number:"))
count=0
for i in range(1,n):
    if(n%i==0):
        count+=i
        print(count)
if(count==n):
    print("true")
else:
    print("false")
