from flake8.main import application
import os


if __name__ == "__main__":
    app = application.Application()
    code_to_check = os.getcwd()
    app.run()
    app.exit()
