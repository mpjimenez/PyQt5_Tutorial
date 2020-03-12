from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QToolBar ,QMenuBar, QColorDialog ,QTextEdit, QFontDialog, QLabel, QVBoxLayout, QHBoxLayout, QAction
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog

from random import randint


import sys

class Window(QMainWindow):
 
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 QPreviewDiaglog";
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

    # add print Action
    printAction = QAction(QIcon("../_Icons/print.png"), "Print", self);
    printAction.triggered.connect(self.printDialog);
    fileMenu.addAction(printAction);

    # add print preview action
    printPreviewAction = QAction(QIcon("../_Icons/print_preview.png"), "Print Preview", self);
    printPreviewAction.triggered.connect(self.printPreviewDialog);
    fileMenu.addAction(printPreviewAction); # add to fileMenu
    
    # add exit action
    exitAction = QAction(QIcon("../_Icons/exit.png"), 'Exit', self);
    exitAction.setShortcut("Ctrl+E");
    exitAction.triggered.connect(self.exitWindow);
    fileMenu.addAction(exitAction); # add to fileMenu


    # add copy action
    copyAction = QAction(QIcon("../_Icons/copy.png"), 'Copy', self);
    copyAction.setShortcut("Ctrl+C");
    editMenu.addAction(copyAction); # add to editMenu

    # add cut Action
    cutAction = QAction(QIcon("../_Icons/cut.png"), 'Cut', self);
    cutAction.setShortcut("Ctrl+X");
    editMenu.addAction(cutAction); # add to editMenu

    # add save action
    saveAction = QAction(QIcon("../_Icons/save.png"), 'Save', self);
    saveAction.setShortcut("Ctrl+S");
    editMenu.addAction(saveAction); # add to editMenu

    # add paste action
    pasteAction = QAction(QIcon("../_Icons/paste.png"), 'paste', self);
    pasteAction.setShortcut("Ctrl+P");
    editMenu.addAction(pasteAction); # add to editMenu

    # create fontAction and add to viewMenu
    fontAction = QAction(QIcon("../_Icons/choose-font.png"), "Font", self);
    fontAction.setShortcut("Ctrl+F");
    fontAction.triggered.connect(self.fontDialog);
    viewMenu.addAction(fontAction); # add to viewMenu

    # create colorAction and add to viewMenu
    colorAction = QAction(QIcon("../_Icons/color.svg"), "Color", self);
    colorAction.triggered.connect(self.colorDialog);
    viewMenu.addAction(colorAction); # add to viewMenu

    # create Toolbar
    toolbar = self.addToolBar("ToolBar");

    # add actions to tool bar
    toolbar.addAction(copyAction);
    toolbar.addAction(cutAction);
    toolbar.addAction(pasteAction);
    toolbar.addAction(saveAction);
    toolbar.addAction(exitAction);
    toolbar.addAction(fontAction);
    toolbar.addAction(colorAction);
    toolbar.addAction(printAction);
    toolbar.addAction(printPreviewAction);


  def exitWindow(self):
    self.close()

  def CreateEditor(self):
    self.textEdit = QTextEdit(self);
    self.setCentralWidget(self.textEdit);

  def fontDialog(self):
    font, ok = QFontDialog.getFont();
    if ok:
      self.textEdit.setFont(font);

  def colorDialog(self):
    color = QColorDialog.getColor();
    self.textEdit.setTextColor(color);

  def printDialog(self):
    printer = QPrinter(QPrinter.HighResolution);
    dialog = QPrintDialog(printer, self);

    if dialog.exec_() == QPrintDialog.Accepted:
      self.textEdit.print_(printer);
  
  
  def printPreviewDialog(self):
    printer = QPrinter(QPrinter.HighResolution);
    previewDialog = QPrintPreviewDialog(printer, self);
    previewDialog.paintRequested.connect(self.printPreview);
    previewDialog.exec_();

  def printPreview(self, printer):
    self.textEdit.print_(printer);
    

   

if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());