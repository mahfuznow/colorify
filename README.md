
![logo](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/icon.jpg) 

# Colorify

>Did you find it difficult to read your output in the terminal or while running a python script? Here comes colorify. It will provide you a huge range of color to choose from to print any text in the terminal with color.

## Installation

**Install python3 :**
```bash
apt install python3
```
**Install pip :**
```bash
apt install python3-pip
```
**Install the library :**
```bash
pip install colorify
```


## How to use?
### Use in command line
**library usages:**
```bash
colorify -h
```
Or,
```bash
colorify --help
```
**Output**
![output0](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/output0.JPG) ____________ 


**Example commands**
```bash
colorify "Random Colored text"
colorify "Random Colored text"
colorify "Random Colored text"
colorify "Random Colored text"
colorify "Random Colored text"
colorify "Random Colored text"
colorify "Random Colored text"
colorify "Random Colored text"
colorify "Random Colored text"
colorify "Random Colored text"
```
**Output**
![output1](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/output1.JPG) ____________ ![output2](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/output2.JPG)

> 
    1. First output is generated from light themed terminal
    2. Sencond output is generated from dark themed terminal 


**Example commands:**
```bash
# text color = green
colorify -tc green Success
# text color = black , background color = green
colorify -tc black -bc green Succes))

colorify -tc red Error
colorify -tc white -bc red Error

colorify -tc orange Alert
colorify -tc black -bc orange Alert

colorify -tc blue Info
colorify -tc white -bc blue Info
```
Or,

```bash
# text color = green
colorify --text-color green Success
# text color = black , background color = green
colorify --text-color black --background-color green Succes))

colorify --text-color red Error
colorify --text-color white --background-color red Error

colorify --text-color orange Alert
colorify --text-color black --background-color orange Alert

colorify --text-color blue Info
colorify --text-color white --background-color blue Info
```

**Output**
![output1](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/output3.JPG) ____________ ![output](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/output4.JPG)

> 
    1. First output is generated from light themed terminal
    2. Sencond output is generated from dark themed terminal 


### Use in python script

**Example code:**
```python

from colorify import *

# initializing COLORIFY
init_colorify()

#this will generate text in random color each time
for i in range(10):
    print(colorify("Random Colored text"))
```
**Output**
![output3](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/output1.JPG) ____________ ![output4](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/output2.JPG)

> 
    1. First output is generated from light themed terminal
    2. Sencond output is generated from dark themed terminal 



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

**Output**
![output1](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/output3.JPG) ____________ ![output](https://raw.githubusercontent.com/mahfuznow/colorify/master/images/output4.JPG)

> 
    1. First output is generated from light themed terminal
    2. Sencond output is generated from dark themed terminal 



## Color options

**In command line:**
```bash
colorify [-h] [-tc TEXT_COLOR] [-bc BACKGROUND_COLOR] [-l] [-v] text
```
List all color:
```bash
colorify -l
```
Or,
```bash
colorify -cl
```
Or,
```bash
colorify --color-list
```

**In python script:**
```python
print(colorify("Your text", C.TEXT_COLOR , C.BACKGROUND_COLOR))
```
List all color:
```python

from colorify import *

# initializing COLORIFY
init_colorify()
#this will print the list of all available color
printAllColor()
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
