import sys
from PyQt5.QtWidgets import QApplication

from Login.VistaLogin.formLogPython import Ui_VistaLog

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_home = Ui_VistaLog()
    vista_home.show()
    sys.exit(app.exec())


