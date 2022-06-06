import sys
import numpy as np
import psycopg2
import sqlalchemy
from ui import manager_ui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
import login_main
from datetime import datetime, date


class Manager(manager_ui.Ui_manager):

    def __init__(self):
        super().__init__()
        self.acc = ''
        self.kt = ''
        self.total_money = 0
        self.bill = 0

        self.Manager = QtWidgets.QMainWindow()
        self.login_form = login_main.LoginUi(forward_form=0)
        self.setupUi(self.Manager)

        self.show_table(table_db='Doanhthu_ngay', table_qt=self.table_bill_ngay)
        self.show_table(table_db='Doanhthu_thang', table_qt=self.table_bill_thang)
        self.lbl_acc.setText('')
        self.show_table(table_db='Nhanvien', table_qt=self.table_acc)
        self.lbl_menu.setText('')
        self.show_table(table_db='Menu', table_qt=self.table_menu)
        self.comboBox.addItems(self.get_menu())

        self.ui_control()

    def show(self):
        qr = self.Manager.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.Manager.move(qr.topLeft())
        self.Manager.show()

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
        self.btn_add_2.clicked.connect(self.on_add_2)
        self.btn_upd_menu.clicked.connect(self.on_upd_menu)
        self.btn_add_acc.clicked.connect(self.on_add_acc)
        self.btn_logout.clicked.connect(self.on_logout)

    def on_b0(self):
        self.kt = "Table_0"
        self.txt_b.setText('Mang về')
        self.show_table(table_db=self.kt, table_qt=self.table_bill)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b1(self):
        self.kt = "Table_1"
        self.txt_b.setText('1')
        self.show_table(table_db=self.kt, table_qt=self.table_bill)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b2(self):
        self.kt = "Table_2"
        self.txt_b.setText('2')
        self.show_table(table_db=self.kt, table_qt=self.table_bill)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b3(self):
        self.kt = "Table_3"
        self.txt_b.setText('3')
        self.show_table(table_db=self.kt, table_qt=self.table_bill)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b4(self):
        self.kt = "Table_4"
        self.txt_b.setText('4')
        self.show_table(table_db=self.kt, table_qt=self.table_bill)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b5(self):
        self.kt = "Table_5"
        self.txt_b.setText('5')
        self.show_table(table_db=self.kt, table_qt=self.table_bill)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b6(self):
        self.kt = "Table_6"
        self.txt_b.setText('6')
        self.show_table(table_db=self.kt, table_qt=self.table_bill)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b7(self):
        self.kt = "Table_7"
        self.txt_b.setText('7')
        self.show_table(table_db=self.kt, table_qt=self.table_bill)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b8(self):
        self.kt = "Table_8"
        self.txt_b.setText('8')
        self.show_table(table_db=self.kt, table_qt=self.table_bill)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b9(self):
        self.kt = "Table_9"
        self.txt_b.setText('9')
        self.show_table(table_db=self.kt, table_qt=self.table_bill)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b10(self):
        self.kt = "Table_10"
        self.txt_b.setText('10')
        self.show_table(table_db=self.kt, table_qt=self.table_bill)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b11(self):
        self.kt = "Table_11"
        self.txt_b.setText('11')
        self.show_table(table_db=self.kt, table_qt=self.table_bill)
        self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_b12(self):
        self.kt = "Table_12"
        self.txt_b.setText('12')
        self.show_table(table_db=self.kt, table_qt=self.table_bill)
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

            self.show_table(table_db=self.kt, table_qt=self.table_bill)
            self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_xoa(self):
        if self.txt_b.text() != '':
            self.del_table(table_db=self.kt)
            self.show_table(table_db=self.kt, table_qt=self.table_bill)
            self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_upd(self):
        if self.txt_b.text() != '':
            self.update_bill()
            self.show_table(table_db=self.kt, table_qt=self.table_bill)
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

            self.show_table(table_db='Doanhthu_ngay', table_qt=self.table_bill_ngay)
            self.del_table(table_db=self.kt)
            self.show_table(table_db=self.kt, table_qt=self.table_bill)
            self.txt_money.setText(str(self.get_money_bill(self.kt)))

    def on_add_2(self):
        total_money = 0
        cur, connection = self.connect_db()

        cur.execute(f''' SELECT * FROM "Doanhthu_ngay" ''')
        data = cur.fetchall()
        for i in data:
            total_money = total_money + int(i[2])

        if total_money != 0:
            today = str(date.today())

            content = (today, str(total_money))
            cur, connection = self.connect_db()
            query = """ INSERT INTO "Doanhthu_thang" (date, total) VALUES (%s, %s) """
            cur.execute(query, content)

            connection.commit()
            count = cur.rowcount

            if connection:
                cur.close()
                connection.close()

            self.show_table(table_db='Doanhthu_thang', table_qt=self.table_bill_thang)
            self.del_table(table_db='Doanhthu_ngay')
            self.show_table(table_db='Doanhthu_ngay', table_qt=self.table_bill_ngay)

    def on_add_acc(self):
        self.lbl_acc.setText('')
        if self.txt_name.text() != '' and self.txt_phone.text() != '' \
                and self.txt_id.text() != '' and self.txt_pass.text() != '':

            kt = True
            accounts = self.login_form.get_account()
            for acc in accounts:
                if self.txt_id.text() == acc[2]:
                    kt = False
                    break

            if kt:
                content = (self.txt_name.text(), self.txt_phone.text(), self.txt_id.text(), self.txt_pass.text())
                cur, connection = self.connect_db()
                query = f""" INSERT INTO "Nhanvien" (name, phone, id, pass) VALUES (%s, %s, %s, %s) """
                cur.execute(query, content)

                connection.commit()
                count = cur.rowcount

                if connection:
                    cur.close()
                    connection.close()

                self.show_table(table_db='Nhanvien', table_qt=self.table_acc)
                self.txt_name.setText('')
                self.txt_phone.setText('')
                self.txt_id.setText('')
                self.txt_pass.setText('')
            else:
                self.lbl_acc.setText('ID đã tồn tại!')

        else:
            self.lbl_acc.setText('Vui lòng điền đủ thông tin!')

    def on_upd_menu(self):
        self.del_table(table_db='Menu')
        rowCount2 = self.table_menu.rowCount()
        for row in range(rowCount2):
            if self.table_menu.item(row, 0).text() == '':
                continue

            col_1 = self.table_menu.item(row, 0).text()
            col_2 = self.table_menu.item(row, 1).text()
            rowData = (col_1, col_2)
            cur, connection = self.connect_db()
            query = f""" INSERT INTO "Menu" (name, unit) VALUES (%s, %s) """
            cur.execute(query, rowData)
            connection.commit()
            count = cur.rowcount
            if connection:
                cur.close()
                connection.close()

        self.lbl_menu.setText('')
        if self.txt_drink.text() != '' and self.txt_unit.text() != '':
            kt = True
            rowCount1 = self.table_menu.rowCount()
            for row in range(rowCount1):
                if self.txt_drink.text() == self.table_menu.item(row, 0).text():
                    content = self.txt_unit.text()
                    self.table_menu.setItem(row, 1, QtWidgets.QTableWidgetItem(str(content)))

                    self.del_table(table_db='Menu')
                    rowCount2 = self.table_menu.rowCount()
                    for row in range(rowCount2):
                        if self.table_menu.item(row, 0).text() == '':
                            continue

                        col_1 = self.table_menu.item(row, 0).text()
                        col_2 = self.table_menu.item(row, 1).text()
                        rowData = (col_1, col_2)
                        cur, connection = self.connect_db()
                        query = f""" INSERT INTO "Menu" (name, unit) VALUES (%s, %s) """
                        cur.execute(query, rowData)
                        connection.commit()
                        count = cur.rowcount
                        if connection:
                            cur.close()
                            connection.close()

                    kt = False
                    break

            if kt:
                content = (self.txt_drink.text(), self.txt_unit.text())
                cur, connection = self.connect_db()
                query = f""" INSERT INTO "Menu" (name, unit) VALUES (%s, %s) """
                cur.execute(query, content)
                connection.commit()
                count = cur.rowcount
                if connection:
                    cur.close()
                    connection.close()

            self.txt_drink.setText('')
            self.txt_unit.setText('')

        else:
            self.lbl_menu.setText('Vui lòng điền đẩy đủ thông tin!')

        self.show_table(table_db='Menu', table_qt=self.table_menu)
        self.comboBox.addItems(self.get_menu())

    def on_logout(self):
        self.Manager.close()
        self.login_form.show()

    def connect_db(self):
        connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="CoffeeManager")
        cur = connection.cursor()
        return cur, connection

    def show_table(self, table_db, table_qt):
        table_qt.setRowCount(0)
        cur, connection = self.connect_db()

        cur.execute(f''' SELECT * FROM "{table_db}" ''')
        data = cur.fetchall()

        if data:
            table_qt.setRowCount(len(data)-1)
            table_qt.insertRow(len(data)-1)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    table_qt.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
                    column += 1

    def del_table(self, table_db):
        cur, connection = self.connect_db()
        query = f""" DELETE FROM "{table_db}" """
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
        self.del_table(table_db=self.kt)
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
    manager_window = Manager()
