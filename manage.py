import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from front import style
import pandas as pd


mainWindow, _ = loadUiType('front/table.ui')


class Mainwindow(QMainWindow, mainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.setWindowTitle("Main page")
        self.setWindowIcon(QIcon('icon/python4.webp'))

        self.Handel_Buttons()
        self.tableWidget.verticalHeader().hide()

        self.submit_button.clicked.connect(self.submit)
        self.calasic_theme()
        self.theme = 'clasic'

        self.update_data()



    def button_clicked(self, row):

        self.df.drop(row, inplace=True)

        # Save the modified DataFrame back to Excel
        self.df.to_excel('MOCK_DATA.xlsx', index=False)
        self.update_data()

    def update_data(self):

        self.Name.setText('')
        self.LastName.setText('')
        self.City.setText('')
        self.tableWidget.setColumnCount(6)
        
        button_color = 'B31312'

        file_path = 'MOCK_DATA.xlsx'
        self.df = pd.read_excel(file_path)
        self.tableWidget.clear()
        headers = ['Name', 'LastName', 'City', '', '', '']
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for index, row in self.df.iterrows():

            setattr(self, f"button_{index}", QPushButton("Delete"))       
            getattr(self, f"button_{index}").setStyleSheet(style.button(button_color))


            for colume in range(3):
                item = QTableWidgetItem(row.iloc[colume])
                self.tableWidget.setItem(index, colume, item)

            self.tableWidget.setCellWidget(index, 3, getattr(self, f"button_{index}"))  # Set the button in the cell
            getattr(self, f"button_{index}").clicked.connect(lambda _, idx=index: self.button_clicked(idx))

    def submit(self):

        name = self.Name.text()
        lastName = self.LastName.text()
        city =self.City.text()

        file_path = 'MOCK_DATA.xlsx'
        existing_df = pd.read_excel(file_path)

        if self.theme == 'dark':
            textColor = 'F1F0CF'
            lineEdit = '84A9AC'
            border_lineEdit = '018383'
        else:
            textColor = '333333'
            lineEdit = 'F2EFE5'
            border_lineEdit = 'cccccc'

        self.groupBox.setStyleSheet(style.groupBox(2, '468B97', lineEdit, border_lineEdit, textColor))

        if name == '' or lastName == '' or city == '' :
            self.error(lineEdit)
        else:
            # Create DataFrame for your new data
            new_data = pd.DataFrame({'Name': [name], 'LastName': [lastName], 'City': [city]})
            # Append new data to the existing DataFrame
            combined_df = existing_df._append(new_data, ignore_index=True)
            # Write the combined DataFrame back to the Excel file
            combined_df.to_excel(file_path, index=False)
            self.error(lineEdit)
            self.update_data()

    def error(self, lineEditColor):
        name = self.Name.text()
        lastName = self.LastName.text()
        city =self.City.text()
        border_color = 'B80000'

        if name == '':
            self.Name.setStyleSheet(style.lineEdit(2, border_color, lineEditColor))
        else:
            self.Name.setStyleSheet(style.lineEdit(1, 'cccccc', lineEditColor))
        if lastName == '':
            self.LastName.setStyleSheet(style.lineEdit(2, border_color, lineEditColor))
        else:
            self.LastName.setStyleSheet(style.lineEdit(1, 'cccccc', lineEditColor))
        if city == '':
            self.City.setStyleSheet(style.lineEdit(2, border_color, lineEditColor))
        else:
            self.City.setStyleSheet(style.lineEdit(1, 'cccccc', lineEditColor))

    def Handel_Buttons(self):

        self.ClasicTheme.clicked.connect(self.calasic_theme)
        self.darktheme.clicked.connect(self.dark_theme)

    def dark_theme(self):

        self.theme = 'dark'

        main_color = '04364A'
        textColor = 'F1F0CF'
        lineEdit = '84A9AC'
        border_lineEdit = '018383'
        table_border = 2 
        table_border_color = '247881'
        table_color = '84A9AC' 
        header_color = '175566'
        header_border = '84A9AC'
        scrollbar_baseColor = '175566'
        scrollbar_Color = '04364A'

        vertical_scrollbar = self.tableWidget.verticalScrollBar()
        horizontal_scrollbar = self.tableWidget.horizontalScrollBar()
        vertical_scrollbar.setStyleSheet(style.scrollbar('vertical', scrollbar_baseColor, scrollbar_Color))
        horizontal_scrollbar.setStyleSheet(style.scrollbar('horizontal', scrollbar_baseColor, scrollbar_Color))
        table_style = self.tableWidget.setStyleSheet(style.table(table_border, table_border_color,
                                                table_color, header_color, header_border, textColor))
        self.groupBox.setStyleSheet(style.groupBox(2, '468B97', lineEdit, border_lineEdit, textColor))
        self.submit_button.setStyleSheet(style.button('008012'))
        self.Name.setStyleSheet(style.lineEdit(2, border_lineEdit, lineEdit))
        self.LastName.setStyleSheet(style.lineEdit(2, border_lineEdit, lineEdit))
        self.City.setStyleSheet(style.lineEdit(2, border_lineEdit, lineEdit))
        self.setStyleSheet(style.main(main_color))                   

    def calasic_theme(self):

        self.theme = 'clasic'

        main_color = 'FBF6EE'
        textColor = '333333'
        lineEdit = 'F2EFE5'
        border_lineEdit = 'cccccc'
        table_border = 2 
        table_border_color = '000000'
        table_color = 'FFF7F1' 
        header_color = 'e9e7e7'
        header_border = 'FFF7F1'
        scrollbar_baseColor = 'f0f0f0'
        scrollbar_Color = 'cccccc'

        vertical_scrollbar = self.tableWidget.verticalScrollBar()
        horizontal_scrollbar = self.tableWidget.horizontalScrollBar()
        vertical_scrollbar.setStyleSheet(style.scrollbar('vertical', scrollbar_baseColor, scrollbar_Color))
        horizontal_scrollbar.setStyleSheet(style.scrollbar('horizontal', scrollbar_baseColor, scrollbar_Color))
        table_style = self.tableWidget.setStyleSheet(style.table(table_border, table_border_color,
                                                table_color, header_color, header_border, textColor))
        self.groupBox.setStyleSheet(style.groupBox(2, '468B97', lineEdit, border_lineEdit, textColor))
        self.submit_button.setStyleSheet(style.button('008012'))
        self.Name.setStyleSheet(style.lineEdit(2, border_lineEdit, lineEdit))
        self.LastName.setStyleSheet(style.lineEdit(2, border_lineEdit, lineEdit))
        self.City.setStyleSheet(style.lineEdit(2, border_lineEdit, lineEdit))
        self.setStyleSheet(style.main(main_color))                   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.setFixedSize(880, 568)
    window.show()
    app.exec_()
