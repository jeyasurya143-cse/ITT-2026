email = input("enter your email:")
flag="false"
if email=="":
   flag="false"
elif ' ' in email:
    flag = "false"
elif email.endswith("@gmail.com"):
    flag = "true"
elif email.endswith("@mepcoeng.ac.in"):  #it is only used for my college domain
    flag = "true"
else:
   for i in email:
      if i.isupper():flag = "false"
      else:flag = "true"
if flag == "true":
    print("valid")
else:
    print("invalid")
