import psycopg2
from ui import employee_ui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
import login_main
from datetime import datetime


class Employee(employee_ui.Ui_employee):
    def __init__(self):
        super().__init__()
        self.acc = ''
        self.kt = ''
        self.total_money = 0
        self.bill = 0

        self.Employee = QtWidgets.QMainWindow()
        self.login_form = login_main.LoginUi(forward_form=0)
        self.setupUi(self.Employee)

        self.comboBox.addItems(self.get_menu())

        self.ui_control()

    def show(self):
        qr = self.Employee.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.Employee.move(qr.topLeft())
        self.Employee.show()

    def ui_control(self):
        self.btn_b0.clicked.connect(self.on_b0)
        self.btn_b1.clicked.connect(self.on_b1)
        self.btn_b2.clicked.connect(self.on_b2)
        self.btn_b3.clicked.connect(self.on_b3)
        self.btn_b4.clicked.connect(self.on_b4)
        self.btn_b5.clicked.connect(self.on_b5)
        self.btn_b6.clicked.connect(self.on_b6)
        self.btn_b7.clicked.connect(self.on_b7)
        self.btn_b8.clicked.connect(self.on_b8)
        self.btn_b9.clicked.connect(self.on_b9)
        self.btn_b10.clicked.connect(self.on_b10)
        self.btn_b11.clicked.connect(self.on_b11)
        self.btn_b12.clicked.connect(self.on_b12)
        self.btn_add.clicked.connect(self.on_add)
        self.btn_xoa.clicked.connect(self.on_xoa)
        self.btn_upd.clicked.connect(self.on_upd)
        self.btn_tt.clicked.connect(self.on_tt)
        self.btn_logout.clicked.connect(self.on_logout)

    def on_b0(self):
        self.kt = "Table_0"
        self.txt_b.setText('Mang về')
        self.show_bill(self.kt)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b1(self):
        self.kt = "Table_1"
        self.txt_b.setText('1')
        self.show_bill(self.kt)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b2(self):
        self.kt = "Table_2"
        self.txt_b.setText('2')
        self.show_bill(self.kt)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b3(self):
        self.kt = "Table_3"
        self.txt_b.setText('3')
        self.show_bill(self.kt)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b4(self):
        self.kt = "Table_4"
        self.txt_b.setText('4')
        self.show_bill(self.kt)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b5(self):
        self.kt = "Table_5"
        self.txt_b.setText('5')
        self.show_bill(self.kt)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b6(self):
        self.kt = "Table_6"
        self.txt_b.setText('6')
        self.show_bill(self.kt)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b7(self):
        self.kt = "Table_7"
        self.txt_b.setText('7')
        self.show_bill(self.kt)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b8(self):
        self.kt = "Table_8"
        self.txt_b.setText('8')
        self.show_bill(self.kt)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b9(self):
        self.kt = "Table_9"
        self.txt_b.setText('9')
        self.show_bill(self.kt)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b10(self):
        self.kt = "Table_10"
        self.txt_b.setText('10')
        self.show_bill(self.kt)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b11(self):
        self.kt = "Table_11"
        self.txt_b.setText('11')
        self.show_bill(self.kt)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b12(self):
        self.kt = "Table_12"
        self.txt_b.setText('12')
        self.show_bill(self.kt)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_add(self):
        if self.txt_b.text() != '':
            amount = self.spinBox.text()
            mon = self.comboBox.currentText()
            if int(amount) > 0:
                kt = True
                rowCount = self.table_bill.rowCount()
                for row in range(rowCount):
                    if self.table_bill.item(row, 0).text() == mon:
                        content = int(self.table_bill.item(row, 1).text()) + int(amount)
                        self.table_bill.setItem(row, 1, QtWidgets.QTableWidgetItem(str(content)))
                        self.update_bill()
                        kt = False
                        break

                if kt:
                    cur, connection = self.connect_db()
                    cur.execute(f''' SELECT unit FROM "Menu" WHERE  name = %s ''', (mon, ))
                    result = cur.fetchone()
                    for don_gia in result:
                        add_content = (mon, int(amount), don_gia, '')

                    self.insert_bill(name_table=self.kt, content=add_content)

            self.show_bill(name_table=self.kt)
            self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_xoa(self):
        if self.txt_b.text() != '':
            self.del_bill(name_table=self.kt)
            self.show_bill(name_table=self.kt)
            self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_upd(self):
        if self.txt_b.text() != '':
            self.update_bill()
            self.show_bill(self.kt)
            self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_tt(self):
        if self.txt_b.text() != '' and self.txt_money.text() != '0':
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            total_bill = self.txt_money.text()
            content = (self.acc, current_time, total_bill)

            cur, connection = self.connect_db()
            query = """ INSERT INTO "Doanhthu_ngay" (account, time, bill) VALUES (%s, %s, %s) """
            cur.execute(query, content)

            connection.commit()
            count = cur.rowcount

            if connection:
                cur.close()
                connection.close()

            self.del_bill(name_table=self.kt)
            self.show_bill(name_table=self.kt)
            self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_logout(self):
        self.Employee.close()
        self.login_form.show()

    def connect_db(self):
        connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="CoffeeManager")
        cur = connection.cursor()
        return cur, connection

    def show_bill(self, name_table):
        self.table_bill.setRowCount(0)
        cur, connection = self.connect_db()

        cur.execute(f''' SELECT * FROM "{name_table}" ''')
        data = cur.fetchall()

        if data:
            self.table_bill.setRowCount(len(data)-1)
            self.table_bill.insertRow(len(data)-1)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.table_bill.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
                    column += 1

    def del_bill(self, name_table):
        cur, connection = self.connect_db()
        query = f""" DELETE FROM "{name_table}" """
        cur.execute(query)

        connection.commit()
        count = cur.rowcount

        if connection:
            cur.close()
            connection.close()

    def insert_bill(self, name_table, content):
        cur, connection = self.connect_db()
        query = f""" INSERT INTO "{name_table}" (drink, amount, unit, note) VALUES (%s, %s, %s, %s) """
        cur.execute(query, content)

        connection.commit()
        count = cur.rowcount

        if connection:
            cur.close()
            connection.close()

    def update_bill(self):
        self.del_bill(self.kt)
        rowCount = self.table_bill.rowCount()

        for row in range(rowCount):
            if self.table_bill.item(row, 0).text() == '':
                continue

            col_1 = self.table_bill.item(row, 0).text()
            col_2 = int(self.table_bill.item(row, 1).text())
            col_3 = int(self.table_bill.item(row, 2).text())
            col_4 = self.table_bill.item(row, 3).text()
            rowData = (col_1, col_2, col_3, col_4)
            self.insert_bill(name_table=self.kt, content=rowData)

    def get_menu(self):
        cur, connection = self.connect_db()

        cur.execute(''' SELECT name FROM "Menu" ''')
        data = cur.fetchall()
        list_menu = []
        if data:
            for i in data:
                list_menu.append(i[0])

        return list_menu

    def get_money_bill(self, name_table):
        self.bill = 0
        cur, connection = self.connect_db()

        cur.execute(f''' SELECT amount, unit FROM "{name_table}" ''')
        data = cur.fetchall()
        for i in data:
            self.bill = self.bill + i[0] * i[1]

        return self.bill


if __name__ == '__main__':
    epl_window = Employee()
