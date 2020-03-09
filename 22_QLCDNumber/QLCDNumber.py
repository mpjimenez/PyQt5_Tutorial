from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLCDNumber
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from random import randint


import sys

class Window(QWidget):
 
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 QLCDNumber";
    self.top = 300;
    self.left = 1100;
    self.width = 400;
    self.height = 250;
    self.iconName = "../_Icons/pic.jpg";
    self.setWindowIcon(QtGui.QIcon(self.iconName));
    self.setWindowTitle(self.title);
    self.setGeometry(self.left, self.top, self.width, self.height);

    self.initUI();
    self.show();



  def initUI(self):
    vbox = QVBoxLayout();

    # Create LCDNumber
    self.lcd = QLCDNumber();
    self.lcd.setStyleSheet("background-color:green");

    # create button
    self.button = QPushButton("Random Number Generator");
    self.button.setStyleSheet('background-color:yellow');
    self.button.clicked.connect(self.LCDHandler);

    # add UI components to layout
    vbox.addWidget(self.lcd);
    vbox.addWidget(self.button)

    # set vboxlayout to window
    self.setLayout(vbox);

  def LCDHandler(self):
    random = randint(1, 200);
    self.lcd.display(random);

if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());