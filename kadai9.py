import random
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QGridLayout, QSizePolicy

class Window(QMainWindow):

    def __init__(self, verses):
        super().__init__()

        self.verses = verses
        self.current_verse_index = -1

        self.setFixedSize(QSize(1920, 1080))
        self.setWindowTitle('百人一首')
        self.countryLabel = QLabel('開始')
        self.countryLabel.setAlignment(Qt.AlignCenter)
        self.countryLabel.setStyleSheet('font: 40px; font-weight: bold')

        self.startBtn = QPushButton('はじめ')
        self.startBtn.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.startBtn.setStyleSheet('font: 20px; font-weight: bold')
        self.startBtn.clicked.connect(self.push_startBtn)

        self.nextBtn = QPushButton('つぎの句へ')
        self.nextBtn.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.nextBtn.setStyleSheet('font: 20px; font-weight: bold')
        self.nextBtn.setEnabled(False)
        self.nextBtn.clicked.connect(self.push_nextBtn)

        layout = QGridLayout()
        layout.addWidget(self.countryLabel, 0, 0, 1, 4)
        layout.addWidget(self.startBtn, 1, 0, 1, 1)
        layout.addWidget(self.nextBtn, 1, 1, 1, 3)

        mainWindow = QWidget()
        mainWindow.setLayout(layout)

        self.setCentralWidget(mainWindow)

    def push_startBtn(self):
        self.startBtn.setEnabled(False)
        self.nextBtn.setEnabled(True)
        random.shuffle(self.verses)
        self.current_verse_index = 0
        self.countryLabel.setText(self.verses[self.current_verse_index])

    def push_nextBtn(self):
        self.current_verse_index += 1
        if self.current_verse_index < len(self.verses):
            self.countryLabel.setText(self.verses[self.current_verse_index])
        else:
            self.countryLabel.setText("すべての句を表示しました")
            self.startBtn.setEnabled(True)
            self.nextBtn.setEnabled(False)

if __name__ == "__main__":
    with open("hyakunin_issyu.txt", "r", encoding="utf-8") as file:
        verses = [line.strip() for line in file.readlines()]

    app = QApplication([])
    ex = Window(verses)
    ex.show()
    app.exec()