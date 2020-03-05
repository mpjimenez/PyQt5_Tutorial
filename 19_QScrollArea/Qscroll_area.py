from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QVBoxLayout, QSlider, QLabel, QFormLayout, QGroupBox, QLabel, QScrollArea, QPushButton
from PyQt5 import QtGui


import sys

class Window(QWidget):
 
  def __init__(self, val):
    super().__init__()

    self.title = "PyQt5 QScroll Area";
    self.top = 300;
    self.left = 1100;
    self.width = 400;
    self.height = 250;
    self.iconName = "../_Icons/pic.jpg";
    self.numButtons = val

    self.InitWindow();


  def InitWindow(self):
    self.setWindowIcon(QtGui.QIcon(self.iconName));
    self.setWindowTitle(self.title);
    self.setGeometry(self.left, self.top, self.width, self.height);
    self.setStyleSheet('background-color:green');
    

    formLayout = QFormLayout();
    groupBox = QGroupBox("This is a Group Box");

    # Lists
    labelList = []
    buttonList= []

    for i in range(self.numButtons):
      labelList.append(QLabel("Label " + str(i + 1)));
      buttonList.append(QPushButton("Click Me"));
      formLayout.addRow(labelList[i], buttonList[i]);


    
    groupBox.setLayout(formLayout);
    scroll = QScrollArea();
    scroll.setWidget(groupBox);
    scroll.setWidgetResizable(True);
    scroll.setFixedHeight(400);

    layout = QVBoxLayout();
    layout.addWidget(scroll);
    self.setLayout(layout);
    self.show();
   

if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window(20);
  sys.exit(App.exec());