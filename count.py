n=int(input("Enter the Number:"))
a=str(n)
e_count=0
o_count=0
for i in a:
    i=int(i)
    if(i%2==0):
        e_count+=1
    else:
        o_count+=1

print(f"{n} count of even digits is {e_count}")
print(f"{n} count of odd digits is {o_count}")
