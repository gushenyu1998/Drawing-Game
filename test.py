import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import gui.mainwindows

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = gui.mainwindows.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())