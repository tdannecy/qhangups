# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qhangups/qhangupsconversations.ui'
#
# Created: Thu Oct  9 00:54:07 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_QHangupsConversations(object):
    def setupUi(self, QHangupsConversations):
        QHangupsConversations.setObjectName(_fromUtf8("QHangupsConversations"))
        QHangupsConversations.resize(500, 350)
        self.gridLayout = QtGui.QGridLayout(QHangupsConversations)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.conversationsTabWidget = QtGui.QTabWidget(QHangupsConversations)
        self.conversationsTabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.conversationsTabWidget.setTabsClosable(True)
        self.conversationsTabWidget.setMovable(True)
        self.conversationsTabWidget.setObjectName(_fromUtf8("conversationsTabWidget"))
        self.gridLayout.addWidget(self.conversationsTabWidget, 0, 0, 1, 1)

        self.retranslateUi(QHangupsConversations)
        self.conversationsTabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(QHangupsConversations)

    def retranslateUi(self, QHangupsConversations):
        QHangupsConversations.setWindowTitle(_translate("QHangupsConversations", "QHangups - Conversations", None))

