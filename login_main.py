import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from ui import login_ui, pic_login
import manager_main
import employee_main
import psycopg2


class LoginUi(login_ui.Ui_Login_main):
    def __init__(self, forward_form):
        super().__init__()

        self.forward_form = forward_form
        self.Login_form = QtWidgets.QMainWindow()
        self.setupUi(self.Login_form)

        self.ui_control()

    def show(self):
        qr = self.Login_form.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.Login_form.move(qr.topLeft())
        self.Login_form.show()

    def ui_control(self):
        self.txt_lbl.setText('')
        self.btn_cc.clicked.connect(self.on_cancel)
        self.btn_ok.clicked.connect(self.on_ok)
        self.btn_x.clicked.connect(self.on_x)

    def on_x(self):
        self.Login_form.close()

    def on_cancel(self):
        self.txt_user.setText('')
        self.txt_pw.setText('')

    def on_ok(self):
        kt = True
        id = self.txt_user.text()
        password = self.txt_pw.text()
        data = self.get_account()

        for account in data:
            if (id == 'admin') and (password == '1234'):
                self.forward_form = manager_main.Manager()
                self.forward_form.acc = 'admin'
                self.Login_form.close()
                self.forward_form.show()
                kt = False
                break

            elif (id == account[2]) and (password == account[3]):
                self.forward_form = employee_main.Employee()
                self.forward_form.acc = id
                self.forward_form.txt_name.setText(account[0])
                self.forward_form.txt_phone.setText(account[1])
                self.forward_form.txt_id.setText(account[2])
                self.forward_form.txt_pass.setText(account[3])
                self.Login_form.close()
                self.forward_form.show()
                kt = False
                break

        if kt:
            self.txt_lbl.setText('Login fail!')

    def get_account(self):
        connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="CoffeeManager")
        cur = connection.cursor()
        cur.execute(''' SELECT * FROM "Nhanvien" ''')
        data = cur.fetchall()

        return data


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui_control = LoginUi(forward_form=0)
    sys.exit(app.exec_())
