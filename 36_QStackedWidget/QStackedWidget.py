from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QLabel, QPushButton, QVBoxLayout, QStackedWidget
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon

import sys

class StackWidget(QDialog):
  def __init__(self):
    super().__init__()

    self.title = 'PyQt5 QStackWidget';
    self.iconName = "../_Icons/pic.jpg";
    self.top = 300;
    self.left = 1100;
    self.width = 400;
    self.height = 250;
    self.setWindowTitle(self.title);
    self.setWindowIcon(QIcon(self.iconName));
    self.setGeometry(self.left, self.top, self.width, self.height);
    self.show();

    self.StackedWidget();
    

  def StackedWidget(self):

    vbox = QVBoxLayout();
    self.stackedWidget = QStackedWidget();
    vbox.addWidget(self.stackedWidget);

    for x in range(0, 8):
      label = QLabel('Stacked Child ' + str(x + 1));
      label.setFont(QtGui.QFont('Sanserif', 15));
      label.setStyleSheet('color:red');

      self.stackedWidget.addWidget(label);

      self.button = QPushButton("Stack " + str(x + 1));
      self.button.setStyleSheet('background-color:green');
      self.button.page = x;

      self.button.clicked.connect(self.btn_clicked);
      vbox.addWidget(self.button);

    self.setLayout(vbox);


  def btn_clicked(self):
    self.button = self.sender();
    self.stackedWidget.setCurrentIndex(self.button.page);


  
if __name__ == "__main__":
  App = QApplication(sys.argv);
  window = StackWidget();
  sys.exit(App.exec());