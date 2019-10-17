# namedtuples provides the functionality of tuples with the readibility of dictionaries. 
# Basically a compromise between the two
# namedtuple returns a sub-class of tuple with named attributes.

from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue']) # subclass of tuple called Color
#color = Color(66,89, 90) or 
color = Color(red=54, blue=65, green=56)

print(color.blue)

# acces the doc string for the class
Color.__doc__

# convert to dict
color_dict = color._asdict()

# convert from dictionary
color_ntup = Color(**color_dict)
print(color_ntup)