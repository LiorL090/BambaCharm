# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CodeHeaven.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import re
import subprocess
import socket
import pickle

from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.manager import QtKernelManager

# colors
yellow = "rgb(155, 140, 30)"
green = "rgb(115, 198, 118)"
blue = "rgb(37, 31, 155)"
red = "rgb(188, 84, 84)"
purple = "rgb(97, 74, 232)"
_translate = QtCore.QCoreApplication.translate


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """Sets the basics frames and widgets loads the icons and actions"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(995, 760)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/ide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        # menu bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        # self.menuSettings = QtWidgets.QMenu(self.menubar)
        # self.menuSettings.setObjectName("menuSettings")
        #
        # self.menuEdit = QtWidgets.QMenu(self.menubar)
        # self.menuEdit.setObjectName("menuEdit")

        self.menuUser = QtWidgets.QMenu(self.menubar)
        self.menuUser.setObjectName("menuUser")

        MainWindow.setMenuBar(self.menubar)
        # ber with basic operations
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        # actions that appears in the bars
        # self.actionNew = QtWidgets.QAction(MainWindow)
        # icon1 = QtGui.QIcon()
        # icon1.addPixmap(QtGui.QPixmap("icons/new file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.actionNew.setIcon(icon1)
        # self.actionNew.setObjectName("actionNew")

        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setObjectName("actionOpen")

        self.actionSave = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/Save-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSave")

        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/Save-as-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon8)
        self.actionSaveAs.setObjectName("actionSaveAs")

        self.actionNew_Text_File = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/newText.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Text_File.setIcon(icon4)
        self.actionNew_Text_File.setObjectName("actionNew_Text_File")

        self.actioncmd = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/cmd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncmd.setIcon(icon5)
        self.actioncmd.setObjectName("actioncmd")

        self.actionpython = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionpython.setIcon(icon6)
        self.actionpython.setObjectName("actionpython")

        self.actionGoogle = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/google.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoogle.setIcon(icon7)
        self.actionGoogle.setObjectName("actionGoogle")

        self.actionLogIn = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogIn.setIcon(icon8)
        self.actionLogIn.setObjectName("actionLogIn")

        self.actionSignIn = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/signin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSignIn.setIcon(icon9)
        self.actionSignIn.setObjectName("actionSignIn")

        self.actionLogOut = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogOut.setIcon(icon10)
        self.actionLogOut.setObjectName("actionLogOut")

        self.actionDelete = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon11)
        self.actionDelete.setObjectName("actionDelete")

        self.actionMyFiles = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/cloud.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMyFiles.setIcon(icon12)
        self.actionMyFiles.setObjectName("actionMyFiles")

        # add actions to the bars
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)

        self.menuUser.addAction(self.actionLogIn)
        self.menuUser.addAction(self.actionSignIn)

        self.menubar.addAction(self.menuFile.menuAction())
        # self.menubar.addAction(self.menuSettings.menuAction())
        # self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuUser.menuAction())
        # self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionpython)
        self.toolBar.addAction(self.actionNew_Text_File)
        self.toolBar.addAction(self.actioncmd)
        self.toolBar.addAction(self.actionGoogle)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """Sets titles and connects the buttons and actions to their functions"""
        MainWindow.setWindowTitle(_translate("MainWindow", "BambaCharm"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuUser.setTitle(_translate("MainWindow", "Bamba Cloud"))
        # self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        # self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        # self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As"))
        self.actionNew_Text_File.setText(_translate("MainWindow", "New Text File"))
        self.actioncmd.setText(_translate("MainWindow", "cmd"))
        self.actionpython.setText(_translate("MainWindow", "python"))
        self.actionGoogle.setText(_translate("MainWindow", "Google"))
        self.actionLogIn.setText(_translate("MainWindow", "Login"))
        self.actionSignIn.setText(_translate("MainWindow", "Sign In"))
        self.actionLogOut.setText(_translate("MainWindow", "Log out"))
        self.actionDelete.setText(_translate("MainWindow", "Delete account"))
        self.actionMyFiles.setText(_translate("MainWindow", "My files"))

        self.tabWidget.tabCloseRequested.connect(self.close_my_tab)
        self.actionpython.triggered.connect(self.add_python_tab)
        self.actioncmd.triggered.connect(self.add_cmd_tab)
        self.actionGoogle.triggered.connect(self.add_google_tab)
        self.actionNew_Text_File.triggered.connect(self.add_text_tab)
        self.actionSaveAs.triggered.connect(self.save_as_clicked)
        self.actionSave.triggered.connect(self.save_clicked)
        self.actionOpen.triggered.connect(self.open_clicked)
        self.actionLogIn.triggered.connect(self.login_clicked)
        self.actionSignIn.triggered.connect(self.signin_clicked)
        self.actionLogOut.triggered.connect(self.logout_clicked)
        self.actionDelete.triggered.connect(self.delete_clicked)
        self.actionMyFiles.triggered.connect(self.myfiles_clicked)

    def close_my_tab(self, n):
        """Closes the tab"""
        widget = self.tabWidget.currentWidget()
        if widget.objectName() == "python_tab":
            widget.jupyter_widget.kernel_client.stop_channels()
            widget.jupyter_widget.kernel_manager.shutdown_kernel()
        self.tabWidget.removeTab(n)

    def make_jupyter_widget_with_kernel(self):
        """Start a kernel, connect to it, and create a RichJupyterWidget to use it
        """
        USE_KERNEL = 'python3'
        kernel_manager = QtKernelManager(kernel_name=USE_KERNEL)
        kernel_manager.start_kernel()

        kernel_client = kernel_manager.client()
        kernel_client.start_channels()

        jupyter_widget = RichJupyterWidget()
        jupyter_widget.kernel_manager = kernel_manager
        jupyter_widget.kernel_client = kernel_client
        jupyter_widget._display_banner = False
        return jupyter_widget

    def add_python_tab(self):
        """Adds python tab to the tabWidget"""
        self.tab_python = QtWidgets.QWidget()
        self.tab_python.setObjectName("python_tab")
        self.tab_python.setStyleSheet("background-color: rgb(64, 72, 80);")
        self.tab_python.savable = True
        self.tab_python.path = ""
        self.tab_python.file_name = "Python"
        self.tab_python.verticalLayout = QtWidgets.QVBoxLayout(self.tab_python)
        self.tab_python.verticalLayout.setObjectName("verticalLayout")
        self.tab_python.textEdit = QtWidgets.QTextEdit(self.tab_python)
        self.tab_python.textEdit.setMinimumSize(QtCore.QSize(0, 251))
        self.tab_python.textEdit.setObjectName("plainTextEdit")
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setStyleHint(QtGui.QFont.Monospace)
        font.setFixedPitch(True)
        font.setPointSize(10)
        metrics = QtGui.QFontMetrics(font)
        self.tab_python.textEdit.setTabStopWidth(4 * metrics.width(' '))
        self.tab_python.textEdit.setFont(font)
        self.tab_python.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tab_python.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.tab_python.textEdit.setStyleSheet(
            "border-radius: 10px; border: 1px solid #cdcdcd; border-color: %s; font-size: 12pt; color: white; background-color: rgb(34, 34, 34);" % blue)
        self.tab_python.verticalLayout.addWidget(self.tab_python.textEdit)
        self.tab_python.horizontalLayout = QtWidgets.QHBoxLayout()
        self.tab_python.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.tab_python.horizontalLayout.setObjectName("horizontalLayout")
        self.tab_python.playButton = QtWidgets.QPushButton(self.tab_python)
        self.tab_python.playButton.setAutoFillBackground(False)
        self.tab_python.playButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/playNoBack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_python.playButton.setIcon(icon)
        self.tab_python.playButton.setIconSize(QtCore.QSize(25, 25))
        self.tab_python.playButton.setFlat(True)
        self.tab_python.playButton.setObjectName("pushButton_2")
        self.tab_python.horizontalLayout.addWidget(self.tab_python.playButton)
        self.tab_python.stopButton = QtWidgets.QPushButton(self.tab_python)
        self.tab_python.stopButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_python.stopButton.setIcon(icon1)
        self.tab_python.stopButton.setIconSize(QtCore.QSize(25, 25))
        self.tab_python.stopButton.setFlat(True)
        self.tab_python.stopButton.setObjectName("pushButton")
        self.tab_python.horizontalLayout.addWidget(self.tab_python.stopButton)
        self.tab_python.verticalLayout.addLayout(self.tab_python.horizontalLayout)
        self.tab_python.jupyter_widget = self.make_jupyter_widget_with_kernel()
        self.tab_python.jupyter_widget.setMaximumSize(QtCore.QSize(16777215, 192))
        self.tab_python.verticalLayout.addWidget(self.tab_python.jupyter_widget)
        self.tabWidget.addTab(self.tab_python, "Python")
        self.tab_python.playButton.clicked.connect(self.python_run_clicked)
        self.tab_python.stopButton.clicked.connect(self.python_stop_clicked)
        return self.tab_python

    def add_cmd_commands_tab(self):
        """Adds cmd commands tab to the tabWidget"""
        self.cmd_commands_tab = QtWidgets.QWidget()
        self.cmd_commands_tab.setObjectName("cmd_commands_tab")
        self.cmd_commands_tab.savable = False
        self.cmd_commands_tab.gridLayout = QtWidgets.QGridLayout(self.cmd_commands_tab)
        self.cmd_commands_tab.gridLayout.setObjectName("gridLayout_2")
        self.cmd_commands_tab.textBrowser = QtWidgets.QTextBrowser(self.cmd_commands_tab)
        self.cmd_commands_tab.textBrowser.setObjectName("textEdit")
        self.cmd_commands_tab.gridLayout.addWidget(self.cmd_commands_tab.textBrowser, 0, 0, 1, 1)
        self.tabWidget.addTab(self.cmd_commands_tab, "cmd commands")
        cmd_table = open("cmd_table.html", "r").read()
        self.cmd_commands_tab.textBrowser.setHtml(_translate("MainWindow", cmd_table))

        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setStyleHint(QtGui.QFont.Monospace)
        font.setFixedPitch(True)
        font.setPointSize(14)
        self.cmd_commands_tab.textBrowser.setFont(font)

    def add_google_tab(self):
        """Adds google tab to the tabWidget"""
        self.google_tab = QtWidgets.QWidget()
        self.google_tab.setObjectName("google_tab")
        self.google_tab.savable = False
        self.google_tab.gridLayout = QtWidgets.QGridLayout(self.google_tab)
        self.google_tab.gridLayout.setObjectName("gridLayout_4")
        self.google_tab.browser = QtWebEngineWidgets.QWebEngineView(self.google_tab)
        self.google_tab.browser.setObjectName("google")
        self.google_tab.gridLayout.addWidget(self.google_tab.browser, 0, 0, 1, 1)
        self.tabWidget.addTab(self.google_tab, "Google")
        self.google_tab.browser.setUrl(QtCore.QUrl("https://google.com"))

    def add_text_tab(self):
        """Adds text tab to the tabWidget"""
        self.text_tab = QtWidgets.QWidget()
        self.text_tab.setObjectName("text_tab")
        self.text_tab.savable = True
        self.text_tab.path = ""
        self.text_tab.file_name = "Text"
        self.text_tab.setStyleSheet("background-color: rgb(64, 72, 80);")
        self.text_tab.gridLayout = QtWidgets.QGridLayout(self.text_tab)
        self.text_tab.gridLayout.setObjectName("gridLayout_3")
        self.text_tab.textEdit = QtWidgets.QTextEdit(self.text_tab)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setStyleHint(QtGui.QFont.Monospace)
        font.setFixedPitch(True)
        font.setPointSize(10)
        metrics = QtGui.QFontMetrics(font)
        self.text_tab.textEdit.setTabStopWidth(4 * metrics.width(' '))
        self.text_tab.textEdit.setFont(font)
        self.text_tab.textEdit.setStyleSheet(
            "border-radius: 10px; border: 1px solid #cdcdcd; border-color: %s; font-size: 12pt; color: white; background-color: rgb(34, 34, 34);" % yellow)
        self.text_tab.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_tab.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text_tab.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.text_tab.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.text_tab.textEdit.setObjectName("plainTextEdit")
        self.text_tab.gridLayout.addWidget(self.text_tab.textEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.text_tab, "Text")
        return self.text_tab

    def add_cmd_tab(self):
        """Adds cmd tab to the tabWidget"""
        self.cmd_tab = QtWidgets.QWidget()
        self.cmd_tab.setObjectName("cmd_tab")
        self.cmd_tab.savable = False
        self.cmd_tab.setStyleSheet("background-color: rgb(64, 72, 80);")
        self.cmd_tab.verticalLayout = QtWidgets.QVBoxLayout(self.cmd_tab)
        self.cmd_tab.verticalLayout.setObjectName("gridLayout_3")
        self.cmd_tab.textEdit = QtWidgets.QTextEdit(self.cmd_tab)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setStyleHint(QtGui.QFont.Monospace)
        font.setFixedPitch(True)
        font.setPointSize(10)
        metrics = QtGui.QFontMetrics(font)
        self.cmd_tab.textEdit.setTabStopWidth(4 * metrics.width(' '))
        self.cmd_tab.textEdit.setFont(font)
        self.cmd_tab.textEdit.setStyleSheet(
            "border-radius: 10px; border: 1px solid #cdcdcd; border-color: %s; font-size: 8pt; color: white; background-color: rgb(34, 34, 34);" % purple)
        self.cmd_tab.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cmd_tab.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cmd_tab.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.cmd_tab.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.cmd_tab.textEdit.setObjectName("plainTextEdit")
        self.cmd_tab.textEdit.setReadOnly(True)
        # self.plainTextEdit5.addAction(self.action_enter_pressed)
        self.cmd_tab.textEditCommands = QtWidgets.QTextEdit(self.cmd_tab)
        self.cmd_tab.textEditCommands.setTabStopWidth(4 * metrics.width(' '))
        self.cmd_tab.textEditCommands.setFont(font)
        self.cmd_tab.textEditCommands.setStyleSheet(
            "border-radius: 10px; border: 1px solid #cdcdcd; border-color: %s; font-size: 12pt; color: white; background-color: rgb(34, 34, 34);" % red)
        self.cmd_tab.textEditCommands.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cmd_tab.textEditCommands.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cmd_tab.textEditCommands.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.cmd_tab.textEditCommands.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.cmd_tab.textEditCommands.setObjectName("plainTextEdit")
        self.cmd_tab.textEditCommands.setMaximumSize(QtCore.QSize(16777215, 30))
        self.cmd_tab.textEditCommands.keyPressEvent = self.enter_clicked

        self.cmd_tab.verticalLayout.addWidget(self.cmd_tab.textEdit)
        self.cmd_tab.verticalLayout.addWidget(self.cmd_tab.textEditCommands)
        self.tabWidget.addTab(self.cmd_tab, "cmd")
        self.add_cmd_commands_tab()

    def enter_clicked(self, qKeyEvent):
        widget = self.tabWidget.currentWidget()
        """What happens when enter key is clicked"""
        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            self.run_cmd_command()

            qKeyEvent.accept()
            return
        else:
            qKeyEvent.ignore()
            return QtWidgets.QTextEdit.keyPressEvent(widget.textEditCommands, qKeyEvent)

    def run_cmd_command(self):
        try:
            widget = self.tabWidget.currentWidget()
            command = widget.textEditCommands.toPlainText()
            p = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT,
                                 shell=True)
            output = p.communicate()[0].decode('utf-8')
            text = widget.textEdit.toPlainText() + "\n>>>" + command + "\n" + output
            widget.textEdit.setPlainText(text)
            widget.textEditCommands.setPlainText("")
        except:
            pass

    def save_as_clicked(self):
        """Save as button is clicked"""
        widget = self.tabWidget.currentWidget()
        if widget is not None:
            if widget.savable:
                if widget.objectName() == "text_tab":
                    ending = ".txt"
                    not_end_with = ".py"
                else:
                    ending = ".py"
                    not_end_with = ".txt"
                name = QtWidgets.QFileDialog.getSaveFileName(caption="Save File", filter="Text files (*%s)" % ending)
                if name:
                    widget.path = name[0].replace(not_end_with, ending)
                    try:
                        match = re.search(r'/([\w -]+%s)' % ending, widget.path)
                        if match:
                            widget.file_name = match.group(1)
                        file = open(widget.path, 'w')
                        text = widget.textEdit.toPlainText()
                        file.write(text)
                        file.close()
                        self.tabWidget.setTabText(self.tabWidget.indexOf(widget),
                                                  _translate("MainWindow", widget.file_name))
                    except:
                        pass

    def save_clicked(self):
        """Save button is clicked"""
        widget = self.tabWidget.currentWidget()
        if widget is not None:
            if widget.savable:
                try:
                    file = open(widget.path, 'w')
                    text = widget.textEdit.toPlainText()
                    file.write(text)
                    file.close()
                except:
                    pass

    def open_clicked(self):
        """Open button is clicked"""
        name = QtWidgets.QFileDialog.getOpenFileName(caption="Choose File", filter="Text files (*.py *.txt)")
        if name:
            path = name[0]
            try:
                if path.endswith(".py"):
                    tab = self.add_python_tab()
                    tab.path = path
                    ending = ".py"
                    match = re.search(r'/([\w -]+%s)' % ending, path)
                    if match:
                        tab.file_name = match.group(1)
                    self.tabWidget.setTabText(self.tabWidget.indexOf(tab),
                                              _translate("MainWindow", tab.file_name))
                    file = open(path, 'r')
                    text = file.read()
                    tab.textEdit.setPlainText(text)
                    file.close()
                else:
                    tab = self.add_text_tab()
                    tab.path = path
                    ending = ".txt"
                    match = re.search(r'/([\w -]+%s)' % ending, path)
                    if match:
                        tab.file_name = match.group(1)
                    self.tabWidget.setTabText(self.tabWidget.indexOf(tab),
                                              _translate("MainWindow", tab.file_name))
                    file = open(path, 'r')
                    text = file.read()
                    tab.textEdit.setPlainText(text)
                    file.close()

            except:
                pass

    def python_run_clicked(self):
        """run button in python tab clicked"""
        widget = self.tabWidget.currentWidget()
        command = "run " + widget.path
        if widget.path == "":
            command = "Make sure you have saved the script file"
        widget.jupyter_widget.execute(source=command)

    def python_stop_clicked(self):
        """run button in python tab clicked"""
        widget = self.tabWidget.currentWidget()
        widget.jupyter_widget.reset("")

    def login_widget_create(self):
        """Creates login widget"""
        self.login_widget = QtWidgets.QWidget()
        self.login_widget.verticalLayout = QtWidgets.QVBoxLayout(self.login_widget)
        self.login_widget.setFixedSize(QtCore.QSize(300, 300))
        self.login_widget.setWindowTitle(_translate("MainWindow", "Login"))
        self.login_widget.setAutoFillBackground(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_widget.setWindowIcon(icon8)

        oImage = QtGui.QImage("icons\login_back.png")
        sImage = oImage.scaled(QtCore.QSize(300, 300))  # resize Image to widgets size
        palette = QtGui.QPalette()
        palette.setBrush(10, QtGui.QBrush(sImage))  # 10 = Windowrole
        self.login_widget.setPalette(palette)

        self.login_widget.label = QtWidgets.QLabel(self.login_widget)
        self.login_widget.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.login_widget.label.setText("Login please")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login_widget.label.setFont(font)

        self.login_widget.hLayout1 = QtWidgets.QHBoxLayout()
        self.login_widget.lineEditUser = QtWidgets.QLineEdit()
        self.login_widget.labelU = QtWidgets.QLabel()
        self.login_widget.labelU.setMaximumSize(QtCore.QSize(50, 20))
        self.login_widget.labelU.setText("Username:")
        self.login_widget.hLayout1.addWidget(self.login_widget.labelU)
        self.login_widget.hLayout1.addWidget(self.login_widget.lineEditUser)

        self.login_widget.hLayout2 = QtWidgets.QHBoxLayout()
        self.login_widget.lineEditPass = QtWidgets.QLineEdit()
        self.login_widget.labelP = QtWidgets.QLabel()
        self.login_widget.labelP.setMaximumSize(QtCore.QSize(50, 20))
        self.login_widget.labelP.setText("Password:")
        self.login_widget.hLayout2.addWidget(self.login_widget.labelP)
        self.login_widget.hLayout2.addWidget(self.login_widget.lineEditPass)

        self.login_widget.button = QtWidgets.QPushButton(self.login_widget)
        self.login_widget.button.setText("Login")
        self.login_widget.button.clicked.connect(self.login_to_server)

        self.login_widget.verticalLayout.addWidget(self.login_widget.label)
        self.login_widget.verticalLayout.addLayout(self.login_widget.hLayout1)
        self.login_widget.verticalLayout.addLayout(self.login_widget.hLayout2)
        self.login_widget.verticalLayout.addWidget(self.login_widget.button)

        return self.login_widget

    def login_clicked(self):
        """when login button clicked open the login widget"""
        widget = self.login_widget_create()
        widget.show()

    def login_to_server(self):
        """when user want to log in to server send request to server"""
        try:
            username = self.login_widget.lineEditUser.text()
            password = self.login_widget.lineEditPass.text()
            message = "old_user " + username + " " + password
            self.my_socket = socket.socket()
            self.my_socket.connect(("127.0.0.1", 8820))
            self.my_socket.send(message.encode('utf-8'))
            data = self.my_socket.recv(1024)
            data = data.decode('utf-8')
            self.login_widget.label.setText(data)
            if data == "successful login":
                self.login_widget.close()
                self.menuUser.removeAction(self.actionLogIn)
                self.menuUser.removeAction(self.actionSignIn)
                self.menuUser.addAction(self.actionMyFiles)
                self.menuUser.addSeparator()
                self.menuUser.addAction(self.actionLogOut)
                self.menuUser.addAction(self.actionDelete)
        except:
            self.login_widget.label.setText("Server is not responding")

    def logout_clicked(self):
        """when user wants to disconnect"""
        try:
            message = "req logout"
            self.my_socket.send(message.encode('utf-8'))
        except:
            pass
        self.menuUser.removeAction(self.actionMyFiles)
        self.menuUser.removeAction(self.actionLogOut)
        self.menuUser.removeAction(self.actionDelete)
        self.menuUser.addAction(self.actionLogIn)
        self.menuUser.addAction(self.actionSignIn)

    def signin_widget_create(self):
        """Creates sign in widget"""
        self.signin_widget = QtWidgets.QWidget()
        self.signin_widget.verticalLayout = QtWidgets.QVBoxLayout(self.signin_widget)
        self.signin_widget.setFixedSize(QtCore.QSize(300, 300))
        self.signin_widget.setWindowTitle(_translate("MainWindow", "Sign In"))
        self.signin_widget.setAutoFillBackground(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/signin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.signin_widget.setWindowIcon(icon9)

        oImage = QtGui.QImage("icons\signin_back.jpg")
        sImage = oImage.scaled(QtCore.QSize(300, 300))  # resize Image to widgets size
        palette = QtGui.QPalette()
        palette.setBrush(10, QtGui.QBrush(sImage))  # 10 = Windowrole
        self.signin_widget.setPalette(palette)

        self.signin_widget.label = QtWidgets.QLabel(self.signin_widget)
        self.signin_widget.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.signin_widget.label.setText("Login please")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.signin_widget.label.setFont(font)

        self.signin_widget.hLayout1 = QtWidgets.QHBoxLayout()
        self.signin_widget.lineEditUser = QtWidgets.QLineEdit()
        self.signin_widget.labelU = QtWidgets.QLabel()
        self.signin_widget.labelU.setMaximumSize(QtCore.QSize(50, 20))
        self.signin_widget.labelU.setText("Username:")
        self.signin_widget.hLayout1.addWidget(self.signin_widget.labelU)
        self.signin_widget.hLayout1.addWidget(self.signin_widget.lineEditUser)

        self.signin_widget.hLayout2 = QtWidgets.QHBoxLayout()
        self.signin_widget.lineEditPass = QtWidgets.QLineEdit()
        self.signin_widget.labelP = QtWidgets.QLabel()
        self.signin_widget.labelP.setMaximumSize(QtCore.QSize(50, 20))
        self.signin_widget.labelP.setText("Password:")
        self.signin_widget.hLayout2.addWidget(self.signin_widget.labelP)
        self.signin_widget.hLayout2.addWidget(self.signin_widget.lineEditPass)

        self.signin_widget.hLayout3 = QtWidgets.QHBoxLayout()
        self.signin_widget.lineEditEmail = QtWidgets.QLineEdit()
        self.signin_widget.labelE = QtWidgets.QLabel()
        self.signin_widget.labelE.setMaximumSize(QtCore.QSize(50, 20))
        self.signin_widget.labelE.setText("Password:")
        self.signin_widget.hLayout3.addWidget(self.signin_widget.labelE)
        self.signin_widget.hLayout3.addWidget(self.signin_widget.lineEditEmail)

        self.signin_widget.button = QtWidgets.QPushButton(self.signin_widget)
        self.signin_widget.button.setText("Login")
        self.signin_widget.button.clicked.connect(self.signin_to_server)

        self.signin_widget.verticalLayout.addWidget(self.signin_widget.label)
        self.signin_widget.verticalLayout.addLayout(self.signin_widget.hLayout1)
        self.signin_widget.verticalLayout.addLayout(self.signin_widget.hLayout2)
        self.signin_widget.verticalLayout.addLayout(self.signin_widget.hLayout3)
        self.signin_widget.verticalLayout.addWidget(self.signin_widget.button)

        return self.signin_widget

    def signin_clicked(self):
        """when sign in button clicked open the login widget"""
        widget = self.signin_widget_create()
        widget.show()

    def signin_to_server(self):
        """when user want to sign in to server send request to server"""
        try:
            username = self.signin_widget.lineEditUser.text()
            password = self.signin_widget.lineEditPass.text()
            email = self.signin_widget.lineEditEmail.text()
            message = "new_user " + username + " " + password + " " + email
            self.my_socket = socket.socket()
            self.my_socket.connect(("127.0.0.1", 8820))
            self.my_socket.send(message.encode('utf-8'))
            data = self.my_socket.recv(1024)
            data = data.decode('utf-8')
            self.signin_widget.label.setText(data)
            if data == "successful registration":
                self.signin_widget.close()
                self.menuUser.removeAction(self.actionLogIn)
                self.menuUser.removeAction(self.actionSignIn)
                self.menuUser.addAction(self.actionMyFiles)
                self.menuUser.addSeparator()
                self.menuUser.addAction(self.actionLogOut)
                self.menuUser.addAction(self.actionDelete)
        except:
            self.signin_widget.label.setText("Server is not responding")

    def delete_clicked(self):
        """when delete is clicked"""
        widget = self.create_confirmation_widget()
        widget.show()

    def delete_account(self):
        """when user wants to delete his account"""
        try:
            message = "req delete"
            self.my_socket.send(message.encode('utf-8'))
        except:
            pass
        self.confirmation_widget.close()
        self.menuUser.removeAction(self.actionMyFiles)
        self.menuUser.removeAction(self.actionLogOut)
        self.menuUser.removeAction(self.actionDelete)
        self.menuUser.addAction(self.actionLogIn)
        self.menuUser.addAction(self.actionSignIn)

    def create_confirmation_widget(self):
        """Creates confirmation widget"""
        self.confirmation_widget = QtWidgets.QWidget()
        self.confirmation_widget.verticalLayout = QtWidgets.QVBoxLayout(self.confirmation_widget)
        self.confirmation_widget.setFixedSize(QtCore.QSize(400, 100))
        self.confirmation_widget.setWindowTitle(_translate("MainWindow", "Confirm deletion"))
        self.confirmation_widget.setAutoFillBackground(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.confirmation_widget.setWindowIcon(icon11)

        self.confirmation_widget.label = QtWidgets.QLabel(self.confirmation_widget)
        self.confirmation_widget.label.setText("Are you sure you want to delete your Bambacharm account?")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confirmation_widget.label.setFont(font)

        self.confirmation_widget.hLayout1 = QtWidgets.QHBoxLayout()
        self.confirmation_widget.button_yes = QtWidgets.QPushButton(self.confirmation_widget)
        self.confirmation_widget.button_yes.setText("Yes")
        self.confirmation_widget.button_yes.clicked.connect(self.delete_account)
        self.confirmation_widget.button_no = QtWidgets.QPushButton(self.confirmation_widget)
        self.confirmation_widget.button_no.setText("No")
        self.confirmation_widget.button_no.clicked.connect(self.confirmation_denied)
        self.confirmation_widget.hLayout1.addWidget(self.confirmation_widget.button_yes)
        self.confirmation_widget.hLayout1.addWidget(self.confirmation_widget.button_no)

        self.confirmation_widget.verticalLayout.addWidget(self.confirmation_widget.label)
        self.confirmation_widget.verticalLayout.addLayout(self.confirmation_widget.hLayout1)

        return self.confirmation_widget

    def confirmation_denied(self):
        """user clicks no and don't confirm his action"""
        self.confirmation_widget.close()

    def myfiles_clicked(self):
        """creates window with list of all storage files"""
        widget = self.create_myfiles_widget()
        widget.show()

    def get_files_list(self):
        try:
            message = "req listDir"
            self.my_socket.send(message.encode('utf-8'))
            data = self.my_socket.recv(1024)
            data = pickle.loads(data)
            return data
        except:
            pass
        return []

    def create_myfiles_widget(self):
        """Creates myfiles widget"""
        files_list = self.get_files_list()

        self.myfiles_widget = QtWidgets.QWidget()
        self.myfiles_widget.verticalLayout = QtWidgets.QVBoxLayout(self.myfiles_widget)
        self.myfiles_widget.setFixedSize(QtCore.QSize(200, 300))
        self.myfiles_widget.setWindowTitle(_translate("MainWindow", "Confirm deletion"))
        self.myfiles_widget.setAutoFillBackground(True)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/cloud.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.myfiles_widget.setWindowIcon(icon12)

        self.myfiles_widget.list = QtWidgets.QListWidget(self.myfiles_widget)
        self.myfiles_widget.list.setStyleSheet("background-color: rgb(224, 155, 76);")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.myfiles_widget.list.setFont(font)
        for item in files_list:
            self.myfiles_widget.list.addItem(str(item))

        self.myfiles_widget.hLayout1 = QtWidgets.QHBoxLayout()
        self.myfiles_widget.button_open = QtWidgets.QPushButton(self.myfiles_widget)
        self.myfiles_widget.button_open.setText("Open")
        self.myfiles_widget.button_open.clicked.connect(self.open_server_file)
        self.myfiles_widget.button_delete = QtWidgets.QPushButton(self.myfiles_widget)
        self.myfiles_widget.button_delete.setText("Delete")
        self.myfiles_widget.button_delete.clicked.connect(self.delete_server_file)
        self.myfiles_widget.hLayout1.addWidget(self.myfiles_widget.button_open)
        self.myfiles_widget.hLayout1.addWidget(self.myfiles_widget.button_delete)

        self.myfiles_widget.verticalLayout.addWidget(self.myfiles_widget.list)
        self.myfiles_widget.verticalLayout.addLayout(self.myfiles_widget.hLayout1)

        return self.myfiles_widget

    def open_server_file(self):
        """send request to server to get certain file"""
        item = self.myfiles_widget.list.selectedItems()
        if len(item) != 0:
            file_name = item[0].text()

    def delete_server_file(self):
        """send request to server to delete certain file"""
        try:
            items = self.myfiles_widget.list.selectedItems()
            if items:
                for item in items:
                    file_name = item.text()
                    self.myfiles_widget.list.takeItem(self.myfiles_widget.list.row(item))
                    message = "req deleteFile " + file_name
                    self.my_socket.send(message.encode('utf-8'))
        except:
            pass




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
