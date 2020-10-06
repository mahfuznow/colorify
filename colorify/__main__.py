import sys
from .colorify import *
from argparse import ArgumentParser

#main method will be called from setup.py
if __name__ == '__main__':
    main()

def main():
    parser1 = ArgumentParser()

    #firstly search for "-cl or --color-list" in argument
    #we are doing this separately so that in this case "text" argument is't required
    #add_help = False parameter will make sure that help functionalites works for the remaining_args only
    parser1 = ArgumentParser(add_help=False)
    parser1.add_argument('-l','-cl', '--color-list', dest='color_list', action='store_true',
                    help='this is an optional argument that prints stuff')
    #parsing known arguments as "args" & unknown arguments as "remaining_arg"
    args, remaining_args = parser1.parse_known_args()
    # if found then print all the colors
    if args.color_list:
        printAllColor()
    #if not found continue our main argument
    else:
        parser2 = ArgumentParser()
        # definiing required argument
        parser2.add_argument('text', help='Text')

        #defining optional arguments
        parser2.add_argument('-tc', '--text-color', dest='text_color', help='Set Text color',type=str)
        parser2.add_argument('-bc', '--background-color', dest='background_color', help='Set Background color',type=str)
        
        #this is a dummy argument to be shown in "help"
        parser2.add_argument('-l','-cl', '--color-list', dest='color_list', help='List of all colors', action="store_true")
        #this will print the program name with the version number
        parser2.add_argument('-v', '-V','--version', action='version', version='%(prog)s {version}'.format(version=version_number))
       

        args =  parser2.parse_args(remaining_args)


        text = args.text

        
        if args.text_color:
            text_color = args.text_color
        #if text color is not provided generate a random one
        else:
            text_color = getRandomColorName()

        if args.background_color:
            background_color = args.background_color
            print(colorify(text,
                    getattr(C, text_color)
                    ,getattr(C, background_color)))
        #if background color is not provided, print without background
        else:
            print(colorify(text,
                        getattr(C, text_color)))
