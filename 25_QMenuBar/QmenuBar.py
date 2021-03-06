from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenuBar, QLabel, QVBoxLayout, QHBoxLayout, QAction
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from random import randint


import sys

class Window(QMainWindow):
 
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 QMenuBar";
    self.top = 300;
    self.left = 1100;
    self.width = 400;
    self.height = 250;
    self.iconName = "../_Icons/pic.jpg";
    self.setWindowIcon(QtGui.QIcon(self.iconName));
    self.setWindowTitle(self.title);
    self.setGeometry(self.left, self.top, self.width, self.height);
    

    self.CreateMenu();
    self.show();
   



  def CreateMenu(self):
    mainMenu = self.menuBar();
    fileMenu = mainMenu.addMenu("File");
    editMenu = mainMenu.addMenu("Edit");
    viewMenu = mainMenu.addMenu("View");
    helpMenu = mainMenu.addMenu("Help");

    # Add Actions to fileMenu
    copyAction = QAction(QIcon("../_Icons/copy.png"), 'Copy', self);
    copyAction.setShortcut("Ctrl+C");
    fileMenu.addAction(copyAction);

    cutAction = QAction(QIcon("../_Icons/cut.png"), 'Cut', self);
    cutAction.setShortcut("Ctrl+X");
    fileMenu.addAction(cutAction);

    saveAction = QAction(QIcon("../_Icons/save.png"), 'Copy', self);
    saveAction.setShortcut("Ctrl+S");
    fileMenu.addAction(saveAction);

    # Add Actions to editMenu
    exitAction = QAction(QIcon("../_Icons/exit.png"), 'Exit', self);
    exitAction.setShortcut("Ctrl+E");
    exitAction.triggered.connect(self.exitWindow);
    editMenu.addAction(exitAction);

  def exitWindow(self):
    self.close()


    
    

    # Add UI components to layout
    
  
    

   

if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());