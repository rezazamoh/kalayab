import sys
import resorses.res
import digikala
from PyQt5.uic import loadUi
from PyQt5.QtCore import QThread
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication , QListWidgetItem
searched_phrase = ''
result_list = []

class main_screen(QMainWindow):
    def __init__(self):
        super(main_screen,self).__init__()
        loadUi("main.ui",self)
        self.search_button.clicked.connect(self.search_func)
        self.laptop_label.mousePressEvent = self.goto_lap

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

    def goto_lap(self,event):
            global result_list
            result_list = digikala.scan('گوشی موبایل')
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
            result_list = digikala.scan('گوشی موبایل')
            result_window = result_screen()
            widget.addWidget(result_window)
            widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_cloth(self,event):
            global result_list
            result_list = digikala.scan('گوشی موبایل')
            result_window = result_screen()
            widget.addWidget(result_window)
            widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_digi(self,event):
            global result_list
            result_list = digikala.scan('گوشی موبایل')
            result_window = result_screen()
            widget.addWidget(result_window)
            widget.setCurrentIndex(widget.currentIndex()+1)

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

    def back_func(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.removeWidget(self)

    def search_func(self):
        if len(self.search_input.text())>3:
            global searched_phrase
            searched_phrase = self.search_input.text()
            print(searched_phrase)
        else: 
            self.error_dialog = QtWidgets.QErrorMessage()
            self.error_dialog.showMessage('لطفا حداقل ۴ حرف وارد کنید!')

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