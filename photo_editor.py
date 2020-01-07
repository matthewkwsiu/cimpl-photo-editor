# SYSC 1005 A Fall 2018 Lab 7

import sys  # get_image calls exit
from Cimpl import *
from filters import *

def get_image():
    """
    None => image
    
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    
    >>>get_image()
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img


def show_commands():
    """
    None => None
    
    prints out all the commands available
    
    >>>show_commands
    L)oad image
    B)lur   E)dge detect   P)osterize   S)catter   T)int sepia
    W)eighted grayscale   X)treme contrast
    Q)uit
    :
    """
    commands = ["L)oad image",
                "B)lur   E)dge detect   P)osterize   S)catter   T)int sepia"
                ,"W)eighted grayscale   X)treme contrast"
                ,"Q)uit"]
    length_of_list = len(commands)
    for x in range (length_of_list):
        print(commands[x])



# A bit of code to demonstrate how to use get_image().




if __name__ == "__main__":
    ans = ""
    image_loaded = False
    # checks that Q is not inputted
    while (ans != "Q"):
        show_commands()
        ans = input(":")   
        
        # checks that a valid command was inputted
        if ans in  ["L", "Q", "B", "E", "P", "S", "T", "W", "X"]:  
            if (ans == "L"):
                img = get_image()
                image_loaded = True
            elif(ans != "L"):
                # checks that an image was already loaded
                if image_loaded != True:
                    print("No image loaded")
                else:
                    if(ans == "B"):
                        img = blur(img)
                    elif(ans == "E"):
                        threshold = input("Threshold? (0 - 256)")
                        img = detect_edges_better(img, int(threshold))
                    elif(ans == "P"):
                        img = posterize(img)
                    elif(ans == "S"):
                        img = scatter(img)
                    elif(ans == "T"):
                        img = sepia_tint(img)
                    elif(ans == "W"):
                        img = weighted_grayscale(img)
                    elif(ans == "X"):
                        img = extreme_contrast(img)
                        
        else:
            print ("No such command")
        if image_loaded == True and ans != "Q":
            show(img) 
        