from PyQt5.QtWidgets import QApplication, QDialog, QGroupBox, QVBoxLayout, QHBoxLayout, QRadioButton, QLabel
from PyQt5 import QtGui, QtCore
import sys



class Window(QDialog):
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 Radio Button";
    self.top = 300;
    self.left = 1100;
    self.width = 400;
    self.height = 100;

    self.InitWindow();

  def InitWindow(self):
    self.setWindowIcon(QtGui.QIcon("pic.jpg"));
    self.setWindowTitle(self.title);
    self.setGeometry(self.left, self.top, self.width, self.height);

    self.radioButton();

    vbox = QVBoxLayout();
    
    self.label = QLabel(self);
    self.label.setFont(QtGui.QFont("Sanserif", 15));

    vbox.addWidget(self.groupBox);
    vbox.addWidget(self.label);
    self.setLayout(vbox);


    self.show()


  def radioButton(self):
    self.groupBox = QGroupBox("What is your favorite Sport ?");
    self.groupBox.setFont(QtGui.QFont("sanserif", 13));
    hboxLayout = QHBoxLayout();

    self.radioBtn1 = QRadioButton("Soccer");
    self.radioBtn1.setChecked(True);
    self.radioBtn1.setIcon(QtGui.QIcon("../_Icons/soccer.png"));
    self.radioBtn1.setFont(QtGui.QFont("sanserif", 13));
    self.radioBtn1.setIconSize(QtCore.QSize(40, 40));
    self.radioBtn1.toggled.connect(self.onRadioBtn);

    self.radioBtn2 = QRadioButton("Basketball");
    self.radioBtn2.setIcon(QtGui.QIcon("../_Icons/basketball.png"));
    self.radioBtn2.setFont(QtGui.QFont("sanserif", 13));
    self.radioBtn2.setIconSize(QtCore.QSize(40, 40));
    self.radioBtn2.toggled.connect(self.onRadioBtn);

    self.radioBtn3 = QRadioButton("Baseball");
    self.radioBtn3.setIcon(QtGui.QIcon("../_Icons/baseball.jpg"));
    self.radioBtn3.setFont(QtGui.QFont("sanserif", 13));
    self.radioBtn3.setIconSize(QtCore.QSize(40, 40));
    self.radioBtn3.toggled.connect(self.onRadioBtn);


    hboxLayout.addWidget(self.radioBtn1);
    hboxLayout.addWidget(self.radioBtn2);
    hboxLayout.addWidget(self.radioBtn3);


    self.groupBox.setLayout(hboxLayout);

  def onRadioBtn(self):
    radioBtn = self.sender();

    if (radioBtn.isChecked()):
      self.label.setText("You have selected " + radioBtn.text());



if __name__ == "__main__":
  App = QApplication(sys.argv);
  window = Window();

  sys.exit(App.exec());
