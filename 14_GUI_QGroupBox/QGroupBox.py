from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui

import sys

class Window(QWidget):
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 QGroupBox";
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

    # create layouts
    hbox = QHBoxLayout();
    vbox = QVBoxLayout();

    # create groupbox
    groupbox = QGroupBox("Select your favorite programming language");
    groupbox.setFont(QtGui.QFont("sanserif", 15));

    # create radio buttons
    rad1 = QRadioButton("Python");
    rad2 = QRadioButton("Java");
    rad3 = QRadioButton("C++");
    
    # add UI components to vbox
    vbox.addWidget(rad1);
    vbox.addWidget(rad2);
    vbox.addWidget(rad3);

    groupbox.setLayout(vbox)
    self.setLayout(hbox);
    
    # add UI components to layout
    hbox.addWidget(groupbox);
    


    self.show();





if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());