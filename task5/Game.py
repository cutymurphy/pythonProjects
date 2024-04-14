import sys
import random

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QHBoxLayout, QVBoxLayout, QMessageBox, QLabel

import Logic


class GameWindow(QWidget):

    def __init__(self, heigth, width):
        super().__init__()
        self.setWindowTitle('Color Matching Game')
        self.setGeometry(100, 100, heigth, width)

        self.array = self.initialize_array()

        layout = QVBoxLayout()
        self.setup_top_buttons(layout)
        self.setup_game_grid(layout)
        self.setup_bottom_buttons(layout)

        self.timer_label = QLabel()
        layout.addWidget(self.timer_label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.count = 0
        self.timer.start(10)  # Задаем интервал в миллисекундах (1000 мс = 1 секунда)

        self.setLayout(layout)

    def update_timer(self):
        self.count += 1
        milliseconds = self.count % 100
        seconds = (self.count // 100) % 60
        minutes = (self.count // 6000) % 60
        self.timer_label.setText(f"Timer: {minutes:02d}:{seconds:02d}:{milliseconds:02d}")


    def initialize_array(self):
        colors = ['red', 'green', 'blue', 'yellow']
        array = [random.sample(colors, len(colors)) for _ in range(4)]
        return array

    def setup_top_buttons(self, layout):
        top_row_layout = QHBoxLayout()
        for i in range(6):
            button = self.create_button("↑")

            if i in (0, 5):
                button.setStyleSheet("background-color: transparent; color: transparent;")

            button.clicked.connect(lambda _, idx = i - 1: self.shift_col_up(idx))
            top_row_layout.addWidget(button)
        layout.addLayout(top_row_layout)

    def setup_bottom_buttons(self, layout):
        bottom_row_layout = QHBoxLayout()
        for i in range(6):
            button = self.create_button("↓")

            if i in (0, 5):
                button.setStyleSheet("background-color: transparent; color: transparent;")

            button.clicked.connect(lambda _, idx=i - 1: self.shift_col_down(idx))
            bottom_row_layout.addWidget(button)
        layout.addLayout(bottom_row_layout)

    def setup_game_grid(self, layout):
        self.square_lists = []

        for row_index in range(4):
            row_layout = QHBoxLayout()
            button = self.create_button("←")
            button.clicked.connect(lambda _, idx=row_index: self.shift_row_left(idx))
            row_layout.addWidget(button)

            square_list = []
            for color in self.array[row_index]:
                square = QFrame()
                square.setFixedSize(50, 50)
                square.setStyleSheet(f"background-color: {color};")
                row_layout.addWidget(square)
                square_list.append(square)

            button = self.create_button("→")
            button.clicked.connect(lambda _, idx=row_index: self.shift_row_right(idx))
            row_layout.addWidget(button)

            layout.addLayout(row_layout)
            self.square_lists.append(square_list)

    def create_button(self, text):
        button = QPushButton(text)
        button.setFixedSize(50, 50)
        return button

    def shift_row_left(self, row_index):
        row = self.array[row_index]
        Logic.Logic.shift_row_left(self.array, row_index)

        for square, color in zip(self.square_lists[row_index], row):
            square.setStyleSheet(f"background-color: {color};")

        self.win_window()

    def shift_row_right(self, row_index):
        row = self.array[row_index]
        Logic.Logic.shift_row_right(self.array, row_index)

        for square, color in zip(self.square_lists[row_index], row):
            square.setStyleSheet(f"background-color: {color};")

        self.win_window()

    def shift_col_up(self, col_index):
        col = [list(c) for c in zip(*self.array)][col_index]
        Logic.Logic.shift_col_up(self.array, col_index)

        for square, color in zip([list(c) for c in zip(*self.square_lists)][col_index], col):
            square.setStyleSheet(f"background-color: {color};")

        self.win_window()

    def shift_col_down(self, col_index):
        col = [list(c) for c in zip(*self.array)][col_index]
        Logic.Logic.shift_col_down(self.array, col_index)

        for square, color in zip([list(c) for c in zip(*self.square_lists)][col_index], col):
            square.setStyleSheet(f"background-color: {color};")

        self.win_window()

    def check_win(self):
        if (self.array[0][0] == self.array[0][1] == self.array[1][0] == self.array[1][1] and
                self.array[0][2] == self.array[0][3] == self.array[1][2] == self.array[1][3] and
                self.array[2][0] == self.array[2][1] == self.array[3][0] == self.array[3][1] and
                self.array[2][2] == self.array[2][3] == self.array[3][2] == self.array[3][3]):
            return True

    def win_window(self):
        checked = self.check_win()
        if checked:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("WIN!")
            dlg.setText("Вы победили!")
            button = dlg.exec()

            if button == QMessageBox.StandardButton.Ok:
                print("OK!")



def main(heigth, width):
    app = QApplication(sys.argv)
    game_window = GameWindow(heigth, width)
    game_window.show()
    sys.exit(app.exec_())

main(400, 400)
