desired_height_lath = int(input())

current_height_lath = desired_height_lath - 30
total_jumps = 0
is_failed = False

while True:

    for jump in range(1, 4):
        current_jump = int(input())
        total_jumps += 1
        if current_jump > current_height_lath:
            break
        elif jump == 3:
            is_failed = True

    if is_failed:
        print(
            f"Tihomir failed at {current_height_lath}cm after {total_jumps} jumps.")
        break
    current_height_lath += 5
    if current_height_lath > desired_height_lath:
        print(
            f"Tihomir succeeded, he jumped over {desired_height_lath}cm after {total_jumps} jumps.")
        break
