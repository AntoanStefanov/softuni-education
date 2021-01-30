number = int(input())


def loading_percentage_info(number):
    return f"{number}% "


def loading_bar_in_bracets(number):
    total_in_bracets_symbols_and_dots = 10
    symbols = (number // 10) * "%"
    dots = (total_in_bracets_symbols_and_dots - (number//10)) * "."
    return f"[{symbols}{dots}]"


def loading_bar(number):
    loading_bar = loading_bar_in_bracets(number)
    if loading_percentage_info(number) == "100% ":
        return "100% Complete!\n" + loading_bar
    else:
        return loading_percentage_info(number) + loading_bar + "\nStill loading..."


print(loading_bar(number))
