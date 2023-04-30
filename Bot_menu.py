# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BotKKOcXR.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(630, 400)
        MainWindow.setMinimumSize(QSize(630, 400))
        MainWindow.setMaximumSize(QSize(630, 400))
        MainWindow.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 630, 400))
        self.widget_2.setMinimumSize(QSize(630, 400))
        self.widget_2.setMaximumSize(QSize(630, 400))
        self.widget_2.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius:2px;\n"
"border-color: white;\n"
"font: bold 14px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(9, 9, 50, 382))
        self.widget_3.setMinimumSize(QSize(50, 0))
        self.widget_3.setMaximumSize(QSize(200, 16777215))
        self.widget_3.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius:2px;\n"
"border-color: white;\n"
"font: bold 14px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.menu_button = QPushButton(self.widget_3)
        self.menu_button.setObjectName(u"menu_button")
        self.menu_button.setGeometry(QRect(10, 10, 30, 30))
        self.menu_button.setMinimumSize(QSize(0, 30))
        self.menu_button.setMaximumSize(QSize(30, 30))
        self.menu_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_button.setFocusPolicy(Qt.NoFocus)
        self.menu_button.setContextMenuPolicy(Qt.NoContextMenu)
        self.menu_button.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius:2px;\n"
"border-color: white;\n"
"font: bold 14px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.end_button = QPushButton(self.widget_3)
        self.end_button.setObjectName(u"end_button")
        self.end_button.setGeometry(QRect(60, 80, 131, 61))
        self.end_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.end_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.start_button = QPushButton(self.widget_3)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(60, 10, 131, 61))
        self.start_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.click_button = QPushButton(self.widget_3)
        self.click_button.setObjectName(u"click_button")
        self.click_button.setGeometry(QRect(60, 150, 131, 61))
        self.click_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.click_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.click_button_3 = QPushButton(self.widget_3)
        self.click_button_3.setObjectName(u"click_button_3")
        self.click_button_3.setGeometry(QRect(60, 290, 131, 61))
        self.click_button_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.click_button_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.button_word = QPushButton(self.widget_3)
        self.button_word.setObjectName(u"button_word")
        self.button_word.setGeometry(QRect(60, 220, 131, 61))
        self.button_word.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_word.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.right_menu = QWidget(self.widget_2)
        self.right_menu.setObjectName(u"right_menu")
        self.right_menu.setGeometry(QRect(70, 9, 551, 382))
        self.right_menu.setMinimumSize(QSize(0, 0))
        self.right_menu.setMaximumSize(QSize(16777215, 5645654))
        self.right_menu.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius:2px;\n"
"border-color: white;\n"
"font: bold 14px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.verticalLayout_2 = QVBoxLayout(self.right_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.textBrowser = QTextBrowser(self.right_menu)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.textBrowser.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Nirmala UI"])
        font.setBold(True)
        font.setItalic(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.textBrowser.setFont(font)
        self.textBrowser.setTabletTracking(False)
        self.textBrowser.setFocusPolicy(Qt.NoFocus)
        self.textBrowser.setLayoutDirection(Qt.LeftToRight)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: bold 14px;")
        self.textBrowser.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.input_line_edit = QLineEdit(self.right_menu)
        self.input_line_edit.setObjectName(u"input_line_edit")
        self.input_line_edit.setMaximumSize(QSize(16777215, 30))
        self.input_line_edit.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius:2px;\n"
"border-color: white;\n"
"font: bold 14px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.input_line_edit)

        self.label_3 = QLabel(self.right_menu)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius:0px;\n"
"border-color: white;\n"
"font: bold 14px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.right_menu.raise_()
        self.widget_3.raise_()
        self.widget_word = QWidget(self.centralwidget)
        self.widget_word.setObjectName(u"widget_word")
        self.widget_word.setGeometry(QRect(50, 410, 531, 31))
        self.widget_word.setMinimumSize(QSize(0, 31))
        self.widget_word.setMaximumSize(QSize(571, 411))
        self.widget_word.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius:5px;\n"
"border-color: white;\n"
"font: bold 14px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(100, 100, 100); ;\n"
"\n"
"")
        self.button_clouse_word = QPushButton(self.widget_word)
        self.button_clouse_word.setObjectName(u"button_clouse_word")
        self.button_clouse_word.setGeometry(QRect(10, 10, 31, 31))
        self.button_clouse_word.setCursor(QCursor(Qt.PointingHandCursor))
        self.scrollArea = QScrollArea(self.widget_word)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(50, 40, 441, 301))
        self.scrollArea.setStyleSheet(u"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius:0px;\n"
"border-color: white;\n"
"font: bold 14px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(100, 100, 100); ;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 424, 636))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit_7 = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setMinimumSize(QSize(0, 150))
        self.textEdit_7.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius:5px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"color: black;\n"
"background-color: white; ;")

        self.verticalLayout.addWidget(self.textEdit_7)

        self.textEdit_6 = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setMinimumSize(QSize(0, 150))
        self.textEdit_6.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius:5px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"color: black;\n"
"background-color: white; ;")

        self.verticalLayout.addWidget(self.textEdit_6)

        self.textEdit_4 = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMinimumSize(QSize(0, 150))
        self.textEdit_4.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius:5px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"color: black;\n"
"background-color: white; ;")

        self.verticalLayout.addWidget(self.textEdit_4)

        self.textEdit_5 = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setMinimumSize(QSize(0, 150))
        self.textEdit_5.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius:5px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"color: black;\n"
"background-color: white; ;")

        self.verticalLayout.addWidget(self.textEdit_5)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.widget_word_2 = QWidget(self.centralwidget)
        self.widget_word_2.setObjectName(u"widget_word_2")
        self.widget_word_2.setGeometry(QRect(50, 450, 538, 31))
        self.widget_word_2.setMinimumSize(QSize(0, 31))
        self.widget_word_2.setMaximumSize(QSize(571, 411))
        self.widget_word_2.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius:5px;\n"
"border-color: white;\n"
"font: bold 14px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(100, 100, 100); ;\n"
"\n"
"")
        self.button_clouse_word_2 = QPushButton(self.widget_word_2)
        self.button_clouse_word_2.setObjectName(u"button_clouse_word_2")
        self.button_clouse_word_2.setGeometry(QRect(10, 10, 31, 31))
        self.button_clouse_word_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.label = QLabel(self.widget_word_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 100, 291, 21))
        self.label.setStyleSheet(u"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius:0px;\n"
"border-color: white;\n"
"font: bold 14px;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.button_ok_name = QPushButton(self.widget_word_2)
        self.button_ok_name.setObjectName(u"button_ok_name")
        self.button_ok_name.setGeometry(QRect(420, 60, 41, 31))
        self.button_ok_name.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius:2px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.input_name_lineedit = QLineEdit(self.widget_word_2)
        self.input_name_lineedit.setObjectName(u"input_name_lineedit")
        self.input_name_lineedit.setGeometry(QRect(80, 60, 341, 31))
        self.input_name_lineedit.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius:2px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"color: black;\n"
"background-color: white; ;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_button.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.end_button.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041e\u041d\u0415\u0426", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0427\u0410\u0422\u042c", None))
        self.click_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0415\u0419\u0421\u0422\u0412\u0418\u0415", None))
        self.click_button_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041f\u0420\u041e\u0421\u0418\u0422\u042c", None))
        self.button_word.setText(QCoreApplication.translate("MainWindow", u"\u0411\u041b\u0410\u041a\u041d\u041e\u0422", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Nirmala UI'; font-size:14px; font-weight:700; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u043c\u0430\u043d\u0434\u044b - \u0443\u0437\u043d\u0430\u0442\u044c \u0447\u0442\u043e \u043e\u043d\u043e \u043c\u043e\u0436\u0435\u0442", None))
        self.button_clouse_word.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_clouse_word_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0410\u041a \u0416\u0415 \u0412\u0410\u0421 \u041d\u0410\u0417\u042b\u0412\u0410\u0422\u042c \u0414\u041e\u0420\u041e\u0413\u041e\u0419 \u0414\u0420\u0423\u0413", None))
        self.button_ok_name.setText(QCoreApplication.translate("MainWindow", u"OK", None))
    # retranslateUi

