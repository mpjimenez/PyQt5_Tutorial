from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtCore import QRect
from PyQt5 import QtGui, QtCore

import sys

class Window(QMainWindow):
  def __init__(self):
    super().__init__()

    title = "PyQt5 Push Button";
    left = 500;
    top = 200;
    width = 300;
    height = 250;
    iconName = "pic.jpg";

    self.setWindowTitle(title);
    self.setWindowIcon(QtGui.QIcon(iconName));
    self.setGeometry(left, top, width, height);

    self.UiComponents();

    self.show();

  def UiComponents(self):
    btn = QPushButton("Click Me", self);
    #btn.move(50, 50);

    # set geometry of the button
    btn.setGeometry(QRect(100, 100, 111, 50 )) # x pos, y pos, width, height

    btn.setIcon(QtGui.QIcon("pic.jpg")); # add icon to the left of button
    btn.setIconSize(QtCore.QSize(40, 40)); ''' Change the size of the icon --> import needed: from PyQt5 import QtCore '''

    btn.setToolTip("This is Click Me Button");

if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());
