# pixel-binary

## Synopsis

This app will allow anyone to surreptitious insert copyright information or other hidden messages into images of their choosing.

It will convert ASCII text to an image of black & white pixels representing 0's and 1's of binary code, and vice-versa.

## Installation

This requires the Pygame library and Flask. Make sure you have the latest version installed.

## API Implementation
The following code may be used on any web page running HTML5. It will allow encoding and deciphering of files with a number of options present.

`<form action="https://pixel-binary.herokuapp.com/encode" method="post">
<fieldset style="padding:20">
    <legend><h2>Encode text</h2></legend>
    Text to decode: <input type="text" name="submitText" placeholder="Text to decode"><br />
    File name: <input type="text" name="fileName" placeholder="File name">
    <div id="file type" style="display: inline-block">
        PNG: <input type="radio" name="fileType" value=".png" checked="checked">&nbsp;&nbsp;
        BMP: <input type="radio" name="fileType" value=".bmp">&nbsp;&nbsp;
        JPG: <input type="radio" name="fileType" value=".jpg">&nbsp;&nbsp;
    </div><br />
    Color 1: <input type="color" name="color0" value="#000000"> 
    Color 2: <input type="color" name="color1" value="#ffffff"><br />
    <input type="submit" value="&nbsp;Convert text!&nbsp;">
</fieldset
</form>

<fieldset style="padding:20">
    <legend><h2>Decipher image</h2></legend>
<form action="https://pixel-binary.herokuapp.com/decipher" method="post">
    Upload: <input type="file" name="imageUpload" value="Upload valid image."><br />
    <input type="checkbox" name="asFile" value="on" checked="checked"> Save as *.txt file<br />
    <input type="submit" value="&nbsp;Convert image!&nbsp;">
</fieldset>
</form>`

## Running the program

The app can be run from the command line (`python prompt.py`) or by using web forms through the API.

Through the prompt, you must first choose which type of operation you wish to perform: "/encode", or "/decipher".

### /encode

Encoding will prompt for a string of text and a filename. It will transform ASCII text to a binary string, then output an image with each binary bit turned into a pixel (black for "0", white for "1" by default). Each character will be encoded into 8 pixels in a 1px tall horizontal image.

PNG or BMP images are recommended, but the app can also support JPG with mixed results.

### /decipher

Deciphering will prompt for an image name to revert into ASCII text. It will attempt to automatically find two sufficiently different colors of pixels, and give the option to save the text as text document.

This should succeed most of the time (JPEG images have mixed results). If it fails, it will give the option to "flip" the binary digits to attempt a second interpretation if necessary.

### /options

The program also allows for certain parameters to be changed. Colors can be used as long as they are different enough from each other, otherwise it will revert to the default black & white scheme.

Eventually it should be able to handle multi-line images with minor tweaks, and locally save settings.

## Contributors

Program written by Dennis Comella / 2017
E-mail: dec168@gmail.com

Feel free to use this app and contribute your own improvements or suggestions. (I apologize for the code being super sloppy.) Please give credit to app creators.

## Documentation

Created using Python 3.6 and Pygame 1.9.3.

v1.00 - All the bugs worked out; API functions properly. Some code cleanup and additional options can still be done. 9/15/2017

v0.89 - API support imminent 9/11/2017

v0.8 - Initial release on 9/4/2017
All features are functional to create and decipher one-dimensional "binary" images. Other options in development.