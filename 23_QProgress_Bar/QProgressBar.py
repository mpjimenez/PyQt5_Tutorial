from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QThread, pyqtSignal


import sys, time

class MyThread(QThread):
  
  change_value = pyqtSignal(int);

  def run(self):
    cnt = 0;
    while(cnt < 100):
      cnt +=1;

      time.sleep(0.3);
      self.change_value.emit(cnt)


class Window(QWidget):
 
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 QProgress Bar";
    self.top = 300;
    self.left = 1100;
    self.width = 300;
    self.height = 100;
    self.iconName = "../_Icons/pic.jpg";
    self.setWindowIcon(QtGui.QIcon(self.iconName));
    self.setWindowTitle(self.title);
    self.setGeometry(self.left, self.top, self.width, self.height);
    self.show();

    self.InitUI();
   


  def InitUI(self):
    vbox = QVBoxLayout();

    # create Progress Bar
    self.progressbar = QProgressBar();
    self.progressbar.setMaximum(100);
    self.progressbar.setStyleSheet("QProgressBar {border:2px solid grey; border-radius:8px; padding:1px}"
                                    "QProgressBar::chunk {background:green}");

    #self.progressbar.setOrientation(Qt.Vertical);
    self.progressbar.setTextVisible(False);

    # create pushButton
    self.btn = QPushButton("Run Progressbar");
    self.btn.clicked.connect(self.startProgressBar);
    self.btn.setStyleSheet('background-color:yellow');


    # Add UI components to layout
    vbox.addWidget(self.progressbar);
    vbox.addWidget(self.btn);
    self.setLayout(vbox);

  def startProgressBar(self):
    self.thread = MyThread();
    self.thread.change_value.connect(self.setProgressVal);

    self.thread.start();

  def setProgressVal(self, val):
    self.progressbar.setValue(val);
    
    
   
if __name__ == "__main__":
  App = QApplication(sys.argv)
  window = Window();
  sys.exit(App.exec());