x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()
он

print(x)
outer()
print(x)


# Expected Output
# global
# outer: local
# inner: nonlocal
# outer: nonlocal
# global: changed!

outer outer inner local, v purviq outre promenq li local ?


def outer1():
    x = 20
    def outer2(): 
        x = 10
        def inner():
            nonlocal x
            x = 5
