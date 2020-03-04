from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QPushButton, QHBoxLayout, QVBoxLayout, QSplitter, QLineEdit
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt


import sys

class Window(QWidget):
  def __init__(self):
    super().__init__()

    self.title = "PyQt QSplitter";
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
    #self.setStyleSheet('background-color:navy');

    hbox = QHBoxLayout();

    # Create frames
    left = QFrame();
    left.setFrameShape(QFrame.StyledPanel);

    bottom = QFrame();
    bottom.setFrameShape(QFrame.StyledPanel);

    # Create LineEdit
    lineEdit = QLineEdit();
    lineEdit.setStyleSheet("background-color:green");

    # Create Splitter: Horizontal or Vertical
    splitter1 = QSplitter(Qt.Horizontal);
    splitter1.setStyleSheet("background-color:red");
    splitter1.addWidget(left);
    splitter1.addWidget(lineEdit);
    splitter1.setSizes([200, 200]);

    splitter2 = QSplitter(Qt.Vertical);
    splitter2.setStyleSheet("background-color:yellow");
    splitter2.addWidget(splitter1);
    splitter2.addWidget(bottom);

    hbox.addWidget(splitter2);


    self.setLayout(hbox);
    self.show();
    

  
  


if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());