days = int(input())
treated_patients = 0
untreated_patients = 0
doctors = 7
for day in range(1, days + 1):
    new_patients = int(input())
    if day % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    if doctors < new_patients:
        untreated_patients += new_patients - doctors
        treated_patients += doctors
    else:
        treated_patients += new_patients
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")


############# OR #############


days = int(input())

treated_patients = 0
untreated_patients = 0
doctors = 7

for day in range(1, days + 1):
    new_patients = int(input())

    if day % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1

    if doctors < new_patients:
        untreated_patients += new_patients - doctors
        treated_patients += doctors
    elif doctors >= new_patients:
        treated_patients += new_patients


print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
