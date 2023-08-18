from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class NewsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("News Window")
        self.setGeometry(100, 100, 400, 300)

        label = QLabel("Hello, World!", self)
        label.move(150, 120)
