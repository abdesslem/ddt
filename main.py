import sys
from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *
from mainGUI import Ui_Dialog

class MyForm(QtGui.QMainWindow):
    def  mymethod(self):
         self.ui.lineEdit.setText('Hello World')
         #self.textFieldExample.clear() 
         self.ui.progressBar.setProperty("value", 100)


    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QObject.connect(self.ui.toolButton_3,SIGNAL("released()"),self.mymethod) # signal/slot connection
        QObject.connect(self.ui.toolButton_2,SIGNAL("released()"),self.mymethod)
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
