from PyQt5.QtWidgets import QApplication, QDialog, QGroupBox, QVBoxLayout, QHBoxLayout, QCheckBox, QLabel
from PyQt5 import QtGui, QtCore
import sys



class Window(QDialog):
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 CheckBox";
    self.top = 300;
    self.left = 1100;
    self.width = 400;
    self.height = 100;

    self.InitWindow();

  def InitWindow(self):
    self.setWindowIcon(QtGui.QIcon("pic.jpg"));
    self.setWindowTitle(self.title);
    self.setGeometry(self.left, self.top, self.width, self.height);

    self.CreateCheckBox();

    vbox = QVBoxLayout();
    vbox.addWidget(self.groupbox);

    self.label = QLabel(self);
    vbox.addWidget(self.label);
    self.label.setFont(QtGui.QFont("sanserif", 15));

    self.setLayout(vbox);


    self.show();

  def CreateCheckBox(self):
    self.groupbox = QGroupBox("What is your favorite programming language?");
    self.groupbox.setFont(QtGui.QFont("Sanserif", 13));
    hboxLayout = QHBoxLayout();

    self.checkbx1 = QCheckBox("Python");
    self.checkbx1.setIcon(QtGui.QIcon("../_Icons/python.png"));
    self.checkbx1.setIconSize(QtCore.QSize(40,40));
    self.checkbx1.setFont(QtGui.QFont("sanserif", 13));
    self.checkbx1.toggled.connect(self.onCheckBox_Toggled);

    self.checkbx2 = QCheckBox("C++");
    self.checkbx2.setIcon(QtGui.QIcon("../_Icons/C_Plus_Plus.png"));
    self.checkbx2.setIconSize(QtCore.QSize(40,40));
    self.checkbx2.setFont(QtGui.QFont("sanserif", 13));
    self.checkbx2.toggled.connect(self.onCheckBox_Toggled);

    self.checkbx3 = QCheckBox("Java");
    self.checkbx3.setIcon(QtGui.QIcon("../_Icons/java.jpeg"));
    self.checkbx3.setIconSize(QtCore.QSize(40,40));
    self.checkbx3.setFont(QtGui.QFont("sanserif", 13));
    self.checkbx3.toggled.connect(self.onCheckBox_Toggled);
    
    
    hboxLayout.addWidget(self.checkbx1);
    hboxLayout.addWidget(self.checkbx2);
    hboxLayout.addWidget(self.checkbx3);
    self.groupbox.setLayout(hboxLayout);

  def onCheckBox_Toggled(self):
    if self.checkbx1.isChecked():
      self.label.setText("You have selected: " + self.checkbx1.text());
    
    if self.checkbx2.isChecked():
      self.label.setText("You have selected: " + self.checkbx2.text());

    if (self.checkbx3.isChecked()):
      self.label.setText("You have selected: " + self.checkbx3.text());
  



if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());