from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap

import sys

class Window(QDialog):
  def __init__(self):
    super().__init__()

    
    self.title = "PyQt5 Adding Image";
    self.top = 400;
    self.left = 1200;
    self.width = 500;
    self.height = 400;
    self.iconName = "../_Icons/pic.jpg";

    self.InitWindow();


  def InitWindow(self):
    self.setWindowIcon(QtGui.QIcon(self.iconName));
    self.setWindowTitle(self.title);
    self.setGeometry(self.left, self.top, self.width, self.height);

    vbox = QVBoxLayout();
    labelImage = QLabel(self);
    pixmap = QPixmap("../_Icons/basketball.jpg");
    labelImage.setPixmap(pixmap);
    vbox.addWidget(labelImage);

    self.setLayout(vbox);
    self.show();






if __name__=="__main__":
  App = QApplication(sys.argv);
  window = Window();
  sys.exit(App.exec());
