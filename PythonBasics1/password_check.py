username = input("What is your username? ")
password = input("What is your password? ")

password_length = len(password)
pass_star = '*' * password_length
print(f'Hey {username}, your password {pass_star} is {password_length} letters long!')