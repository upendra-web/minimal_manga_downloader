# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manga2.ui'
#
# Created by: PyQt4 UI code generator 4.12
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(768, 583)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.MainWidget = QtGui.QTabWidget(self.centralwidget)
        self.MainWidget.setObjectName(_fromUtf8("MainWidget"))
        self.InfoTab = QtGui.QWidget()
        self.InfoTab.setObjectName(_fromUtf8("InfoTab"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.InfoTab)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.splitter = QtGui.QSplitter(self.InfoTab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.MangaSearchInput = QtGui.QLineEdit(self.layoutWidget)
        self.MangaSearchInput.setObjectName(_fromUtf8("MangaSearchInput"))
        self.verticalLayout_3.addWidget(self.MangaSearchInput)
        self.MangaList = QtGui.QListView(self.layoutWidget)
        self.MangaList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.MangaList.setObjectName(_fromUtf8("MangaList"))
        self.verticalLayout_3.addWidget(self.MangaList)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.LinkInput = QtGui.QLineEdit(self.layoutWidget1)
        self.LinkInput.setObjectName(_fromUtf8("LinkInput"))
        self.horizontalLayout.addWidget(self.LinkInput)
        self.SearchButton = QtGui.QPushButton(self.layoutWidget1)
        self.SearchButton.setObjectName(_fromUtf8("SearchButton"))
        self.horizontalLayout.addWidget(self.SearchButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.ChapterLinks = QtGui.QListWidget(self.layoutWidget1)
        self.ChapterLinks.setObjectName(_fromUtf8("ChapterLinks"))
        self.verticalLayout_2.addWidget(self.ChapterLinks)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.CheckAll = QtGui.QCheckBox(self.layoutWidget1)
        self.CheckAll.setTristate(False)
        self.CheckAll.setObjectName(_fromUtf8("CheckAll"))
        self.horizontalLayout_2.addWidget(self.CheckAll)
        self.CheckSelected = QtGui.QCheckBox(self.layoutWidget1)
        self.CheckSelected.setTristate(False)
        self.CheckSelected.setObjectName(_fromUtf8("CheckSelected"))
        self.horizontalLayout_2.addWidget(self.CheckSelected)
        self.DownloadButton = QtGui.QPushButton(self.layoutWidget1)
        self.DownloadButton.setObjectName(_fromUtf8("DownloadButton"))
        self.horizontalLayout_2.addWidget(self.DownloadButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addWidget(self.splitter)
        self.MainWidget.addTab(self.InfoTab, _fromUtf8(""))
        self.DownloadTab = QtGui.QWidget()
        self.DownloadTab.setObjectName(_fromUtf8("DownloadTab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.DownloadTab)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.DownloadSearchInput = QtGui.QLineEdit(self.DownloadTab)
        self.DownloadSearchInput.setObjectName(_fromUtf8("DownloadSearchInput"))
        self.horizontalLayout_3.addWidget(self.DownloadSearchInput)
        self.DownloadSearchButton = QtGui.QPushButton(self.DownloadTab)
        self.DownloadSearchButton.setObjectName(_fromUtf8("DownloadSearchButton"))
        self.horizontalLayout_3.addWidget(self.DownloadSearchButton)
        self.ResumeAllButton = QtGui.QPushButton(self.DownloadTab)
        self.ResumeAllButton.setObjectName(_fromUtf8("ResumeAllButton"))
        self.horizontalLayout_3.addWidget(self.ResumeAllButton)
        self.pushButton = QtGui.QPushButton(self.DownloadTab)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.DownloadTable = QtGui.QTableWidget(self.DownloadTab)
        self.DownloadTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.DownloadTable.setObjectName(_fromUtf8("DownloadTable"))
        self.DownloadTable.setColumnCount(0)
        self.DownloadTable.setRowCount(0)
        self.DownloadTable.verticalHeader().setVisible(False)
        self.verticalLayout_4.addWidget(self.DownloadTable)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.MainWidget.addTab(self.DownloadTab, _fromUtf8(""))
        self.OptionsTab = QtGui.QWidget()
        self.OptionsTab.setObjectName(_fromUtf8("OptionsTab"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.OptionsTab)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label = QtGui.QLabel(self.OptionsTab)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_7.addWidget(self.label)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.DirectoryInput = QtGui.QLineEdit(self.OptionsTab)
        self.DirectoryInput.setObjectName(_fromUtf8("DirectoryInput"))
        self.horizontalLayout_4.addWidget(self.DirectoryInput)
        self.DirectoryBrowse = QtGui.QPushButton(self.OptionsTab)
        self.DirectoryBrowse.setObjectName(_fromUtf8("DirectoryBrowse"))
        self.horizontalLayout_4.addWidget(self.DirectoryBrowse)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.MainWidget.addTab(self.OptionsTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.MainWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.StatusBar = QtGui.QStatusBar(MainWindow)
        self.StatusBar.setObjectName(_fromUtf8("StatusBar"))
        MainWindow.setStatusBar(self.StatusBar)

        self.retranslateUi(MainWindow)
        self.MainWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Minimal Manga Downloader", None))
        self.SearchButton.setText(_translate("MainWindow", "Search", None))
        self.CheckAll.setText(_translate("MainWindow", "Check All", None))
        self.CheckSelected.setText(_translate("MainWindow", "Check Selected", None))
        self.DownloadButton.setText(_translate("MainWindow", "Download", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.InfoTab), _translate("MainWindow", "Info", None))
        self.DownloadSearchButton.setText(_translate("MainWindow", "Search", None))
        self.ResumeAllButton.setText(_translate("MainWindow", "Resume All", None))
        self.pushButton.setText(_translate("MainWindow", "Stop All", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.DownloadTab), _translate("MainWindow", "Download", None))
        self.label.setText(_translate("MainWindow", "Directory:", None))
        self.DirectoryBrowse.setText(_translate("MainWindow", "Browse", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.OptionsTab), _translate("MainWindow", "Options", None))
