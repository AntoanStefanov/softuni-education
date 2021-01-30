class User:
    pass


# user 1 is an "instance" of the User class / User 1 е отделен случай от User класа
# user 1 is an "object"/ user 1 е обект
user1 = User()

# To attach data to this object , you first type the name of the object , a dot , the name of the variable, and give it a value

user1.first_name = "Dave"
user1.second_name = "Bowman"

# Since first_name and last_name are attached to an object, we call them FIELDS - data attached to an object.
# They store data specific to user1

# To see that the data is in the user1-object, let's print them
# You access the data the same way you assigned it(object name,dot,field name)
# field names - lowercase and underscores as variables(PEP - 8)
print(user1.first_name)
print(user1.second_name)

# Here the name Dave Bowman is attached to the object user1.
# To make this clear, let's create standalone variables

first_name = "Arthur"
second_name = "Georgiec"

# These variables are not attached to a user object

print(first_name, second_name)

# But if you print the variables attached to user 1 , you get Dave Bowman

print(user1.first_name, user1.second_name)

# Even though we used the same variable names, the values are kept seperate.


# With classes, there is no limit to the number of the objects you can make.


# Let's make second user.

user2 = User()

user2.first_name = "Frank"
user2.second_name = "Poole"

# We use the exact same field names as before, but this time  the values are attached to user 2


# To see , that Python keeps these three names seperate, we will print the three names


print(first_name, second_name)
print(user1.first_name, user1.second_name)
print(user2.first_name, user2.second_name)


# So classes are used to make objects, and each object can have different values for the same variable names.


# You can attach additional fields to the objects, and they do not have to be strings.
# Let's suppose the user1 has an age of 37


user1.age = 37
user2.favourite_book = "Pinokio"

# We are now in situation , where user 1 and user 2 have different fields attached to them.

# The user 1 has an age. User 2 does not.

print(user1.age)

# When we try to print the age of user 2, which we have not assigned , we get an attribute error
