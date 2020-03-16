

import sys
from interface import *

from PyQt5.QtWidgets import QApplication, QMainWindow

#程序运行头 GUI初始化界面
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())