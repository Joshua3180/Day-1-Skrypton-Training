Y = int(input())
if Y%4==0:
    if Y%100==0:
        if Y%400==0:
            print("Leap Year")
        else:
             print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")