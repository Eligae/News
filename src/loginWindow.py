from src.function import papago
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QLabel, QWidget, QStackedWidget, QApplication
from src.NewsWindow import NewsWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 200, 300) 

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.login_widget = QWidget()
        self.login_layout = QVBoxLayout(self.login_widget)

        self.clientId_input = QLineEdit(self)
        self.clientId_input.move(50, 50)

        self.secret_input = QLineEdit(self)
        self.secret_input.move(50, 100)
        self.secret_input.setEchoMode(QLineEdit.Password) 

        self.login_button = QPushButton('로그인', self)
        self.login_button.move(50, 150)
        self.login_button.clicked.connect(self.login)

        self.status_label = QLabel(self)
        self.status_label.move(50, 200)

        self.load_saved_credentials()
        self.news_window = None

    def load_saved_credentials(self):
        try:
            with open('.\\src\\credentials.txt', 'r') as file:
                lines = file.readlines()
                if len(lines) == 2:
                    self.clientId_input.setText(lines[0].strip())
                    self.secret_input.setText(lines[1].strip())
        except FileNotFoundError:
            pass

    def save_credentials(self):
        username = self.clientId_input.text()
        password = self.secret_input.text()
        with open('credentials.txt', 'w') as file:
            file.write(username + '\n')
            file.write(password + '\n')

    def login(self):
        username = self.clientId_input.text()
        password = self.secret_input.text()
        papago.clientData(username, password)
        loginCheck = papago.toEng('로그인 테스트용')

        if loginCheck != 401:
            self.hide()
            if self.news_window is None:  # NewsWindow 인스턴스가 없으면 생성
                self.news_window = NewsWindow()

            self.news_window.show()  # 기존에 생성된 인스턴스를 표시
        else:
            print('error')