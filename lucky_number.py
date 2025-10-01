import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor
from PyQt5.QtCore import Qt

class LuckyNumber(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lucky Number Game")
        self.setGeometry(200, 100, 420, 320)
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #e0c3fc, stop:1 #8ec5fc);")
        self.target = random.randint(1, 100)
        self.attempts = 0
        self.init_ui()

    def init_ui(self):
        font_title = QFont("Segoe UI", 22, QFont.Bold)
        font_label = QFont("Segoe UI", 14)
        font_btn = QFont("Segoe UI", 14)
        self.title = QLabel("สุ่มเลขทายโชค (1-100)")
        self.title.setFont(font_title)
        self.title.setAlignment(Qt.AlignCenter)
        self.info = QLabel("กรอกเลขที่คุณคิดว่าใช่!")
        self.info.setFont(font_label)
        self.info.setAlignment(Qt.AlignCenter)
        self.input = QLineEdit()
        self.input.setFont(font_label)
        self.input.setAlignment(Qt.AlignCenter)
        self.input.setMaxLength(3)
        self.input.setStyleSheet("background: #fff; border-radius: 8px; padding: 8px; font-size: 16px;")
        self.btn = QPushButton("ทายเลข")
        self.btn.setFont(font_btn)
        self.btn.setStyleSheet("background-color: #a1c4fd; border-radius: 10px; padding: 10px; font-weight: bold;")
        self.btn.clicked.connect(self.check_number)
        self.result = QLabel("")
        self.result.setFont(font_label)
        self.result.setAlignment(Qt.AlignCenter)
        vbox = QVBoxLayout()
        vbox.addWidget(self.title)
        vbox.addWidget(self.info)
        vbox.addWidget(self.input)
        vbox.addWidget(self.btn)
        vbox.addWidget(self.result)
        self.setLayout(vbox)

    def check_number(self):
        guess = self.input.text()
        if not guess.isdigit():
            self.result.setText("กรุณากรอกตัวเลขเท่านั้น!")
            self.result.setStyleSheet("color: #ff4e50;")
            return
        guess = int(guess)
        self.attempts += 1
        if guess < self.target:
            self.result.setText("มากกว่านี้!")
            self.result.setStyleSheet("color: #0099f7;")
        elif guess > self.target:
            self.result.setText("น้อยกว่านี้!")
            self.result.setStyleSheet("color: #f7971e;")
        else:
            self.result.setText(f"ถูกต้อง! คุณทาย {self.attempts} ครั้ง")
            self.result.setStyleSheet("color: #43e97b;")
            QMessageBox.information(self, "ยินดีด้วย!", f"คุณทายถูกต้องใน {self.attempts} ครั้ง\nเริ่มเกมใหม่!")
            self.target = random.randint(1, 100)
            self.attempts = 0
            self.input.clear()
            self.result.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LuckyNumber()
    window.show()
    sys.exit(app.exec_())
