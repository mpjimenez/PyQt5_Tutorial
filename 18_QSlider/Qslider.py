from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QVBoxLayout, QSplitter, QLineEdit, QSlider, QLabel
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt


import sys

class Window(QWidget):
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 QSlider";
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
    self.setStyleSheet('background-color:green');
    hbox = QHBoxLayout();

    self.label = QLabel("0");
    self.label.setFont(QtGui.QFont("sanserif", 15));

    # Create Slider: Horizontal or Vertical
    self.slider = QSlider()
    self.slider.setOrientation(Qt.Horizontal);
    self.slider.setTickPosition(QSlider.TicksBelow);
    self.slider.setTickInterval(10);
    self.slider.setMinimum(0);
    self.slider.setMaximum(100);
    self.slider.valueChanged.connect(self.changed_value);


    # Add UI components
    hbox.addWidget(self.slider);
    hbox.addWidget(self.label);
   
    self.setLayout(hbox);
    self.show();
    

  def changed_value(self):
    size = self.slider.value();
    self.label.setText(str(size));
  


if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());