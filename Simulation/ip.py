def is_valid_ipv4(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255 or (part != str(num)):
            return False
    return True
while True:
   user_input = input("\nEnter an IP address to verify: ").strip()
   if is_valid_ipv4(user_input):
      print("it is a VALID IPv4 address.")
      break
   else:
      print("it is INVALID.enter a valid ipv4!!")
