from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout
from popup import UI_MessageWindow

class UI_VerificareWindow(QDialog):

    def receive_message(self, message):
        # Afișare mesaj în QLabel
        self.message_label.setText(message)

    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Verificare Dialog")
        self.setGeometry(300, 300, 150, 100)
        background_pixmap = QPixmap("Imagini/background2.jpg")
        background_image = background_pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(background_image))
        self.setPalette(palette)
        title_font = QFont()
        title_font.setFamily("Agbalumo")
        title_font.setPointSize(20)

        message_window = UI_MessageWindow()
        message_window.message_signal.connect(self.receive_message)

        button_style = """
                                         QPushButton {
                                             color: #e06797;
                                             background-color: #f4bfd4;
                                             border: 2px solid #e995b7;
                                             border-radius: 15px;
                                             margin-left: 25px;
                                             margin-right: 25px;
                                         }
                                         QPushButton:hover {
                                             background-color: #e995b7;
                                             border-color:#f4bfd4;
                                             color: #f4bfd4;
                                         }
                                     """

        self.message_label = QLabel("")
        self.message_label.setStyleSheet("color: #e06797")
        self.message_label.setFont(QFont("Agbalumo", 14))
        self.message_label.setAlignment(Qt.AlignCenter)

        ok_button = QPushButton("OK")
        ok_button.setFont(QFont("Agbalumo", 14))
        ok_button.setStyleSheet(button_style)
        ok_button.setCursor(Qt.PointingHandCursor)

        ok_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.message_label)
        layout.addWidget(ok_button)
        self.setLayout(layout)

