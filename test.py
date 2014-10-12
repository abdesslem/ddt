from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
 
def main(args) :
         app=QApplication(args)
         button=QPushButton("Hello World !", None)
         button.show()
         app.connect(app,SIGNAL("lastWindowClosed()"),app,SLOT("quit()"))
         app.connect(button, SIGNAL("clicked()"),app,SLOT("quit()"))
         app.exec_()
if __name__ == "__main__" :
   main(sys.argv)
