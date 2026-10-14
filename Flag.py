import io
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QButtonGroup


ui = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>634</width>
    <height>534</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>70</y>
      <width>160</width>
      <height>123</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLabel" name="label">
       <property name="font">
        <font>
         <pointsize>20</pointsize>
        </font>
       </property>
       <property name="text">
        <string>Цвет №1</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_3">
       <property name="text">
        <string>Синий</string>
       </property>
       <property name="checked">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_2">
       <property name="text">
        <string>Красный</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_4">
       <property name="text">
        <string>Зелёный</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>70</y>
      <width>160</width>
      <height>123</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_2">
     <item>
      <widget class="QLabel" name="label_2">
       <property name="font">
        <font>
         <pointsize>20</pointsize>
        </font>
       </property>
       <property name="text">
        <string>Цвет №2</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_5">
       <property name="text">
        <string>Синий</string>
       </property>
       <property name="checked">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_6">
       <property name="text">
        <string>Красный</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_7">
       <property name="text">
        <string>Зелёный</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="make_flag">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>250</y>
      <width>111</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Сделать флаг</string>
    </property>
   </widget>
   <widget class="QLabel" name="result">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>220</y>
      <width>341</width>
      <height>251</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>8</pointsize>
     </font>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_3">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>70</y>
      <width>160</width>
      <height>123</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_3">
     <item>
      <widget class="QLabel" name="label_4">
       <property name="font">
        <font>
         <pointsize>20</pointsize>
        </font>
       </property>
       <property name="text">
        <string>Цвет №3</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_8">
       <property name="text">
        <string>Синий</string>
       </property>
       <property name="checked">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_9">
       <property name="text">
        <string>Красный</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_10">
       <property name="text">
        <string>Зелёный</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>634</width>
     <height>24</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(io.StringIO(ui), self)  # Одна строка — и всё работает!
        self.make_flag.clicked.connect(self.run1)
        self.color_group_1= QButtonGroup(self)
        self.data = ['','','']
        self.color_group_1.addButton(self.radioButton_2)
        self.color_group_1.addButton(self.radioButton_3)
        self.color_group_1.addButton(self.radioButton_4)
        self.color_group_2 = QButtonGroup(self)
        self.color_group_2.addButton(self.radioButton_5)
        self.color_group_2.addButton(self.radioButton_6)
        self.color_group_2.addButton(self.radioButton_7)
        self.color_group_1.buttonClicked.connect(self.run)
        self.color_group_2.buttonClicked.connect(self.run)
    def run1(self):
        self.result.setText(f'Цвета: {self.data[0]}, {self.data[1]}')
    def run(self, a):
        if self.sender() == self.color_group_1:
            self.data[0]= a.text()
        if self.sender() == self.color_group_2:
            self.data[1] = a.text()
        print(self.data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec())