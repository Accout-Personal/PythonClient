from formpythonsimo3 import ui_test03
import sys
from PyQt5.QtWidgets import QApplication

from formpythonSimo import Ui_test01

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_home = ui_test03()
    vista_home.show()
    sys.exit(app.exec())