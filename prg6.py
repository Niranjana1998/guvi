leap=int(input())
if((leap%400==0)or((leap%4==0)and(leap%100 != 0))):
    print("yes")
else:
    print("no")
