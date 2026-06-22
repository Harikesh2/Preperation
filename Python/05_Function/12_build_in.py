# https://docs.python.org/3/library/functions.html  - Buid-in function in python

def chai_flavour(flavour="masala"):
    """Return the flavour of chai"""
    chai = "ginger"
    return flavour

print(chai_flavour.__doc__)
print(chai_flavour.__name__)

#help(len)

def generate_bill(chai = 0, samosa = 0):
    """
    Calculate the total bill for the chai and samosa 

    : params chai : Number of chai cups (10 rupess each)
    : params samosa : Number of samosa (15 rupess each)
    : return (total amount, Thank You !!)
    """
    total = chai*10 + samosa*15
    return total , "Thank You For Shopping With Us!!"

print(generate_bill(1, 3))