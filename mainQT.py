import sys
from PyQt5.QtWidgets import QApplication

from formpython import Ui_TestClass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_home = Ui_TestClass()
    vista_home.show()
    sys.exit(app.exec())