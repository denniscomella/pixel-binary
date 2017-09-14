import settings
from settings import Global
import decipher
import encode
import sys
from flask import Flask, send_file, request


# get user input
def get_text():
    text = input("Enter a command or '/help' for a list of commands: ")
    if text in ("/options", "/o"):
        settings.options()
        get_text()
    elif text in ("/decipher", "/d"):
        decipher.interpret()
    elif text in ("/encode", "/e"):
        text = input("Enter the ASCII text to be converted to a graphical bit string: ")
        encode.run(text)  # begin main program to encode text.
    elif text in ("/help", "/h"):
        sys.stdout.write("\033[94m")
        print("Type '/encode' or '/e' to convert ASCII text to an image.")
        print("Type '/decipher' or '/d' to convert a valid image to text.")
        print("Type '/options' or '/o' to change image output options.")
        print("Type '/help' or '/h' to see a list of commands.")
        sys.stdout.write("\033[0;0m")
        get_text()
    elif text == "/dir":
        from os import listdir
        files = listdir()
        for file in files:
            print(str(file))
    else:
        print("Not a valid command.")
        get_text()


app = Flask(__name__)

# this will be implemented on the web!
@app.route('/encode', methods=['POST'])
def text_to_img():
    try:
        text = request.form['submitText']
        Global.filename = request.form['fileName']

        encode.run(text)

        return send_file(Global.filename, as_attachment=True, cache_timeout=5)
    except Exception as ex:
        return str(ex) + ": There was an error."

if __name__ == "__main__":
    app.run()


# # #
# this is all that's needed to run the app normally with text prompt.
# get_text()
# # #



# end app
