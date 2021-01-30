words = input().split(", ")
# Не е нужно да сплитваме , приемаме цялото за стринг, место да проверяваме дума по дума(лист).
text = input()

matched_words = [word for word in words if word in text]
print(matched_words)
