import view
import model
import sys
from PyQt5 import QtGui, QtWidgets


class Presenter:
    def __init__(self, view_):
        self.view = view_
        self.model = model.LinkedList()

    def duplicates(self):
        self.model.remove_duplicates()
        self.update()

    def sort_asc(self):
        self.model.sort_asc()
        self.update()

    def sort_desc(self):
        self.model.sort_desc()
        self.update()

    def reverse(self):
        self.model.reverse()
        self.update()

    def reset(self):
        for i in range(self.model.size):
            self.delete(0)
        self.view.list.deactivate_node()

    def remove_node(self, p):
        if p is None: return
        self.view.list.pressed(event=None, source_object=self.view.list.nodes[p])
        self.delete(p)

    def delete(self, p):
        self.model.remove(p)
        self.update()

    def insert(self, value):
        if self.model.size == 5:  # size of the list cannot be greater than 5 due to GUI
            return
        if value == "" or len(value) > 8:
            return
        else:
            self.view.input_field.setText("")
            self.model.insert(value)
            self.update()

    def update(self):
        self.view.list.show_nodes(self.model.size)
        i = 0
        for a in self.model.get_values():
            self.view.list.nodes[i].setText(str(a))
            i += 1

    def show(self):

        app = QtWidgets.QApplication(sys.argv)
        app.setWindowIcon(QtGui.QIcon('Graphic/icon.png'))

        MainWindow = QtWidgets.QMainWindow()

        self.view.setup(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
