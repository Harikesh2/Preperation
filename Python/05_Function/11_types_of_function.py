# Types of function
# Pure  Impure 
# Recursive Function
# Lambdas (Anonymous Function) 

# Pure  Impure 
def pure_chai(cups):
    return cups * 10;

total_chai = 0 
# not recommended this type of function defining because you can change the global variable
def impure_chai(cups):
    global total_chai
    total_chai += cups

# recursion function
def pour_chai(n):
    print(n)
    if n == 0 :
        return "All cup poured"
    return pour_chai(n-1)

print(pour_chai(3))

# lambdas function 
chai_types = ["Ginger","kadak", "Light", "kadak"]

# list - is the build in mutable squence and filter is the filter squence
strong_chai = list(filter(lambda chai: chai == "kadak",chai_types))
# here the lambda syntax is lambda chai: chai == "kadak" and the list
print(strong_chai)

# https://docs.python.org/3/library/functions.html  - Buid-in function in python