# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Perparing", order)

# this will concatinate the Ginger chai in the preparing and the output is Perparing Ginger chai
# prepare_chai(chai)
# here the output is just Ginger chai
# print(chai)

# this is list - it can be mutable
# chai = [1,2,3]

# def edit_chai(cup):
#     cup[1] = 42

# # here the list second item will change and output will be [1, 42, 3]
# edit_chai(chai)
# print(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "low") # positional parameter
make_chai(tea = "Green", sugar="Low",milk="Yes") # keyword parameter


def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("cinnamon","cardmom", sweetner="Honey", foam="yes")
# In python there are two type of arguments - 1. args (normal arguments) 2. *kwargs (keyword arguments) or we call key value arguments
# output - for special_chai() would be Ingredients ('cinnamon', 'cardmom') Extras {'sweetner': 'Honey', 'foam': 'yes'}

# def chai_order(order = []):
#     order.append("Masala")
#     print(order)

# chai_order()
# chai_order()
# this will append ['Masala'] and ['Masala', 'Masala'] two times in the second output.


# here the value will only add when we pass that value
def chai_order(order = None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()
