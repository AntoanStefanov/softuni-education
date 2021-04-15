def kwargs_length(**kwargs):
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25, 'address': 'Al.Stamb'}

print(kwargs_length(**dictionary))
