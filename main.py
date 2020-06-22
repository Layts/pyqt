import sys
import table

if __name__ == '__main__':
    app = table.QtWidgets.QApplication(sys.argv)
    window = table.MainWindow()
    window.show()
    app.exec_()
