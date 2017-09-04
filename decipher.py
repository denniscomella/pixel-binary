"""
This module decodes an image into readable text.
"""

import pygame
from re import match


def get_file():
    print("This feature works best with images of two distinct colors.")
    print("It will only work for characters of 8 bits each.")
    filename = input("Enter the name of the file you wish to decipher: ")
    file = pygame.image.load(filename)
    return file


def interpret():
    file = get_file()
    pxarray = pygame.PixelArray(file)
    print(pxarray)
    print(pxarray[0, 0])
    rgb_array = [[] for x in range(len(pxarray))]  # create blank 2d array
    print("len(pxarray): " + str(len(pxarray)))
    for i in range(len(pxarray)):
        hexn = pxarray[i, 0]  # pxarray is 2D so it must have a second argument [x, y]
        rgb_array[i] = []  # change 0xFFFFFF == 16777215 (hex) to [255, 255, 255]
        while hexn > 0:
            remainder = hexn % 256
            rgb_array[i].insert(0, remainder)
            hexn = int((hexn - remainder) / 256)
        if len(rgb_array[i]) > 3:
            print("PixelArray presented illicit data.")
            break
        else:
            while len(rgb_array[i]) < 3:
                rgb_array[i].insert(0, 0)
    first_color = [0, 0, 0]
    second_color = [0, 0, 0]
    for i in range(len(rgb_array)):  # color test; should not iterate more than a few times
        for j in range(len(rgb_array[i])):
            if i + 1 > len(rgb_array):
                print("blah error")
                break
            if abs(rgb_array[i][j] - rgb_array[i + 1][j]) > 128:  # found two different colors
                first_color = rgb_array[i]
                second_color = rgb_array[i + 1]  # this only looks at the first distinctly different adjacent colors
                break  # this will not always work when using high JPEG compression!!
        if first_color != second_color:
            print(str(first_color) + " " + str(second_color))
            break
    zero_one_string = ""
    one_zero_string = ""
    for pixel in rgb_array:
        try_first = False
        if pixel == first_color:
            zero_one_string += "1"
            one_zero_string += "0"
            continue
        elif pixel == second_color:
            zero_one_string += "0"
            one_zero_string += "1"
            continue
        # if code runs here there are more than two distinct colors to be interpreted, so find closest one
        for j in range(len(pixel)):
            # print("j: " + str(pixel) + " " + str(j))
            if abs(pixel[j] - first_color[j]) < 128:
                # color seems to be similar so far...
                # must be true for each R,G,B in the color to be considered true.
                try_first = True
                continue
            else:
                try_first = False
                break  # colors are too different; finish checking colors
        if try_first:
            # determined to be first color!
            zero_one_string += "1"
            one_zero_string += "0"  # the second string here could be iterated later to improve processing efficiency
        elif not try_first:
            # must be the second color
            one_zero_string += "1"
            zero_one_string += "0"
    char_str_2 = ""
    char_str_1 = ""
    bin1 = one_zero_string  # record binary before making changes to string (use for logs during save)
    bin2 = zero_one_string
    while len(one_zero_string) >= 8:
        # int(number, 2) to convert binary to decimal
        # chr(i) to turn number into character (reverse of "ord()")
        char_str_1 += chr(int(one_zero_string[0:8], 2))
        char_str_2 += chr(int(zero_one_string[0:8], 2))
        one_zero_string = one_zero_string[8:]
        zero_one_string = zero_one_string[8:]
    print("First possible string.")
    print(char_str_1)
    second = False
    if match('^[\w\-+*#_$©]+', char_str_1) is None:
        pr_second(char_str_2)
        second = True
    while not second:
        worked = check_yes_no("Did this decode readable text? (y/n): ")
        if not worked:
            pr_second(char_str_2)
            second = True
        elif worked:
            break
        else:  # this should never run due to redundancy in check_yes_no() method
            print("Please respond accordingly.")
            # loop back to start of "while"
            pass
    saved = False
    while not saved:
        save_it = check_yes_no("Would you like to save this text to a file? (y/n): ")
        if save_it:
            if second:
                new_char_str = char_str_1 + "\nBinary: " + bin1 + "\n\n" + char_str_2 + "\nBinary: " + bin2
            else:
                new_char_str = char_str_1 + "\nBinary: " + bin1
            print("This will overwrite any existing *.txt file. This cannot be undone.")
            try:
                file_name = input("Please enter a file name (will be saved as *.txt): ")
                save_txt(file_name, new_char_str)
            except UnicodeEncodeError:
                try:
                    file = open(file_name + ".txt")
                    file.close()
                except:
                    print("File could not be closed...")
                    pass

                if second:
                    new_char_str = char_str_2 + "\nBinary: " + bin2
                    try:
                        save_txt(file_name, new_char_str)
                        break
                    except:
                        pass
                import sys
                sys.stdout.write("\033[1;31m")
                print("There was an error encoding. Strings returned undefined Unicode characters.")
                sys.stdout.write("\033[0;0m")
            saved = True
        elif not save_it:
            break


def pr_second(char_str_2):
    print("Second possible string (binary reversed).")
    print(char_str_2)
    pass


def check_yes_no(message):
    user_input = input(message)
    if user_input in ("y", "Y", "yes", "Yes", "YES"):
        return True
    elif user_input in ("n", "N", "no", "No", "NO"):
        return False
    else:
        print("'" + user_input + "' is not a valid response.")
        check_yes_no(message)


def save_txt(file_name, text_string):
    if file_name[-4:] == ".txt" and len(file_name) >= 5:
        file_name = file_name[:-4]
    file = open(file_name + ".txt", "w")
    file.write(text_string)
    file.close()
    print("File saved.")
    pass


############################################

if __name__ == "__main__":
    interpret()
