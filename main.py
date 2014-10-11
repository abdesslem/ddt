#from PyQt4 import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.Qt import *
from mainGUI import Ui_Dialog
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    f = setupUi()
    f.show()
    app.setMainWidget(f)
    app.exec_loop()
