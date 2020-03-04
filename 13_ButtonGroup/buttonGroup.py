from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QHBoxLayout, QLabel, QVBoxLayout
from PyQt5 import QtGui
from PyQt5.QtCore import QRect

import sys 

class Window(QWidget):
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 QButton Group";
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

    self.show();





if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());