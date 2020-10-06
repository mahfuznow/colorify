import sys
from .colorify import *
from argparse import ArgumentParser

if __name__ == '__main__':
    main()

def main():
    #print('in main')
    # args = sys.argv[1:]
    # print('count of args :: {}'.format(len(args)))
    # for arg in args:
    #     print('passed argument :: {}'.format(arg))
    #     print(colorify(format(arg),C.light,C.orange))

    #initializing parser
    parser = ArgumentParser()
    # definiing required argument
    parser.add_argument('text', help='Text')
    #defining optional arguments
    parser.add_argument('-tc', '--text-color', help='Text color',type=str)
    parser.add_argument('-bc', '--background-color', help='Background color',type=str)

    args = parser.parse_args()

   

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


