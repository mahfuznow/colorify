
![logo](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/icon.jpg) 

## Colorify

>Did you find it difficult to read your output in the terminal while running a python script? Here comes colorify. It will provide you a huge range of color to choose from to print any text in the terminal with color.


### How to use?

**Install the library :**
```bash
pip install colorify

```

**Example code:**
```python

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
print(colorify("Info  ", C.white, C.blue))
```
### Output
![output1](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/output1.JPG) ____________ ![output](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/output2.JPG)


> 
    1. First output is generated from light themed terminal
    2. Sencond output is generated from dark themed terminal 


## Color options

```python
print(colorify("Your text", C.color_name , C.color_name))
```

### Basic colors:
![color_palette](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/color-basic.JPG)


### More colors:
![color_palette](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/color-1.JPG)![color_palette](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/color-2.JPG)![color_palette](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/color-3.JPG)![color_palette](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/color-4.JPG)![color_palette](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/color-5.JPG)![color_palette](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/color-6.JPG)![color_palette](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/color-7.JPG)![color_palette](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/color-8.JPG)![color_palette](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/color-9.JPG)![color_palette](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/color-10.JPG)![color_palette](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/color-11.JPG)

### Need more colors?
```python
#use your own RGB color
print(colorify("Your text", (r,g,b) , (r,g,b)))
```
