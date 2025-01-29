year = int(input("Enter the year:"))
y="Leap year" if(year%4==0 and year%400==0 or year%4==0 and year%100!=0) else "Not a Leap year"
print(y)
