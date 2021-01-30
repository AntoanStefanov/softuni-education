

companies = {}

while True:

    data = input()

    if data == "End":
        break

    company_name, user_id = data.split(" -> ")

    if company_name not in companies:
        companies[company_name] = []
        
    # if user_id not in companies.values():
    #     companies[company_name].append(user_id) Защо това не работи, а това работи:
    if user_id not in companies[company_name]:
        companies[company_name].append(user_id)

sorted_companies = dict(sorted(companies.items()))

for company, users_ids in sorted_companies.items():
    print(company)
    for user_id in users_ids:
        print(f"-- {user_id}")
