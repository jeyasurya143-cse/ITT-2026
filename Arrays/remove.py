n=eval(input("enter the number:"))
a=int(input("enter the key:"))
l=len(n)
s=0
print("[",end="")
for i in range(l):
   if n[i]!=a:
      s=s+1
      print(n[i],end=",")
   else:
      continue
for j in range(l-s):
   print("_",end=",")
print("]\n","no of remaining elements:",s)
