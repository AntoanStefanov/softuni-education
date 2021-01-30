command = input()
steps = 0
while command != "Going home":
    steps += int(command)
    if steps >= 10_000:
        print("Goal reached! Good job!")
        print(f"{steps - 10_000} steps over the goal!")
        break
    command = input()
else:
    steps_to_home = int(input())
    steps += steps_to_home
    if steps >= 10_000:
        print("Goal reached! Good job!")
        print(f"{steps - 10_000} steps over the goal!")
    else:
        print(f"{10_000 - steps} more steps to reach goal.")


# ТОВА Е АКО Е ВЪЗМОЖНО НА ДВА РЕДА ДА СЕ НАПИШЕ "GOING" на един и "home" на другия ! НЕ Е ПО ЗАДАЧАТА , но така е по трудно и се опитах да го направя

goal = 10000

total_steps = 0
command_counter = 0
while goal > total_steps:
    inpt = input()
    if inpt == "Going" or inpt == "home":
        command_counter += 1
        inpt = input()
        if command_counter == 2:
            steps_to_home = int(input())
            more_steps = goal - total_steps - steps_to_home
            break
        continue

    if inpt == "Going home":
        steps_to_home = int(input())
        total_steps += steps_to_home
        if total_steps >= goal:
            over_steps = total_steps - goal
            break

        else:
            more_steps = goal - total_steps
            break
    steps = int(inpt)
    total_steps += steps
    if total_steps >= 10000:
        over_steps = total_steps - goal
        break

if total_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{over_steps} steps over the goal!")
else:
    print(f"{more_steps} more steps to reach goal.")
