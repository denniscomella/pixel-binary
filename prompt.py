import app
from settings import Global


def run():
    Global.prompt = True
    app.get_text()
    Global.prompt = False


if __name__ == "__main__":
    run()
