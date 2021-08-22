import sys
from PyQt5.QtWidgets import QApplication

#from formleo import Ui_UIwindow
from formpython import Ui_UIwindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_home = Ui_UIwindow()
    vista_home.show()
    sys.exit(app.exec())