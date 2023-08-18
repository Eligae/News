import newsSection
import papago
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.username_input = QLineEdit(self)
        self.username_input.move(50, 50)

        self.password_input = QLineEdit(self)
        self.password_input.move(50, 100)
        self.password_input.setEchoMode(QLineEdit.Password)  # 비밀번호 입력 필드 설정

        self.login_button = QPushButton('로그인', self)
        self.login_button.move(50, 150)
        self.login_button.clicked.connect(self.login)

        self.status_label = QLabel(self)
        self.status_label.move(50, 200)

        self.load_saved_credentials()  # 저장된 값 불러오기

    def load_saved_credentials(self):
        try:
            with open('credentials.txt', 'r') as file:
                lines = file.readlines()
                if len(lines) == 2:
                    self.username_input.setText(lines[0].strip())
                    self.password_input.setText(lines[1].strip())
        except FileNotFoundError:
            pass

    def save_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()
        with open('credentials.txt', 'w') as file:
            file.write(username + '\n')
            file.write(password + '\n')

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # 로그인 로직 여기에 작성

        self.status_label.setText(f"로그인 정보: {username}, {password}")
        self.save_credentials()  # 값 저장

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.setWindowTitle('로그인')
    window.setGeometry(100, 100, 300, 300)
    window.show()
    sys.exit(app.exec_())


