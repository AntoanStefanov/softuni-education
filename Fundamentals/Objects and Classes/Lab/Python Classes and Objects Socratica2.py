import datetime
# The first feature we will add is an init method
# A function inside a class is called method
# init == initialization a.k.a "Constructor"
# The name of this method is init with double underscores before and after.
# This method is called everytime you create a new instance of the class.
# The first argument to this method is the word self, which is a reference to the new object that is being created.
# You can add additional arguments after self. We will add full_name and birthday arguments
# The first thing we will do is store these values to fields in the object.
# We do this by typing self , dot , the field name , and then we assign it a value.
# We will store the full name as a field called name, but we will store the value birthday in a field also called birthday.
# Second birthday is the value provided when you create a user object , but the first birthday is the field that stores the value


class User:
    # DocString
    """ 
    A member of FriendFace. For now we are only storing their name and birthday.

    """

    def __init__(self, full_name, birthday):

        self.birthday = birthday  # yyyymmdd

        # Extract the first and last names
        # We will call the split method on the full_name, the pieces will be sotred in an array
        name_pieces = full_name.split()
        # the first name will be the first string in that array
        self.first_name = name_pieces[0]
        # the last name will be the last string in that array
        self.last_name = name_pieces[-1]
        # Notice that we attached the first_name to self. And last name didn't
        # We will see the results
    # Let's add another method to the User class that will return the age of the user in years.
    # Like the init method th first argument is self
    # And to show our responsible nature , add a brief docstring.

    def age(self):
        """
        Return the age of the user in years.
        """
        # We will compute the age using the user's birthday, so this method doesn't require any additional parameters.
        # Since we will be working with states we need to import the data/time module
        # Let's first get the today's date. We shall assume it is May 21st , 2001. For same answer for everybody
        today = datetime.date(2001, 5, 12)
        # Next convert the birthday string into a data object
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        # With these three int we can create a date object, for the user birthday
        date_of_birth = datetime.date(yyyy, mm, dd)
        # If you compute the difference between today and date of birth, you get time delta object.
        #  The time delta object has a field called days.
        age_in_days = (today - date_of_birth).days
        # ignoring leap years , we can now compute the age in years by dividing by 365
        age_in_years = age_in_days / 365
        # finally return the age in years
        return int(age_in_years)

        # To test this method call the age method and print the result


# We will now create a user and use the init method
# We must provide two values
user = User("Dave Bowman", "19710315")

# We can test that these values are stored in the object
print(user.name)
print(user.birthday)


# Let's add another feature to our class..
# In the init method let's break apart the name and txtract the first and last names

print(user.name)
print(user.first_name)
print(user.last_name)
# 'User' object has no attribute "last_name". This is because we didn't attach last name to the object using self.
# We assigned the value to the variable last_name, which only exists until the end of the method.
# Let's go back and attach last_name to self
print(user.birthday)


# We can further improve this class by adding help text. To do this , you type special string , we call a docstring.
# Now look what will happen when you call help function to this class.
help(User)
# Python displays a useful overview of the User class

# Displays the docstring summary , and it also shows the arguments that are expexted in the init method.
# It's good idea to weite docstrings

# help call displays two additional items - dict and weakref

print(user.age())

# You did not type self when calling age method . The self keyword is only used when writing a method

# if you call the help func once more , you will see the summary now includes a description of the age method
