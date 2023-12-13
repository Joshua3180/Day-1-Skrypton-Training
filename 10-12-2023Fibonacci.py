Fbonaci = int(input("How Many Fibonacci Numbers (For Example say 100): "))

n1 = 0
n2 = 1
count = 0


if Fbonaci <= 0:
   print("Please enter a positive integer")

elif Fbonaci == 1:
   print("Fibonacci numbers upto",Fbonaci,":")
   print(n1)

  # ekada fibonacci sequence generate aithdhi and then values update cheyali

else:
   print("Fibonacci numbers:")
   while count < Fbonaci:
       print(n1)
       nth = n1 + n2
       
       n1 = n2
       n2 = nth
       count += 1