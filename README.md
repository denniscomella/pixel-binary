#pixel-binary

##Implementation

This app will allow anyone to surreptitious insert copyright information or other hidden messages into images of their choosing.

##Installation

This requires the Pygame library. Make sure you have the latest version installed.

Run app.py to begin.

##Running the program

You must first choose which type of operation you wish to perform: "/encode", or "/decipher".

###/encode

Encoding will prompt for a string of text and a filename. It will transform ASCII text to a binary string, then output an image with each binary bit turned into a pixel (black for "0", white for "1" by default). Each character will be encoded into 8 pixels in a 1px tall horizontal image.

PNG or BMP images are recommended, but the app can also support JPG with mixed results.

###/decipher

Deciphering will prompt for an image name to revert into ASCII text. It will attempt to automatically find two sufficiently different colors of pixels, and give the option to save the text as text document.

This should succeed most of the time (JPEG images have mixed results). If it fails, it will give the option to "flip" the binary digits to attempt a second interpretation if necessary.

###/options

The program also allows for certain parameters to be changed.

Eventually it should be able to handle multi-line images with minor tweaks, and locally save settings.

##Copyright

Program written by Dennis Comella. © 2017
E-mail: dec168@gmail.com

Feel free to use this app and contribute your own improvements or suggestions. Please give credit.

##Documentation

Created using Python 3.6 and Pygame 1.9.3.

v0.8 - Initial release on 9/4/2017
All features are functional to create and decipher one-dimensional "binary" images. Other options in development.