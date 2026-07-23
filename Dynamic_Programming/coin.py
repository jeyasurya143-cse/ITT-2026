A=int(input("enter number of coins for suresh:"))
B=int(input("enter number of coins for sundar:"))
if A>=B:
   C=int(input("sundar lost,enter a coin given by raja:"))
   B=B+C
else:
   C=int(input("suresh lost,enter a coin given by D:"))
   A=A+C
if A>=B:
   D=int(input("sundar lost after coin given by raja . enter D coin:"))
   B=B+D
else:
   D=int(input("suresh lost after coin given by raja . enter D coin:"))
   A=A+D
if A>=B:
   print("suresh is winning")
else:
   print("sundar is winning")
