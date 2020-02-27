from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QGridLayout, QVBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

import sys

class Window(QDialog):
  def __init__(self):
    super().__init__()
    self.title = "PyQt5 Grid Layout";
    self.left = 500;
    self.top = 200;
    self.width = 400;
    self.height = 100;
    self.iconName = "pic.jpg";

    self.InitWindow();

    self.InitWindow();

  def InitWindow(self):
    self.setWindowTitle(self.title);
    self.setWindowIcon(QtGui.QIcon(self.iconName));
    self.setGeometry(self.left, self.top, self.width, self.height);
  
    self.CreateLayout();
    vbox = QVBoxLayout();
    vbox.addWidget(self.groupBox);

    self.setLayout(vbox);
    
    self.show()


  def CreateLayout(self):
    self.groupBox = QGroupBox("What is your Favorite Programming Language ?");
    gridLayout = QGridLayout();

    btn1 = QPushButton("Python", self);
    btn1.setIcon(QtGui.QIcon("../_Icons/python.jpg")); # add icon to the left of button
    btn1.setIconSize(QtCore.QSize(40, 40)); # Change the size of the icon --> import needed: from PyQt5 import QtCore
    btn1.setMinimumHeight(40);
    gridLayout.addWidget(btn1, 0, 0);

    btn2 = QPushButton("C++", self);
    btn2.setIcon(QtGui.QIcon("../_Icons/C_Plus_Plus.png")); # add icon to the left of button
    btn2.setIconSize(QtCore.QSize(40, 40)); # Change the size of the icon --> import needed: from PyQt5 import QtCore
    btn2.setMinimumHeight(40);
    gridLayout.addWidget(btn2, 0, 1); # row, column

    btn3 = QPushButton("Fortran", self);
    btn3.setIcon(QtGui.QIcon("../_Icons/fortran.png")); # add icon to the left of button
    btn3.setIconSize(QtCore.QSize(40, 40)); # Change the size of the icon --> import needed: from PyQt5 import QtCore
    btn3.setMinimumHeight(40);
    gridLayout.addWidget(btn3, 1, 0); # row, column

    btn4 = QPushButton("C#", self);
    btn4.setIcon(QtGui.QIcon("../_Icons/c_sharp.jpg")); # add icon to the left of button
    btn4.setIconSize(QtCore.QSize(40, 40)); # Change the size of the icon --> import needed: from PyQt5 import QtCore
    btn4.setMinimumHeight(40);
    gridLayout.addWidget(btn4, 1, 1); # row, column

    self.groupBox.setLayout(gridLayout);




if __name__=="__main__":
  App = QApplication(sys.argv);
  window = Window();
  sys.exit(App.exec());

