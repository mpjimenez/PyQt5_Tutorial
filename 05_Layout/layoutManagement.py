from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

import sys

class Window(QDialog):
  def __init__(self):
    super().__init__()

    self.title = "Layout Management";
    self.left = 500;
    self.top = 200;
    self.width = 400;
    self.height = 100;
    self.iconName = "pic.jpg";

    self.InitWindow();
    

   
  
  def InitWindow(self):
    self.setWindowTitle(self.title);
    self.setWindowIcon(QtGui.QIcon(self.iconName));
    self.setGeometry(self.left, self.top, self.width, self.height);

    self.createLayout();
    vbox = QVBoxLayout();
    vbox.addWidget(self.groupBox);
    self.setLayout(vbox);
    
    self.show();

  def createLayout(self):
    self.groupBox = QGroupBox("What is your favorite sport ?");
    hboxlayout = QHBoxLayout();

    btn1 = QPushButton("Soccer", self);
    btn1.setIcon(QtGui.QIcon("../_Icons/soccer.png")); # add icon to the left of button
    btn1.setIconSize(QtCore.QSize(40, 40)); # Change the size of the icon --> import needed: from PyQt5 import QtCore
    btn1.setMinimumHeight(40);
    hboxlayout.addWidget(btn1);

    btn2 = QPushButton("Basketball", self);
    btn2.setIcon(QtGui.QIcon("../_Icons/basketball.jpg")); # add icon to the left of button
    btn2.setIconSize(QtCore.QSize(40, 40)); # Change the size of the icon --> import needed: from PyQt5 import QtCore
    btn2.setMinimumHeight(40);
    hboxlayout.addWidget(btn2);

    btn3 = QPushButton("Baseball", self);
    btn3.setIcon(QtGui.QIcon("../_Icons/baseball.jpg")); # add icon to the left of button
    btn3.setIconSize(QtCore.QSize(40, 40)); # Change the size of the icon --> import needed: from PyQt5 import QtCore
    btn3.setMinimumHeight(40);
    hboxlayout.addWidget(btn3);

    self.groupBox.setLayout(hboxlayout);

if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());
