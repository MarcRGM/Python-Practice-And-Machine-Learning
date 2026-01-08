a=10; b=20
def my_function():
    global a
    a=11; b=21
    
my_function()
print(a) #prints 11
print(b) #prints 20

# In the preceding code, we define two global variables. We need to tell the interpreter, using
# the keyword global, that inside the function, we are referring to a global variable. When
# we change this variable to 11, these changes are reflected in the global scope. However, the
# variable b we set to 21 is local to the function, and any changes made to it inside the
# function are not reflected in the global scope.