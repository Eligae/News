from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import src.function.newsSection as newsSection
import src.function.papago as papago

class NewsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("News Window")
        self.setGeometry(100, 100, 400, 300)

        