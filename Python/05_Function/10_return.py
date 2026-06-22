# Nothing --> implicitly return None 
# One Value 
# Multiple Value
# Early From A Function

# Nothing --> implicitly return None 
# def make_chai():
#      # return "Here is your masala chai"
#     print("Here is your masala chai")

# return_value = make_chai()
# print(return_value) # now this will be None because we don't have any return value for the function

def idle_chaiwala():
    pass

print(idle_chaiwala()) # output would be none  --> # Nothing --> implicitly return None


def sold_cup():
    return 120  # one value return 

total = sold_cup()
print(total)

def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "chai is ready"
    print("chai")

print(chai_status(0))  # early From a function will not print chai is ready
print(chai_status(5)) #
 

#  multiple value
def chai_report():
    return 100, 20, 10 # Sold, remaining -> here third value will throw error --> 

sold, remaining, not_paid = chai_report() # --> we can handle that by adding a _ or not_paid after the value

print("Sold", sold)
print("Remaining", remaining)
