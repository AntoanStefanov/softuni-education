def string_explosion(string):

    total_strength = 0
    index = 0
    while index < len(string):
        ch = string[index]
        if ch == ">":
            strength = int(string[index + 1])
            total_strength += strength

        else:
            if total_strength > 0:
                string = string[:index] + string[index + 1:]
                total_strength -= 1
                continue # Защото трием символ и да не инкрементира индекса отдолу

        index += 1

    return string


string = input()

print(string_explosion(string))
