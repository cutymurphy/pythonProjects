import sys
import random
from functools import partial
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QHBoxLayout, QVBoxLayout, QMessageBox, QLabel

import Logic

class GameWindow(QWidget):
    ROWS = 4
    COLUMNS = 4
    BUTTON_SIZE = 50

    def __init__(self, height, width, array):
        super().__init__()
        self.setWindowTitle('Color Matching Game')
        self.setGeometry(100, 100, height, width)

        self.array = array

        layout = QVBoxLayout()
        self.setup_top_buttons(layout)
        self.setup_game_grid(layout)
        self.setup_bottom_buttons(layout)

        self.timer_label = QLabel()
        layout.addWidget(self.timer_label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.count = 0
        self.timer.start(10)
        self.win_time = ""

        self.setLayout(layout)

    def update_timer(self):
        self.count += 1
        milliseconds = self.count % 100
        seconds = (self.count // 100) % 60
        minutes = (self.count // 6000) % 60
        self.win_time = f"Timer: {minutes:02d}:{seconds:02d}:{milliseconds:02d}"
        self.timer_label.setText(self.win_time)

        if self.check_win():
            self.timer.stop()

    def setup_top_buttons(self, layout):
        top_row_layout = QHBoxLayout()
        for i in range(self.COLUMNS + 2):
            button = self.create_button("↑")

            if i in (0, self.COLUMNS + 1):
                button.setStyleSheet("background-color: transparent; color: transparent;")
            else:
                button.clicked.connect(partial(self.shift_col_up, i - 1))
            top_row_layout.addWidget(button)
        layout.addLayout(top_row_layout)

    def setup_bottom_buttons(self, layout):
        bottom_row_layout = QHBoxLayout()
        for i in range(self.COLUMNS + 2):
            button = self.create_button("↓")

            if i in (0, self.COLUMNS + 1):
                button.setStyleSheet("background-color: transparent; color: transparent;")

            button.clicked.connect(partial(self.shift_col_down, i - 1))
            bottom_row_layout.addWidget(button)
        layout.addLayout(bottom_row_layout)

    def setup_game_grid(self, layout):
        self.square_lists = []

        for row_index in range(self.ROWS):
            row_layout = QHBoxLayout()
            button = self.create_button("←")
            button.clicked.connect(partial(self.shift_row_left, row_index))
            row_layout.addWidget(button)

            square_list = []
            for color in self.array[row_index]:
                square = QFrame()
                square.setFixedSize(self.BUTTON_SIZE, self.BUTTON_SIZE)
                square.setStyleSheet(f"background-color: {color};")
                row_layout.addWidget(square)
                square_list.append(square)

            button = self.create_button("→")
            button.clicked.connect(partial(self.shift_row_right, row_index))
            row_layout.addWidget(button)

            layout.addLayout(row_layout)
            self.square_lists.append(square_list)

    def create_button(self, text):
        button = QPushButton(text)
        button.setFixedSize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        return button

    def shift_row(self, row_index, direction):
        row = self.array[row_index]
        if direction == "left":
            Logic.Logic.shift_row_left(self.array, row_index)
        elif direction == "right":
            Logic.Logic.shift_row_right(self.array, row_index)
        for square, color in zip(self.square_lists[row_index], row):
            square.setStyleSheet(f"background-color: {color};")

        self.show_win_message()

    def shift_row_left(self, row_index):
        self.shift_row(row_index, "left")

    def shift_row_right(self, row_index):
        self.shift_row(row_index, "right")

    def shift_col(self, col_index, direction):
        if direction == "up":
            Logic.Logic.shift_col_up(self.array, col_index)
        elif direction == "down":
            Logic.Logic.shift_col_down(self.array, col_index)

        col = [list(c) for c in zip(*self.array)][col_index]

        for square, color in zip([list(c) for c in zip(*self.square_lists)][col_index], col):
            square.setStyleSheet(f"background-color: {color};")

        self.show_win_message()

    def shift_col_up(self, col_index):
        self.shift_col(col_index, "up")

    def shift_col_down(self, col_index):
        self.shift_col(col_index, "down")

    def check_win(self):
        if self.array[0] == self.array[1] and self.array[2] == self.array[3]:
            for i in range(self.ROWS):
                if self.array[i][0] != self.array[i][1] or self.array[i][2] != self.array[i][3]:
                    return False
            return True
        return False

    def show_win_message(self):
        if self.check_win():
            self.update_timer()
            dlg = QMessageBox(self)
            dlg.resize(400, 200)

            dlg.setFont(QFont("Arial", 16))
            dlg.setWindowTitle("WIN!")

            dlg.setText(f"You Win!\n{self.win_time}")
            dlg.setTextFormat(Qt.TextFormat.AutoText)

            button = dlg.exec()
            if button == QMessageBox.StandardButton.Ok:
                QApplication.quit()

def initialize_array():
    winning_case = [['red', 'red', 'green', 'green'], ['red', 'red', 'green', 'green'],
                    ['blue', 'yellow', 'yellow', 'blue'], ['blue', 'blue', 'yellow', 'yellow']]

    colors = ['red', 'green', 'blue', 'yellow']
    array = [random.sample(colors, len(colors)) for _ in range(4)]

    return winning_case

def main(height, width):
    app = QApplication(sys.argv)
    array = initialize_array()
    game_window = GameWindow(height, width, array)
    game_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main(400, 400)

