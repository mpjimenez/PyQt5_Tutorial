from PyQt5.QtWidgets import QApplication, QWidget, QSizeGrip, QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui, QtCore


import sys

class Window(QWidget):
  def __init__(self):
    super().__init__()

    self.title = "Frameless Window";
    self.top = 300;
    self.left = 1100;
    self.width = 400;
    self.height = 250;
    self.iconName = "../_Icons/pic.jpg";

    self.InitWindow();


  def InitWindow(self):
    self.setWindowIcon(QtGui.QIcon(self.iconName));
    self.setWindowTitle(self.title);
    self.setGeometry(self.left, self.top, self.width, self.height);

    flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint);
    self.setWindowFlags(flags);
    
    vbox = QVBoxLayout();
    sizegrip = QSizeGrip(self);

    vbox.addWidget(sizegrip);
    self.setLayout(vbox);
    
    

    self.show();





if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());