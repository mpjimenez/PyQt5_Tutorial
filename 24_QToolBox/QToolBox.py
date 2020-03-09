from PyQt5.QtWidgets import QApplication, QWidget, QToolBox, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from random import randint


import sys

class Window(QWidget):
 
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 QToolBox";
    self.top = 300;
    self.left = 1100;
    self.width = 400;
    self.height = 250;
    self.iconName = "../_Icons/pic.jpg";
    self.setWindowIcon(QtGui.QIcon(self.iconName));
    self.setWindowTitle(self.title);
    self.setGeometry(self.left, self.top, self.width, self.height);
    self.setStyleSheet('background-color:yellow');

    self.initUI();
    self.show();



  def initUI(self):
    # create layout
    vbox = QVBoxLayout();

    # create toolbox
    toolbox = QToolBox();
    toolbox.setStyleSheet('background-color:green');

    # create Label
    label1 = QLabel();
    label2 = QLabel();
    label3 = QLabel();
    toolbox.addItem(label1, "Python");
    toolbox.addItem(label2, "Java");
    toolbox.addItem(label3, "C++");


    # Add UI components to layout
    vbox.addWidget(toolbox);
    self.setLayout(vbox);

  
    

   

if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());