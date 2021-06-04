def age_assignment(*args, **kwargs):
    names_ages = {}
    for name in args:
        first_letter = name[0]
        names_ages[name] = kwargs[first_letter]
    return names_ages


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


########### SECOND TIME #################

def age_assignment(*args, **kwargs):
    return {name: kwargs[name[0]] for name in args}


print(age_assignment("Peter", "George", G=26, P=19))
