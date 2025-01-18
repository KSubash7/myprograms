n=int(input("Enter the number: "))
a=str(n)
ams=0
for i in a:
    i=int(i)
    cube=i*i*i
    ams+=cube
print(ams)
if(ams==n):
    print("It is a Amstrong number")

else:
    print("Not a amstrong number")
