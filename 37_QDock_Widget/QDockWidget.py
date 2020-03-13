from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QListWidget
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

import sys

class DockDialog(QMainWindow):
  def __init__(self):
    super().__init__()

    self.title = 'PyQt5 QDockWidget';
    self.iconName = "../_Icons/pic.jpg";
    self.top = 300;
    self.left = 1100;
    self.width = 400;
    self.height = 250;
    self.setWindowTitle(self.title);
    self.setWindowIcon(QIcon(self.iconName));
    self.setGeometry(self.left, self.top, self.width, self.height);
    
    self.createDockWidget();
    self.show();



  def createDockWidget(self):
    menubar = self.menuBar();
    file = menubar.addMenu("File");
    edit = menubar.addMenu('Edit');

    file.addAction("New");
    file.addAction("Save");
    file.addAction("Close");

    self.dock = QDockWidget('Dockable', self);
    self.listwidget = QListWidget();
    
    list1 = ['Python', 'C++', 'Java', 'C#'];
    self.listwidget.addItems(list1);
    self.dock.setWidget(self.listwidget);
    self.setCentralWidget(QTextEdit());
    self.addDockWidget(Qt.RightDockWidgetArea, self.dock);




if __name__ == "__main__":
  App = QApplication(sys.argv);
  window = DockDialog();
  sys.exit(App.exec());