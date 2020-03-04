from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout, QLabel, QVBoxLayout
from PyQt5 import QtGui

import sys 

class Window(QWidget):
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 WhatIsThis Class";
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

    hbox = QHBoxLayout();


    # create label
    label = QLabel("Focus and Press SHIFT + F1");
    hbox.addWidget(label); # add btn to hbox layout

    # create button
    btn = QPushButton("Click Me", self);
    btn.setWhatsThis("This is a button that you can click!");
    hbox.addWidget(btn); # add btn to the hbox layout

    # set the layout to hbox
    self.setLayout(hbox);

    self.show();


if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());