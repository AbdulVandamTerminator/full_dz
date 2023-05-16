
import sys
import time
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QFile, QRect
from PySide6 import QtCore
from Bot_menu import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.start_conversation = False
        self.user_name = '... а я незнаю как вас называть ('

        self.ui.menu_button.clicked.connect(self.menu_open)
        self.ui.start_button.clicked.connect(self.start_func)
        self.ui.end_button.clicked.connect(self.end_the_conversation)
        self.ui.button_word.clicked.connect(self.open_word)
        self.ui.button_clouse_word.clicked.connect(self.close_word)
        self.ui.click_button_3.clicked.connect(self.question)
        self.ui.button_clouse_word_2.clicked.connect(self.name_close)
        self.ui.button_ok_name.clicked.connect(self.input_name)
        self.ui.button_clouse_word_3.clicked.connect(self.clicker_close)
        self.ui.klick_button.clicked.connect(self.in_clicker)

    def add_word(self):
        return


    def menu_open(self):
        """
        выдвегает меню и двигает правый виджет
        :return:
        """
        self.animation_menu = QtCore.QPropertyAnimation(self.ui.widget_3, b"geometry")
        self.animation_right_menu = QtCore.QPropertyAnimation(self.ui.right_menu, b"geometry")
        self.ui.widget_3.show()

        if self.ui.widget_3.width() == 50:
            self.animation_right_menu.setDuration(400)
            self.animation_right_menu.setStartValue((QRect(70, 10, 550, 380)))
            self.animation_right_menu.setEndValue((QRect(220, 10, 400, 380)))
            self.animation_right_menu.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
            self.animation_right_menu.start()
            self.animation_menu.setDuration(400)
            self.animation_menu.setStartValue(QRect(10, 15, 50, 383))
            self.animation_menu.setEndValue((QRect(10, 10, 200, 383)))
            self.animation_menu.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
            self.animation_menu.start()
        else:
            self.animation_right_menu.setDuration(400)
            self.animation_right_menu.setStartValue((QRect(220, 10, 400, 380)))
            self.animation_right_menu.setEndValue((QRect(70, 10, 550, 380)))
            self.animation_right_menu.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
            self.animation_right_menu.start()
            self.animation_menu.setDuration(400)
            self.animation_menu.setStartValue(QRect(10, 15, 200, 383))
            self.animation_menu.setEndValue((QRect(10, 10, 50, 383)))
            self.animation_menu.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
            self.animation_menu.start()


    def name_open(self):
        '''
        открывает окошко ввода имени
        :return:
        '''
        self.animation_menu_name = QtCore.QPropertyAnimation(self.ui.widget_word_2, b"geometry")
        self.animation_menu_name.setDuration(400)
        self.animation_menu_name.setStartValue((QRect(100, 571, 571, 31)))
        self.animation_menu_name.setEndValue((QRect(30, 30, 571, 411)))
        self.animation_menu_name.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation_menu_name.start()


    def name_close(self):
        '''
        закрывает окошко ввода имени
        :return:
        '''
        self.animation_menu_name = QtCore.QPropertyAnimation(self.ui.widget_word_2, b"geometry")
        self.animation_menu_name.setDuration(400)
        self.animation_menu_name.setStartValue(QRect(30, 30, 571, 411))
        self.animation_menu_name.setEndValue((QRect(100, 571, 571, 31)))
        self.animation_menu_name.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation_menu_name.start()



    def clicker_open(self):
        '''
        открывает окошко игры
        :return:
        '''
        self.animation_menu_klicker = QtCore.QPropertyAnimation(self.ui.klicker_widget, b"geometry")
        self.animation_menu_klicker.setDuration(400)
        self.animation_menu_klicker.setStartValue((QRect(100, 531, 531, 31)))
        self.animation_menu_klicker.setEndValue((QRect(30, 30, 531, 491)))
        self.animation_menu_klicker.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation_menu_klicker.start()
        print('окошко с игрой открыто')


    def clicker_close(self):
        '''
        закрывает окошко ввода имени
        :return:
        '''
        self.animation_menu_name = QtCore.QPropertyAnimation(self.ui.klicker_widget, b"geometry")
        self.animation_menu_name.setDuration(400)
        self.animation_menu_name.setStartValue(QRect(30, 30, 531, 491))
        self.animation_menu_name.setEndValue((QRect(100, 531, 531, 31)))
        self.animation_menu_name.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation_menu_name.start()


    def in_clicker(self):
        global count
        count = 5
        count += count * 5
        print(count)
        return self.ui.input_klicker_lable.setText(str(count))
    #пока неполноценно работает, я бы даже скозал не работает

    def question(self):
        '''
        команды на которые можно ответить
        :return:
        '''
        text_in_user_text = self.ui.input_line_edit.text()
        if 'Блокнот' in text_in_user_text\
            or 'блокнот' in text_in_user_text\
            or 'word' in text_in_user_text\
            or 'Word' in text_in_user_text\
            or 'Words' in text_in_user_text\
            or 'открой блакнот' in text_in_user_text\
            or 'Открой блакнот' in text_in_user_text\
            or 'jnrhjq ,kfryjn' in text_in_user_text\
            or 'блакнот' in text_in_user_text\
            or 'Блакнот' in text_in_user_text:
            return self.open_word()

        if 'привет' in text_in_user_text\
                or 'Привет' in text_in_user_text\
                or 'привет' in text_in_user_text\
                or 'хай' in text_in_user_text\
                or 'здарова' in text_in_user_text\
                or 'ку' in text_in_user_text:
            self.start_conversation = True
            return self.start_func()

        if 'Завершить' in text_in_user_text\
            or 'завершить' in text_in_user_text\
            or 'пока' in text_in_user_text\
            or 'Пока' in text_in_user_text:
            self.start_conversation = False
            print('завершено')
            return self.ui.textBrowser.setText('Завершено')

        if 'время' in text_in_user_text\
                or 'Время' in text_in_user_text\
                or 'Сколько времени' in text_in_user_text\
                or 'подскажи время' in text_in_user_text\
                or 'Подскажи время' in text_in_user_text\
                or 'какой сегодня день' in text_in_user_text\
                or 'Какой сегодня день' in text_in_user_text\
                or 'какой день' in text_in_user_text\
                or 'Какой день' in text_in_user_text\
                or 'Месяц' in text_in_user_text\
                or 'Какой месяц' in text_in_user_text\
                or 'Месяц' in text_in_user_text\
                or 'Год' in text_in_user_text\
                or 'год' in text_in_user_text\
                or 'Какой год' in text_in_user_text\
                or 'какой год' in text_in_user_text:
            return self.ui.textBrowser.setText(f'Вот сегоднешней день: {str(time.ctime())}')

        if 'Запомни мое имя' in text_in_user_text\
                or 'запомни мое имя' in text_in_user_text\
                or 'Запомни имя' in text_in_user_text\
                or 'запомни имя' in text_in_user_text\
                or 'Называй меня' in text_in_user_text\
                or 'называй меня' in text_in_user_text:
            self.name_open()

        if 'Имя' in text_in_user_text\
                or 'имя' in text_in_user_text\
                or 'Мое имя' in text_in_user_text\
                or 'мое имя' in text_in_user_text\
                or self.user_name.lower() in text_in_user_text:
            self.ui.textBrowser.setText(f'Вы просили называть вас: {self.user_name}')

        if 'закройся' in text_in_user_text\
            or 'закрыть' in text_in_user_text:
            sys.exit(app.exec())

        if 'команды' in text_in_user_text:
            self.ui.textBrowser.setText('Блокнот - открыть блакнот\n'
                                        'привет - поприветствовать\n'
                                        'пока - закончить\n'
                                        'время, год, месяц - узнать информацию о сегодняшнем дне\n'
                                        'запомни имя\n'
                                        'имя - напомнеть о вашем имени\n'
                                        'закрыть - закрыть программу')

        if 'игра' in text_in_user_text\
            or 'buhf' in text_in_user_text:
            self.clicker_open()

        else:
            list_no_info = ['Я пока незнаю такой команды',
                            'я незнаю как ответить на вашь вопрос',
                            'сам ищи, я незнаю']
            self.ui.textBrowser.setText(random.choice(list_no_info))



    def input_name(self):
        """
        выводит присвоенное имя
        :return:
        """
        self.user_name = self.ui.input_name_lineedit.text()
        self.name_close()
        self.ui.input_line_edit.setText('')
        return self.ui.textBrowser.setText(f'Теперь это ваше имя: {self.user_name}')


    def open_word(self):
        """
        открыть блакнот
        :return:
        """
        self.animation_word = QtCore.QPropertyAnimation(self.ui.widget_word, b"geometry")
        self.ui.widget_word.show()
        self.animation_word.setDuration(400)
        self.animation_word.setStartValue(QRect(100, 571, 571, 31))
        self.animation_word.setEndValue((QRect(30, 30, 571, 411)))
        self.animation_word.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation_word.start()


    def close_word(self):
        """
        закрыть блакнот
        :return:
        """
        self.animation_close_word = QtCore.QPropertyAnimation(self.ui.widget_word, b"geometry")
        self.ui.widget_word.show()
        self.animation_word.setDuration(400)
        self.animation_word.setStartValue(QRect(30, 30, 571, 411))
        self.animation_word.setEndValue((QRect(100, 571, 571, 31)))
        self.animation_word.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation_word.start()


    def end_the_conversation(self):
        '''
        завершить общение
        :return:
        '''
        self.start_conversation = False
        self.ui.input_line_edit.setText('')
        return self.ui.textBrowser.setText('Завершено')


    def start_func(self):
        '''
        начать общение
        :return:
        '''
        self.start_conversation = True
        self.ui.textBrowser.setText('Я готов к работе')
        return self.start_conversation ## #



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
