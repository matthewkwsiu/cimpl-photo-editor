""" SYSC 1005 A Fall 2018.

Filters for a photo-editing application.
"""

from Cimpl import *
from random import *

def grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image

def weighted_grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a weighted grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = weighted_grayscale(image)
    >>> show(weighted_gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Sets the value of the RGB components as (29.9% red, 58.7% green
        # , and 11.4% blue)
        # makes a greyscale with a better brightness relative to the human
        # eye
        
        brightness = (r * 0.299 + g * 0.587 + b * 0.114)
                
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image

def extreme_contrast(image):
    ''' (Cimpl.Image) -> Cimpl.Image
    
    Returns a copy of the image, and maximizes the contrast of the light
    and dark pixels
    
    >>> image = load_image(choose_file())
    >>> new_image = extreme_contrast(image)
    >>> show(new_image)
    
    note: 8 possible different colors (black, r, g, b, rg, gb, br, white)
    '''
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        # Sets components of r, g, b to 0 or 255 based on initial color
        
        # Note: pretty sure theres a way to set this up as a list and 
        # for loop to reduce the number of lines
        if r < 128:
            r = 0
        else:
            r = 255
        if g < 128:
            g = 0
        else:
            g = 255
        if b < 128:
            b = 0
        else:
            b = 255    
        new_color = create_color(r, g, b)
        set_color(new_image, x, y, new_color)
    return new_image       
        
def sepia_tint(image):     
    """ (Cimpl.Image) -> Cimpl.Image 
 
    Return a copy of image in which the colours have been
    converted to sepia tones. 
    >>> image = load_image(choose_file())     
    >>> new_image = sepia_tint(image)     
    >>> show(new_image)     
    """ 
    
    new_image = weighted_grayscale(copy(image))
    for x, y, (r, g, b) in new_image:
        if r < 63:
            b *= 0.9
            r *= 1.1
        elif r < 191:
            b *= 0.85
            r *= 1.15
        else:
            b *= 0.93
            r *= 1.08
        new_color = create_color(r, g, b)
        set_color(new_image, x, y, new_color)
    return new_image

def _adjust_component(amount):     
    """ (int) -> int 
 
    Divide the range 0..255 into 4 equal-size quadrants,     
    and return the midpoint of the quadrant in which the     
    specified amount lies. 
 
    >>> _adjust_component(10)     
    31     
    >>> _adjust_component(85)    
    95     
    >>> _adjust_component(142)     
    159     
    >>> _adjust_component(230)     
    223     
    """
    # if elif else, will determine the quadrant the amount 
    # is in, and will return the midpoint of the quadrant
    if amount < 64:
        return 31
    elif amount < 128:
        return 95
    elif amount < 192:
        return 159
    else:
        return 223

def posterize(image):     
    """ (Cimpl.Image) -> Cimpl.Image 
 
    Return a "posterized" copy of image. 
 
    >>> image = load_image(choose_file())     
    >>> new_image = posterize(image)     
    >>> show(new_image)      
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        # this for loop changes the r, g, b parameters to the
        # midpoint of the 4 quadrant, using the 
        # _adjust_component(amount) function
        r = _adjust_component(r)
        g = _adjust_component(g)
        b = _adjust_component(b)
        new_color = create_color(r, g, b)
        set_color(new_image, x, y, new_color)
    return new_image

#Lab 6 Exercise 1
def detect_edges(image, threshold):
    """ 
    (Cimpl.Image, float) -> Cimpl.Image       
    Return a new image that contains a copy of the original image     
    that has been modified using edge detection. 
 
    >>> image = load_image(choose_file())     
    >>> filtered = detect_edges(image, 10.0)     
    >>> show(filtered)     
    """     
    new_image = copy(image)
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)
    
    for y in range(0, get_height(image)-1):
        for x in range(0, get_width(image)):
            r, g, b = get_color(image, x, y)
            brightness = (r + g + b)//3
            r2, g2, b2 = get_color(image, x, y+1)
            brightness2 = (r2 + g2 + b2)//3
            
            if (abs(brightness - brightness2) > threshold):
                set_color(new_image, x, y, black)
            else:
                set_color(new_image, x, y, white)
    
    return new_image           

def detect_edges_better(image, threshold):
    """ 
    (Cimpl.Image, float) -> Cimpl.Image       
    Return a new image that contains a copy of the original image     
    that has been modified using edge detection.        
    >>> image = load_image(choose_file())     
    >>> filtered = detect_edges_better(image, 10.0)     
    >>> show(filtered)     
    """
    new_image = copy(image)
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)
    
    for y in range(0, get_height(image) - 1):
        for x in range(0, get_width(image) - 1):
            r, g, b = get_color(image, x, y)
            brightness = (r + g + b)//3
            
            r_B, g_B, b_B = get_color(image, x, y+1)
            brightness_below = (r_B + g_B + b_B)//3
            
            r_R, g_R, b_R = get_color(image, x+1, y)
            brightness_right = (r_R + g_R + b_R)//3
            
            if (abs(brightness - brightness_below) > threshold) or (abs(brightness - brightness_right) > threshold):
                set_color(new_image, x, y, black)
            else:
                set_color(new_image, x, y, white)
    
    return new_image               

def blur(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of image.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(blurred)    
    """  
    target = copy(image)
        
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):

            '''
            Exercise 0
            
            Note: if you change the for loop so that it starts at 0 (top pixel), 
            there is an error, as when it tries to get the values of the colors 
            to the left of the first pixel, the pixel does not exist, so there 
            is an error
            
            if you do the top pixel, the pixel above does not exist, so there is
            a index outo range error
             
            if you do the leftmost pixel, the pixel to the left does not exist,
            so there is an index error
            
            if you do the right most pixel, the right pixel does not exist, so
            there is an error
            '''

            
            # Grab the pixel @ (x, y) and its eight neighbours

            red = []
            green = []
            blue = []
            
            # Here are the pixel indexes
            # 1 2 3
            # 4   5
            # 6 7 8
            
            
            for y_com in range(-1, 2):
                for x_com in range(-1, 2):
                    # I think I could make this one list, but that would make
                    # it more complicated later with adding red, green, blue
                    #print("{0} , {1}".format(y_com,x_com))
                    a, b, c = get_color(image, x + x_com, y + y_com)
                    red.append(a)
                    green.append(b)
                    blue.append(c)
                       
            new_red = 0
            new_green = 0
            new_blue = 0
            
            # this adds the color of the actual pixel to the list
            a, b, c = get_color(image, x, y)
            red.append(a)
            green.append(b)
            blue.append(c)
            
            for n in range(0, 9):
                new_red += red[n]
                new_green += green[n]
                new_blue += blue[n]
            
            new_red /= 9
            new_green /= 9
            new_blue /= 9
            
            new_color = create_color(new_red, new_green, new_blue)
            
            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)

    return target


def flip_vertical(image):
    """ (Cimpl.Image) -> Cimpl.Image
    Return an image that contains a copy of the original image
    after it has been flipped around an imaginary vertical line
    drawn through its midpoint.
    >>> image = load_image(choose_file())
    >>> filtered = flip_vertical(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    for y in range (get_height(image)):
        for x in range (get_width(image)):
            col = get_color(image, x, y)
            set_color(new_image, x, (get_height(image) - y - 1), col)
            
    return new_image

def flip_horizontal(image):
    """ (Cimpl.Image) -> Cimpl.Image
    Return an image that contains a copy of the original image
    after it has been flipped around an imaginary vertical line
    drawn through its midpoint.
    >>> image = load_image(choose_file())
    >>> filtered = flip_horizontal(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    for y in range (get_height(image)):
        for x in range (get_width(image)):
            col = get_color(image, x, y)
            set_color(new_image, (get_width(image) - x - 1), y, col)
            
    return new_image

def scatter(image):
    """ (Cimpl.image) -> Cimpl.image
    
    Return a new image that looks like a copy of an image in which the pixels
    have been randomly scattered. 
    
    >>> original = load_image(choose_file())
    >>> scattered = scatter(original)
    >>> show(scattered)    
    """
    # Create an image that is a copy of the original.
    
    new_image = copy(image)
    
    # Visit all the pixels in new_image.
    
    for x, y, (r, g, b) in image:
        
        # Generate the row and column coordinates of a random pixel
        # in the original image. Repeat this step if either coordinate
        # is out of bounds.
        
        row_and_column_are_in_bounds = False
        while not row_and_column_are_in_bounds:
            
            # Generate two random numbers between -10 and 10, inclusive.
            
            rand1 = randint(-10,10)
            rand2 = randint(-10,10)
            
            # Calculate the column and row coordinates of a
            # randomly-selected pixel in image.

            random_column = x + rand1
            random_row = y + rand2
            
            # Determine if the random coordinates are in bounds.

            if random_column in range (0,get_width(image)) and random_row in range (0,get_height(image)):
                row_and_column_are_in_bounds = True
                    
        # Get the color of the randomly-selected pixel.
        
        color = get_color(image, random_column, random_row)
        
        # Use that color to replace the color of the pixel we're visiting.
        
        set_color(new_image, x, y, color)
                    
    # Return the scattered image.
    return new_image