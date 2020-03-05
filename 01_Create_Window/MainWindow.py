from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui
import sys



class Window(QMainWindow):
  def __init__(self):
    super().__init__()

    self.top = 300;
    self.left = 1100;
    self.width = 400;
    self.height = 250;
    self.iconName = "../_Icons/pic.jpg";
    self.title = "PyQt5 Window";
   

    self.InitWindow();

  def InitWindow(self):
    self.setWindowIcon(QtGui.QIcon(iconName));
    self.setWindowTitle(self.title);
    self.setGeometry(self.left, self.top, self.width, self.height);

    self.show()



App = QApplication(sys.argv);
window = Window();

sys.exit(App.exec());
