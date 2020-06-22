from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
import db


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

    def headerData(self, column, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if orientation == QtCore.Qt.Horizontal:
            if column == 0:
                return QtCore.QVariant('Название')
            elif column == 1:
                return QtCore.QVariant('Цена')
            elif column == 2:
                return QtCore.QVariant('Ссылка на товар')
            elif column == 3:
                return QtCore.QVariant('Описание')


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = QtWidgets.QTableView()
        self.setWindowTitle('Тестовое задание')
        self.resize(1000, 500)
        self.model = TableModel(db.get_data())
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)
