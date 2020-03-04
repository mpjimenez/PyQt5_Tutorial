from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui, QtCore


import sys

class Window(QWidget):
  def __init__(self):
    super().__init__()

    self.title = "PyQt QFrame";
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
    self.setStyleSheet('background-color:blue');

    # Create layout
    hbox = QHBoxLayout();

    # Create Buttons
    btn = QPushButton("Click Me");
    btn.setStyleSheet('color:white');
    btn.setStyleSheet('background-color:green');

    # Create Frame
    frame = QFrame();
    frame.setFrameShape(QFrame.StyledPanel);
    frame.setStyleSheet('background-color:red');
    frame.setLineWidth(0.6);

    # Add UI components to hbox
    hbox.addWidget(frame);
    hbox.addWidget(btn);
  
    self.setLayout(hbox);
    

    self.show();
    

  
  


if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());