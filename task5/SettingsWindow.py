import sys

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PyQt5.QtWidgets import *

import Game


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 188)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 70, 101, 31))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(180, 70, 41, 31))
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(230, 70, 113, 31))
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(70, 20, 271, 31))
        self.lineEdit_4.setLayoutDirection(Qt.LeftToRight)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 140, 111, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Dialog", u"\u043d\u0430", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0430\u0437\u043c\u0435\u0440\u044b \u043e\u043a\u043d\u0430:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0418\u0433\u0440\u0430\u0442\u044c", None))
    # retranslateUi



class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Меняем текст
        self.ui.lineEdit.setText("400")
        self.ui.lineEdit_3.setText("400")

        # только чтение без изменения содержимого.
        self.ui.lineEdit_2.setReadOnly(True)
        self.ui.lineEdit_4.setReadOnly(True)

        self.ui.pushButton.clicked.connect(self.btn_clicked())

    def btn_clicked(self):
        app = QApplication([])
        game_window = Game.GameWindow(int(self.ui.lineEdit.text()), int(self.ui.lineEdit_3.text()))
        game_window.show()
        sys.exit(app.exec())


app = QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())

