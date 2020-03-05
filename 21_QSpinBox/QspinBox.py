from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5 import QtGui
from PyQt5.QtCore import Qt


import sys

class Window(QWidget):
 
  def __init__(self, val):
    super().__init__()

    self.title = "PyQt5 QSpin Box";
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

    # Create SpinBox
    self.spinBox = QSpinBox();
    self.spinBox.valueChanged.connect(self.spin_changed);

     # Create Label
    self.label = QLabel("Initial Value: " + str(self.spinBox.value()));
    self.label.setFont(QtGui.QFont("Sanserif", 15));
    self.label.setAlignment(Qt.AlignCenter);
    

    # Add UI components to layout
    vbox.addWidget(self.spinBox);
    vbox.addWidget(self.label);
    
    # setLayout to window
    self.setLayout(vbox);
    
    self.show();

  def spin_changed(self):
    spinValue = self.spinBox.value();
    self.label.setText("Current Value is: " + str(spinValue));

if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window(20);
  sys.exit(App.exec());