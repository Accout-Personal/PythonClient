import sys
from PyQt5.QtWidgets import QApplication

#from formleo import Ui_UIwindow
from formleo import Ui_UIwindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_home = Ui_UIwindow()
    vista_home.show()
    sys.exit(app.exec())

#
#from PyQt5.QtWidgets import QWidget
#class Ui_UIwindow(QWidget):
#    def __init__(self, parent=None):
#        super(Ui_UIwindow, self).__init__(parent)
#        UIwindow = self