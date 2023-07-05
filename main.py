import sys
import resorses.res
import digikala
import login
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication , QListWidgetItem ,QTableWidgetItem ,QTableWidget
searched_phrase = ''
result_list = []
selected_item = 'None'
account = 'Guest'

class main_screen(QMainWindow):
    def __init__(self):
        super(main_screen,self).__init__()
        loadUi("main.ui",self)
        self.search_button.clicked.connect(self.search_func)
        self.login_button.clicked.connect(self.login_func)
        self.laptop_label.mousePressEvent = self.goto_lap
        self.mobile_label.mousePressEvent = self.goto_mob
        self.cooking_label.mousePressEvent = self.goto_cook
        self.clothing_label.mousePressEvent = self.goto_cloth
        self.digital_label.mousePressEvent = self.goto_digi
        self.loved_label.mousePressEvent = self.goto_loved
        self.logout.triggered.connect(self.logout_func)

    def search_func(self):
        if len(self.search_input.text())>3:
            global searched_phrase; global result_list
            searched_phrase = self.search_input.text()
            result_list = digikala.scan(searched_phrase)
            result_window = result_screen()
            widget.addWidget(result_window)
            widget.setCurrentIndex(widget.currentIndex()+1)
        
        else: 
            self.error_dialog = QtWidgets.QErrorMessage()
            self.error_dialog.showMessage('لطفا حداقل ۴ حرف وارد کنید!')
    
    def login_func(self):
        login_window = login_screen()
        widget.addWidget(login_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def logout_func(self):
        global account
        if account != 'Guest':
            account = 'Guest'
            self.account_menu.setTitle(account)
            self.logged_out = QtWidgets.QErrorMessage()
            self.logged_out.showMessage('از حساب خود با موفقیت خارج شدید')
        else:
            self.notlogged = QtWidgets.QErrorMessage()
            self.notlogged.showMessage('داخل حسابی نیستید که بخواهید از آن خارج شوید!')

    def goto_loved(self,event):
        global account
        if account == 'Guest':
            self.notlogged = QtWidgets.QErrorMessage()
            self.notlogged.showMessage('داخل حسابی نیستید که بخواهید علاقه مندی هایتان را ببینید!')
    
    def goto_lap(self,event):
            global result_list
            result_list = digikala.scan('لپ تاپ')
            result_window = result_screen()
            widget.addWidget(result_window)
            widget.setCurrentIndex(widget.currentIndex()+1)           

    def goto_mob(self,event):
            global result_list
            result_list = digikala.scan('گوشی موبایل')
            result_window = result_screen()
            widget.addWidget(result_window)
            widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_cook(self,event):
            global result_list
            result_list = digikala.scan('لوازم آشپرخانه')
            result_window = result_screen()
            widget.addWidget(result_window)
            widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_cloth(self,event):
            global result_list
            result_list = digikala.scan('لباس و پوشاک')
            result_window = result_screen()
            widget.addWidget(result_window)
            widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_digi(self,event):
            global result_list
            result_list = digikala.scan('لوازم دیجیتال')
            result_window = result_screen()
            widget.addWidget(result_window)
            widget.setCurrentIndex(widget.currentIndex()+1)

class login_screen(QMainWindow):
    def __init__(self):
        super(login_screen,self).__init__()
        loadUi("login.ui",self)
        self.register_rb.setChecked(True)
        self.done_button.clicked.connect(self.log_reg)
        self.back_button.clicked.connect(self.back_to_main)

    def back_to_main(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.removeWidget(self)

    def log_reg(self):
        
        if self.register_rb.isChecked():
            respond = login.register(self.user_input.text(),self.pass_input.text())
        if self.login_rb.isChecked():
            respond = login.login(self.user_input.text(),self.pass_input.text())
        if respond.isdigit():
            global account
            account = self.user_input.text()
            widget.setCurrentIndex(widget.currentIndex()-1)
            widget.removeWidget(self)
            main_window.account_menu.setTitle(account)
        else:
            self.error_label.setText(respond)
            
class result_screen(QMainWindow):
    def __init__(self):
        super(result_screen,self).__init__()
        loadUi("results.ui",self)
        for i in result_list:
            item = QListWidgetItem(i)
            self.listWidget.addItem(item)
        self.search_input.setText(searched_phrase)
        self.search_button.clicked.connect(self.search_func)
        self.back_button.clicked.connect(self.back_func)
        self.select_button.clicked.connect(self.goto_goodpage)

    def goto_goodpage(self):
        global selected_item ; global result_list
        selected = self.listWidget.currentRow()
        if selected != -1:
            selected_item = (list(result_list.keys())[selected])
            good_window = good_screen()
            widget.addWidget(good_window)
            widget.setCurrentIndex(widget.currentIndex()+1)
                    
    
    def back_func(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.removeWidget(self)

    def search_func(self):
        if len(self.search_input.text())>3:
            global searched_phrase
            searched_phrase = self.search_input.text()
        else: 
            self.error_dialog = QtWidgets.QErrorMessage()
            self.error_dialog.showMessage('لطفا حداقل ۴ حرف وارد کنید!')

class good_screen(QMainWindow):
    def __init__(self):
        super(good_screen,self).__init__()
        loadUi("kala.ui",self)
        global selected_item ; global result_list
        info = digikala.itemscanner(result_list[selected_item][1])
        self.name_label.setText(selected_item)
        self.back_to_results.clicked.connect(self.back_button1)
        #loading image
        self.image_label.setStyleSheet("background-image : url(good.png);border : 2px solid blue")
        
        #loadind info table 
        for i in info:
            rowPosition = self.details_table.rowCount()
            if type(self.details_table) == QTableWidget:
                self.details_table.insertRow(rowPosition)
            self.details_table.setItem(rowPosition , 0, QTableWidgetItem(i.text))
            self.details_table.setItem(rowPosition , 1, QTableWidgetItem(info[i].text))
            
    def back_button1(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.removeWidget(self)         

app=QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
main_window = main_screen()
widget.addWidget(main_window)
widget.setFixedHeight(625)
widget.setFixedWidth(890)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting...")