keyword_list = ["water", "fish", "sun", "sand"]
text = input().lower()
matched_words = []
for keyword in keyword_list:
    if keyword in text:
        matched_words.append(text.count(keyword))
total = sum(matched_words)
print(total)
