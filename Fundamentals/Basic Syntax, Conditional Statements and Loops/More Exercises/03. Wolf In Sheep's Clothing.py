queue = input().split(", ")

for number, animal in enumerate(queue, start=-len(queue)):
    if animal == "wolf":
        wolf_number = abs(number)
if wolf_number == 1:
    print("Please go away and stop eating my sheep")
else:
    print(
        f"Oi! Sheep number {wolf_number - 1}! You are about to be eaten by a wolf!")

########## OR ###########

# array = input().split(", ")

# if array.pop() == "wolf":
#     print("Please go away and stop eating my sheep")
#     raise SystemExit

# arrReversed = array[::-1]
# # start : end : step , така започва от началото , но на обратно

# for i in range(len(arrReversed)):
#     if arrReversed[i] != "sheep":
#         print(
#             f"Oi! Sheep number {i + 1}! You are about to be eaten by a wolf!")
