from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QToolBar , QMenu ,QMenuBar, QColorDialog ,QTextEdit, QFileDialog ,QFontDialog\
                            ,QLabel, QVBoxLayout, QHBoxLayout, QAction, QMessageBox
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QFileInfo
from PyQt5.QtGui import QIcon
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog

from random import randint


import sys

class Window(QMainWindow):
 
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 QContextMenu";
    self.top = 300;
    self.left = 1100;
    self.width = 500;
    self.height = 400;
    self.iconName = "../_Icons/pic.jpg";
    self.setWindowIcon(QtGui.QIcon(self.iconName));
    self.setWindowTitle(self.title);
    self.setGeometry(self.left, self.top, self.width, self.height);
    
   
    self.show();

  '''
    once you run the program right click and the context window will show up!
  '''
  def contextMenuEvent(self, event):
    contextMenu = QMenu(self);

    # create 3 actions
    newAction = contextMenu.addAction("New");
    openAction = contextMenu.addAction("Open");
    quitAction = contextMenu.addAction('Quit');

    action = contextMenu.exec_(self.mapToGlobal(event.pos()));

    if action == quitAction:
      self.close();



  
if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());