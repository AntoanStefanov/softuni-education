user_names = input().split(", ")


def valid_user_names(user_names):
    valid_user_names = []
    for user in user_names:
        valid = True
        user_name = ''
        if 3 <= len(user) <= 16:

            for char in user:
                if char.isalnum():
                    user_name += char
                elif char is "-" or char is "_":
                    user_name += char
                else:
                    valid = False
                    break
            if valid:

                valid_user_names.append(user_name)
    return "\n".join(valid_user_names)


print(valid_user_names(user_names))
