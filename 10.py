x = 5
y = "John"
# print(x + y) #error
print(f"{x} - {y}")

x = "awesome" # Global varible

def myfunc():
    y = 'hello' # Local variable
    print("Python is " + x + ' ' + y)

def myfunc(2):
    y = 'hello' 
    print("2Python is " + x)


print(y)     # not available

myfunc()
myfunc2()