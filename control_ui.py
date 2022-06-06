import sys
from PyQt5 import QtWidgets
import login_main


class UIControl:
    def __init__(self):
        self.login_form = login_main.LoginUi(forward_form=0)

        self.show_login_form()

    def show_login_form(self):
        self.login_form.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui_control = UIControl()
    sys.exit(app.exec_())
