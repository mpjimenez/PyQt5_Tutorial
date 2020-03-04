from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QHBoxLayout, QLabel, QVBoxLayout
from PyQt5 import QtGui
from PyQt5.QtCore import QRect

import sys 

class Window(QWidget):
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 QLine Edit";
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

    # create line edit
    self.lineEdit = QLineEdit(self);
    self.lineEdit.setFont(QtGui.QFont("sanserif", 15));
    self.lineEdit.returnPressed.connect(self.onPressed);
    
    # create label
    self.label = QLabel(self);
    self.label.setFont(QtGui.QFont("sanserif", 15));


    # add widgets to the layout
    hbox.addWidget(self.lineEdit);
    hbox.addWidget(self.label);


    self.setLayout(hbox);




    self.show();


  def onPressed(self):
    self.label.setText(self.lineEdit.text());







if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());