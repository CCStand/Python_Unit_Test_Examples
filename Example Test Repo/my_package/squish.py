class Squishable_Class():
    """This is a custom class that stores 3 values and has a method that returns these values as a list"""
    def __init__(self, thing1="", thing2="", thing3=""):
        self.thing1 = thing1
        self.thing2 = thing2
        self.thing3 = thing3
        
    def get_attribute_val_list(self):
        """A method that returns these values as a list"""
        attribute_dict = vars(self)
        val_list = []
        for val in attribute_dict.values():
            val_list.append(val)
        return(val_list)
    
def imperfect_squish(thing1, thing2):
    """A function that concatenates two strings, but that adds two
       numbers and will crash if a string and a number are passed)."""
    return(thing1 + thing2)

def squish(thing1, thing2):
    """A function that converts two values into strings and concatenates them."""
    thing1 = str(thing1)
    thing2 = str(thing2)
    return(thing1 + thing2)

def dense_squish(thing1, thing2):
    """A function that converts two values into strings, concatenates them,
       and removes any spaces."""
    thing1 = str(thing1).replace(" ", "")
    thing2 = str(thing2).replace(" ", "")
    return(thing1 + thing2)

def sparse_squish(thing1, thing2):
    """A function that converts two values into strings, concatenates them,
       and adds a space between them."""
    thing1 = str(thing1)
    thing2 = str(thing2)
    return(thing1 + " " + thing2)

def squish_list(thing_list):
    """A function that takes a list, converts all element of the list into strings, 
       and concatenates them."""
    squished = ""
    for thing in thing_list:
        squished = squished + str(thing)
    return(squished)

def squish_object(squishable_object):
    """A function that takes a Squishable_Class object, converts all of its elements 
       into strings, and concatenates them."""
    thing_list = squishable_object.get_attribute_val_list()
    
    squished = ""
    for thing in thing_list:
        squished = squished + str(thing)
    return(squished)