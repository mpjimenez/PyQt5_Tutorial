from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QDialog, QVBoxLayout
from PyQt5 import QtGui
import sys

class Window(QDialog):
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 Window";
    self.top = 500;
    self.left = 200;
    self.width = 400;
    self.height = 300;
    self.iconName = "../_Icons/pic.jpg";

    self.InitWindow();

  def InitWindow(self):
    self.setWindowIcon(QtGui.QIcon(self.iconName));
    self.setWindowTitle(self.title);
    self.setGeometry(self.left, self.top, self.width, self.height);

    vbox = QVBoxLayout();
    label1 = QLabel("This is my PyQt5 Label");
    vbox.addWidget(label1);

    label2 = QLabel("This is PyQt5 GUI Application Development");
    label2.setFont(QtGui.QFont("sanserif", 20));
    label2.setStyleSheet('color:red');
    vbox.addWidget(label2);

    self.setLayout(vbox);
    self.show();



if __name__=="__main__":
  App = QApplication(sys.argv);
  window = Window();
  sys.exit(App.exec())