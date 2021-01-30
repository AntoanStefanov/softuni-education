user_name = input()
real_password = input()
trial_password = input()

while trial_password != real_password:
    trial_password = input()
else:
    print(f"Welcome {user_name}!")
