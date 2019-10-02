# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print(f)

# # re-declaring the variable works
f = "abc"
print(f)

# # ERROR: variables of different types cannot be combined
# print("this is a string" + 123)
print("this is a string " + str(123))

# Global vs. local variables in functions


def some_function():
    f = "def"
    print(f)


def some_other_function():
    global f
    f = "jig"
    print(f)


print(f)
print("func")
some_function()
print("other func")
some_other_function()
print("global f")
print(f)
del f
# print(f) error because no global f defined
