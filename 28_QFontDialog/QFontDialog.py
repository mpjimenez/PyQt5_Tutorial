from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QToolBar ,QMenuBar, QTextEdit, QFontDialog, QLabel, QVBoxLayout, QHBoxLayout, QAction
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from random import randint


import sys

class Window(QMainWindow):
 
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 QFontDialog";
    self.top = 300;
    self.left = 1100;
    self.width = 500;
    self.height = 400;
    self.iconName = "../_Icons/pic.jpg";
    self.setWindowIcon(QtGui.QIcon(self.iconName));
    self.setWindowTitle(self.title);
    self.setGeometry(self.left, self.top, self.width, self.height);
    
    self.CreateEditor();
    self.CreateMenu();
    self.show();
   



  def CreateMenu(self):
    mainMenu = self.menuBar();

    # create Menu Items
    fileMenu = mainMenu.addMenu("File");
    editMenu = mainMenu.addMenu("Edit");
    viewMenu = mainMenu.addMenu("View");
    helpMenu = mainMenu.addMenu("Help");

    # add action to editMenu
    exitAction = QAction(QIcon("../_Icons/exit.png"), 'Exit', self);
    exitAction.setShortcut("Ctrl+E");
    exitAction.triggered.connect(self.exitWindow);
    fileMenu.addAction(exitAction);


    # Add Actions to editMenu
    copyAction = QAction(QIcon("../_Icons/copy.png"), 'Copy', self);
    copyAction.setShortcut("Ctrl+C");
    editMenu.addAction(copyAction);

    cutAction = QAction(QIcon("../_Icons/cut.png"), 'Cut', self);
    cutAction.setShortcut("Ctrl+X");
    editMenu.addAction(cutAction);

    saveAction = QAction(QIcon("../_Icons/save.png"), 'Save', self);
    saveAction.setShortcut("Ctrl+S");
    editMenu.addAction(saveAction);

    pasteAction = QAction(QIcon("../_Icons/paste.png"), 'paste', self);
    pasteAction.setShortcut("Ctrl+P");
    editMenu.addAction(pasteAction);

    # create fontAction
    fontAction = QAction(QIcon("../_Icons/choose-font.png"), "Font", self);
    fontAction.setShortcut("Ctrl+F");
    fontAction.triggered.connect(self.fontDialog);
    viewMenu.addAction(fontAction);



    # create Toolbar
    toolbar = self.addToolBar("ToolBar");

    # add actions to tool bar
    toolbar.addAction(copyAction);
    toolbar.addAction(cutAction);
    toolbar.addAction(pasteAction);
    toolbar.addAction(saveAction);
    toolbar.addAction(exitAction);
    toolbar.addAction(fontAction);


  def exitWindow(self):
    self.close()

  def CreateEditor(self):
    self.textEdit = QTextEdit(self);
    self.setCentralWidget(self.textEdit);

  def fontDialog(self):
    font, ok = QFontDialog.getFont();
    if ok:
      self.textEdit.setFont(font);

    
    

    # Add UI components to layout
    
  
    

   

if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());