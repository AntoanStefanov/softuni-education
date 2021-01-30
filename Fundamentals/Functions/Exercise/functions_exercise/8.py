def fill_bar(bar_list, n_bars_to_check):
    for index in range(n_bars_to_check):
        bar_list[index] = "%"
    return bar_list

bar = []

# Place the dots
for num in range(10):
    bar.append(".")

percent = int(input())
bars_to_fill = percent//10

filled = fill_bar(bar, bars_to_fill)

if percent < 100:
    print(f"{percent}% [{''.join(filled)}]")
    print("Still loading...")
else:
    print("100% Complete!")
    print(f"[{''.join(filled)}]")