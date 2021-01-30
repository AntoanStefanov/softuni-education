########## FUNCTION WITH PARAMETERS/ARGUMENTS ####
def string(first_char, second_char, third_char):
    print(f"{first_char}{second_char}{third_char}")


string(input(), input(), input())
################ OR ##############
first_char = input()
second_char = input()
third_char = input()

print(f"{first_char}{second_char}{third_char}")
####### FUNCTION W/ NO PARAMETERS/ARGUMENTS #########


def string1():
    first_char = input()
    second_char = input()
    third_char = input()

    print(f"{first_char}{second_char}{third_char}")


string1()
# EXAMPLE OF DEFINING FUNCTION


def greet():  # defining function = def , function name = greet , () , :
    # indentation, which means the following statements belong to this funtion
    print("Hello there!")  # statement
    print("Welcome aboard")  # statement


    # Now we are done with this function , we need to CALL it. So, we remove the indentation , and add two line break after this funtion (pep-8 recommends, clean code !)
greet()  # calling this function , with () . Just like we call the build in functions
