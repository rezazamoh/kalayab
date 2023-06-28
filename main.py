import sys
import resorses.res
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
searched_phrase = ''

class main_screen(QMainWindow):
    def __init__(self):
        super(main_screen,self).__init__()
        loadUi("main.ui",self)
        self.search_button.clicked.connect(self.search_func)
    
    def search_func(self):
        if len(self.search_input.text())>3:
            widget.setCurrentIndex(widget.currentIndex()+1)
            global searched_phrase
            searched_phrase = self.search_input.text()
            print(searched_phrase)
        else: 
            self.error_dialog = QtWidgets.QErrorMessage()
            self.error_dialog.showMessage('لطفا حداقل ۴ حرف وارد کنید!')
            
class result_screen(QMainWindow):
    def __init__(self):
        super(result_screen,self).__init__()
        loadUi("results.ui",self)
        self.search_input.setText(searched_phrase)
        self.search_button.clicked.connect(self.search_func)
        self.back_button.clicked.connect(self.back_func)

    def back_func(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

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
result_window = result_screen()
widget.addWidget(main_window)
widget.addWidget(result_window)
widget.setFixedHeight(625)
widget.setFixedWidth(890)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting...")