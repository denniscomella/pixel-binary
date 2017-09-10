"""
This module encodes text to an image.
"""

import pygame
from settings import Global


def run(text):
    Global.text_is_valid = False
    binary = Global.binary
    while not Global.text_is_valid:
        for char in text:
            bin_char = format(ord(char), 'b')
            if len(bin_char) > 8:
                print("Symbol (" + char + ") not defined. Each character may contain a maximum of 8 bits. \
                Please do not use any complex symbols.")
                break
                # Exception has happened. 'While' loop will restart!
            while len(bin_char) < 8:
                bin_char = "0" + bin_char
            binary += bin_char + ""
        else:  # follows the success of the for-loop
            Global.text_is_valid = True
            Global.binary = binary
            Global.img_width = len(Global.binary)
            print(Global.binary)
            print("Image width: " + str(Global.img_width))
            continue
        print("getText again.")
        binary = ""
        print(Global.text_is_valid)
        continue  # restarts the while loop
    save_path()
    save_image()


def save_path():
    # determine file name to save image
    while not Global.validFileName:
        # Global.filename = input("Enter a valid filename (*.png or *.bmp recommended; *.jpg and *.tga allowed): ")
        if Global.filename == "settings.png":
            print("File name is forbidden! Please choose a different file name.")
            continue
        if Global.filename == "":
            Global.filename = "image.png"
            print("Image will be saved as default: 'image.png'")
        for ext in Global.valid_exts:
            if Global.filename[-4:] == ext and len(Global.filename) >= 5:
                if Global.filename[-3:] == "jpg":
                    print("JPEG images may produce un-decipherable results due to compression. Proceed accordingly.")
                Global.validFileName = True
                break
        else:
            try:
                # print("\"" + Global.filename[Global.filename.index("."):] + "\" is not a valid file extension.")
                Global.filename = Global.filename + ".png"
            except ValueError:
                print("Please specify a proper file name (e.g. \"sample.png\")")


def save_image():
    # initiate pygame surface
    pygame.init()
    screen = pygame.Surface([Global.img_width, 1])

    # draw all the pixels... currently not working.
    if Global.zero_color != Global.BLACK:
        screen.fill(Global.zero_color)
    for bit in Global.binary:
        if bit == "1":
            x = Global.bitNum
            pygame.draw.line(screen, Global.one_color, [x, 0], [x, 0])  # draws a 1px "line" at [x,0] (0 is first row)
        Global.bitNum += 1

    pygame.image.save(screen, Global.filename)  # save(Surface, filename)
    pygame.quit()
