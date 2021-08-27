from Dipendente.View.VistaAnagraficheDipendente import Ui_VisualizzaAnagDip
from Login.VistaLogin.formLogPython import Ui_VistaLog
from formpythonsimo3 import Ui_UIwindow
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_home = Ui_VistaLog()
    vista_home.show()
    sys.exit(app.exec())