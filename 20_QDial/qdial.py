from PyQt5.QtWidgets import QApplication, QWidget, QDial, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5 import QtGui


import sys

class Window(QWidget):
 
  def __init__(self, val):
    super().__init__()

    self.title = "PyQt5 QDial";
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
    
    # Create Layout
    vbox = QVBoxLayout();

    # Create Label
    self.label = QLabel(self);
    self.label.setFont(QtGui.QFont("Sanserif", 15));

    # Crate Dial
    self.dial = QDial();
    self.dial.setMinimum(0);
    self.dial.setMaximum(100);
    self.dial.setValue(30);
    self.label.setText("Initial Value: " + str(self.dial.value()));
    self.dial.valueChanged.connect(self.dial_changed);

    # Add UI components to layout
    vbox.addWidget(self.dial);
    vbox.addWidget(self.label);
    self.setLayout(vbox);
    

    self.show();

  def dial_changed(self):
    getValue = self.dial.value();
    self.label.setText("Dial is changing " + str(getValue));


   

if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window(20);
  sys.exit(App.exec());