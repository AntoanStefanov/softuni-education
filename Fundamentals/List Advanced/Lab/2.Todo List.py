
notes = []
while True:
    note = input()
    if note == "End":
        break
    importance, action = note.split("-")
    importance = int(importance)  # Обръщалка иначе 80/100
    # Tuple , защото е непроменяем , тук не се налага да се променя и за това го изполва месец may.
    notes.append((importance, action))


# Деградиране на tuple , sorted може да сортира и tuples по нулевия индекс , ако те са равни проверява следващите
# и когато срещне разлика , който е по-малък от другия - целият лист става първи . (Comprehension)
notes_by_importance = [note for importance, note in sorted(notes)]
print(notes_by_importance)


# EXAMPLE ####### THEY ARE THE SAME
# Without Comprehension

notes_by_importance = []
for importance, note in sorted(notes):
    # Тук ако има проверка се проверява (Optinal)
    if note == "Walk the dog":  # Само когато note е "Walk the dog" , тогава добави
        notes_by_importance.append(note)
print(notes_by_importance)

# With Comprehension

notes_by_importance = [note for importance,
                       note in sorted(notes) if note == "Walk the dog"]
