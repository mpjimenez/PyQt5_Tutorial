from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QHBoxLayout, QLabel, QVBoxLayout, QButtonGroup, QPushButton, QLabel
from PyQt5 import QtGui
from PyQt5 import QtCore

import sys 

class Window(QWidget):
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 QButton Group";
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
    self.buttongroup = QButtonGroup();
    self.buttongroup.buttonClicked[int].connect(self.on_button_clicked);

    # Create Label
    self.label = QLabel(self);
    self.label.setFont(QtGui.QFont("sanserif", 15));
    
    # Create the buttons
    btn1 = QPushButton("Python");
    btn1.setFont(QtGui.QFont("sanserif", 13));
    btn1.setIcon(QtGui.QIcon("../_Icons/python.png"));
    btn1.setIconSize(QtCore.QSize(40, 40));
   
    btn2 = QPushButton("Java");
    btn2.setFont(QtGui.QFont("sanserif", 13));
    btn2.setIcon(QtGui.QIcon("../_Icons/java.jpeg"));
    btn2.setIconSize(QtCore.QSize(40, 40));

    btn3 = QPushButton("C++");
    btn3.setFont(QtGui.QFont("sanserif", 13));
    btn3.setIcon(QtGui.QIcon("../_Icons/C_Plus_Plus.png"));
    btn3.setIconSize(QtCore.QSize(40, 40));

    # add UI components to the layout
    hbox.addWidget(btn1);
    hbox.addWidget(btn2);
    hbox.addWidget(btn3);
    hbox.addWidget(self.label)


    # add buttons to the buttonGroup
    self.buttongroup.addButton(btn1, 1);
    self.buttongroup.addButton(btn2, 2);
    self.buttongroup.addButton(btn3, 3);



    self.setLayout(hbox);
    self.show();

  def on_button_clicked(self, id):
    for button in self.buttongroup.buttons():
      if button is self.buttongroup.button(id):
        self.label.setText(button.text() + " was clicked!");
        print(id);






if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());