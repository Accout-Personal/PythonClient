from formpythonsimo3 import Ui_UIwindow
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_home = Ui_UIwindow()
    vista_home.show()
    sys.exit(app.exec())