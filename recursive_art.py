""" TODO: Put your header comment here """

import random
from PIL import Image
import math



def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)
        Randomly chooses one of a list of mathematical functions, and recursively composites them together into a nested list format
        until the required depth is reached.
        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
           """
    #["elementary function name here", argument 1 (optional), argument 2 (optional)]

    list_of_func = ["x", "y", "prod", "avg", "cos_pi", "sin_pi"] #
    if max_depth == 1:
        return random.choice(["x", "y"])
    else:
        random_func = random.choice(list_of_func)
        if random_func in ['prod', 'avg']:
            return [random_func,build_random_function(min_depth -1, max_depth -1), build_random_function(min_depth -1, max_depth -1)]
        else:
            return [random_func,build_random_function(min_depth -1, max_depth -1)]




    #def fib(iterate):
    #    if iterate == 0:
    #        return 0
    #    elif iterate ==1:
    #        return 1
    #    else:
    #        return fib(iterate -1 ) + fib(iterate-2)


def evaluate_random_function(f, x, y):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value
        Searches the list inputted recursively and evaluates each of the functions within the list, in proper order.

        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02

    """
    #base case  :
    # if len(f) == 1:
    #     if f[0]== 'x':
    #         return x
    #     elif f[0]== 'y':
    #         return y
    #lala
    if f[0] == 'x':
        return x #evaluate_random_function(f[1], x, y)
    elif f[0]== 'y':
        return y #float((evaluate_random_function(f[1], x, y)))
    elif f[0] == 'prod':
        return float((evaluate_random_function(f[1], x, y))*(evaluate_random_function(f[2], x, y)))
    elif f[0] ==  'avg':
        return  float(0.5*(float((evaluate_random_function(f[1], x, y)))+float((evaluate_random_function(f[2], x, y)))))
    elif f[0] == 'cos_pi':
        return float(math.cos(math.pi*(evaluate_random_function(f[1], x, y))))
    elif f[0] == 'sin_pi':
        return float(math.sin(math.pi*((evaluate_random_function(f[1], x, y)))))
    #elif f == 'negave':
    #    return float(-0.5*(float((evaluate_random_function(f[1], x, y)))+float((evaluate_random_function(f[2], x, y)))))
    #elif f== 'neg_sin_pi':
        #return float(-1*math.sin(math.pi*((evaluate_random_function(f[1], x, y)))))


def remap_interval(val,
                   input_interval_start,
                   input_interval_end,
                   output_interval_start,
                   output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval
        Turns pixel index into interval index

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
        >>> remap_interval(5, 0, 10, 1, 2)
        1.5
    """
    #floatifying
    value = float(val) #just to get us started
    input_interval_end = float(input_interval_end)
    input_interval_start = float (input_interval_start)
    output_interval_start = float(output_interval_start)
    output_interval_end = float(output_interval_end)
    #actual math
    input_range = input_interval_end - input_interval_start #2
    output_range = output_interval_end - output_interval_start #2
    #print(input_range, output_range)
    scaled_value =(value-input_interval_start)/input_range #5/2 2.5
    scaled_output_val = scaled_value*output_range # 5
    final_output= float(scaled_output_val + output_interval_start)
    return final_output


def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """ Generate test image with random pixels and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


def generate_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    #red_function = ["x"]
    #green_function = ["y"]
    #blue_function = ["x"]
    red_function = build_random_function(7, 9)
    green_function = build_random_function(7, 9)
    blue_function = build_random_function(7, 9)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(evaluate_random_function(red_function, x, y)),
                    color_map(evaluate_random_function(green_function, x, y)),
                    color_map(evaluate_random_function(blue_function, x, y))
                    )

    im.save(filename)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #       implement remap_interval and evaluate_random_function
    generate_art("myart2.png")
    #print build_random_function(2,7)
    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
    #test_image("noise.png")
