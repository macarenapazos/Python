username = input("What's your name?")
password = input("What's your password?")
passwordlength = len(password)
password = '*' * passwordlength

print(f'{username}, your password {password} is {passwordlength} letter long')