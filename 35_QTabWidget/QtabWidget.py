from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QTabWidget, QDialogButtonBox, QGroupBox, QComboBox, QCheckBox,\
                            QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon

import sys

class Tab(QDialog):
  def __init__(self):
    super().__init__()

    self.setWindowTitle('PyQt5 TabWidget');
    self.setWindowIcon(QIcon('../_Icons/pic.jpg'));
    self.top = 300;
    self.left = 1100;
    self.width = 400;
    self.height = 250;
    self.iconName = "../_Icons/pic.jpg";
    self.setGeometry(self.left, self.top, self.width, self.height);

    # create layout
    vbox = QVBoxLayout();

    # crate QTabWidget
    tabWidget = QTabWidget();

    # create buttonBox
    buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel);
    buttonBox.accepted.connect(self.accept);
    buttonBox.rejected.connect(self.reject);

    # add tabs to tabWidget
    tabWidget.addTab(TabContact(), 'Contact Details');
    tabWidget.addTab(TabPersonDetatils(), 'Personal Details');


    vbox.addWidget(tabWidget);
    vbox.addWidget(buttonBox);
    self.setLayout(vbox);


class TabContact(QWidget):
  def __init__(self):
    super().__init__()

    # create widgets for the Contact Tab
    nameLabel = QLabel('Name: ');
    nameEdit = QLineEdit();

    phone = QLabel('Phone');
    phoneEdit = QLineEdit();

    email = QLabel('Email');
    emailEdit = QLineEdit();

    address = QLabel('Address');
    addressEdit = QLineEdit();

    # create vbox layout for the Contact Tab
    vbox = QVBoxLayout();

    # add the wigets to the layout
    vbox.addWidget(nameLabel);
    vbox.addWidget(nameEdit);
    vbox.addWidget(phone);
    vbox.addWidget(phoneEdit);
    vbox.addWidget(email);
    vbox.addWidget(emailEdit);
    vbox.addWidget(address);
    vbox.addWidget(addressEdit);

    self.setLayout(vbox);


class TabPersonDetatils(QWidget):
  def __init__(self):
    super().__init__()

    # create the groupBoxes 
    groupBox1 = QGroupBox('Select your gender');
    groupBox2 = QGroupBox('select your favorite programming language');

    # inputs for comboBox
    list1 = ['Male', 'Female', 'Other'];

    combo = QComboBox();
    combo.addItems(list1);
   
    # inputs for groupbox2
    python = QCheckBox('Python');
    java = QCheckBox('Java');
    cpp = QCheckBox('C++');
    kotlin = QCheckBox('Kotlin');
    csharp = QCheckBox('C#');


    
    vbox1 = QVBoxLayout();
    vbox1.addWidget(combo);
    groupBox1.setLayout(vbox1);

    vbox2 = QVBoxLayout();
    vbox2.addWidget(python);
    vbox2.addWidget(java);
    vbox2.addWidget(cpp);
    vbox2.addWidget(kotlin);
    vbox2.addWidget(csharp);
    groupBox2.setLayout(vbox2);


    mainLayout = QVBoxLayout();
    mainLayout.addWidget(groupBox1);
    mainLayout.addWidget(groupBox2);


    self.setLayout(mainLayout);



  
if __name__ == "__main__":
  App = QApplication(sys.argv);
  tabDialog = Tab();
  tabDialog.show();
  sys.exit(App.exec());