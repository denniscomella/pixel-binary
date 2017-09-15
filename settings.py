import sys

# starting variables
class Global:
    # abstract class to hold variables
    text_is_valid = False
    validFileName = False
    valid_exts = [".jpg", ".bmp", ".png", ".tga"]
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    zero_color = BLACK
    one_color = WHITE
    bitNum = 0
    img_width = 1
    max_width = None
    binary = ""  # gets populated through user.get_text()
    filename = ""
    form_fileType = None


# print("Type \"/options\" to change image parameters.")


# this should either accept R,G,B or an rgbArray of len==3
def options():
    changing_options = True
    command = input("OPTIONS: Type a command or '/exit' to exit settings menu.\n")
    while changing_options:
        if command == "/return" or command == "/save":
            changing_options = False
            print("Currently does not support saving options.")
        elif command in ("/exit", "/quit", "/x", "/q"):
            changing_options = False
            sys.stdout.write('\033[1m')
            print("Settings will used only for this session. Returning to main prompt.")
            sys.stdout.write("\033[0;0m")
        elif command == "/defaults":
            Global.zero_color = Global.BLACK
            Global.one_color = Global.WHITE
            Global.max_width = None
            print("Settings are now set to default.")
        elif command == "/0":
            set_zero(input("Set RGB value for '0' bit, separated by commas (default 0,0,0 for black): ").replace(" ", "").split(","))
        elif command == "/1":
            try:
                set_one(input("Set RGB value for '1' bit, separated by commas (default 255,255,255 for white): ").split(
                    ","))
            except:
                print("Could not interpret input.")
        elif command == "/w":
            try:
                width = int(input(
                    "Enter a max width for the image (enter \"0\" for no limit). Height will not be bound.: "))
                if width > 0:
                    Global.max_width = width
                elif width == 0:
                    Global.max_width = None
                else:
                    raise ValueError("Not a valid width.")
            except:
                print("Please enter a positive integer or 0.")
        elif command == "/help":
            help()
        elif command in ('hi', 'hello', 'hey'):
            print("Hi.")
        elif command == '/invert':
            one = Global.zero_color
            Global.zero_color = Global.one_color
            Global.one_color = one
            del one
        else:
            print("'" + command + "' is not a recognized command. Type '/help' for a list of commands.\n")
        if changing_options:  # did not request "quit"
            command = input("Enter a command: ")


def help():
    print("Please type one of the following commands: ")
    print("/0 - set a custom RGB value for the 'zero' bit.")
    print("/1 - set a custom RGB value for the 'one' bit.")
    print("/invert - swap the bit colors of the '1' and '0'.")
    print("/w - set a maximum width for the output image.")
    print("/defaults - return all settings to their initial values.")
    print("/exit - quit the settings menu without saving options.")
    print("/return - saves all settings and returns to main prompt.")


def set_zero(rgb):
    print(rgb)
    try:
        if len(rgb) == 3:
            for color in range(3):
                rgb[color] = int(rgb[color])
                if 0 <= rgb[color] <= 255:  # it is not properly turning values into integers within the list
                    continue
                else:
                    print("ValueError")
                    raise ValueError()
            Global.zero_color = rgb
        else:
            print("IndexError")
            raise IndexError()
        print("Color set to " + rgb)
    except:
        print("Could not interpret input.")


def set_one(rgb):
    Global.one_color = rgb

def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return [int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)]