from colorify import *

# initializing COLORIFY
init_colorify()

# text color = green
print(colorify("Sucess", C.green))
# text color = black , background color = green
print(colorify("Sucess", C.black, C.green))

print(colorify("Error ", C.red))
print(colorify("Error ", C.white, C.red))

print(colorify("Alert ", C.orange))
print(colorify("Alert ", C.black, C.orange))

print(colorify("Info  ", C.blue))
print(colorify("Info  ", C.white, C.crimson))
