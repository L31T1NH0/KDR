from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
import sys

class KdrCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # criar labels e entradas para kills e deaths
        self.kills_entry = QLineEdit()
        self.kills_entry.setPlaceholderText('Kill')
        self.kills_entry.setStyleSheet('border: 1px solid black; font-size: 16px; padding: 5px; text-align: center;')
        self.deaths_entry = QLineEdit()
        self.deaths_entry.setPlaceholderText('Death')
        self.deaths_entry.setStyleSheet('border: 1px solid black; font-size: 16px; padding: 5px; text-align: center;')

        # criar label para a saída do KDR
        self.kdr_label = QLabel('KDR:')
        self.kdr_label.setStyleSheet('border-bottom: 1px solid black; font-size: 16px; padding: 5px;')

        # criar layout e adicionar widgets
        layout = QVBoxLayout()
        layout.addWidget(self.kills_entry)
        layout.addWidget(self.deaths_entry)
        layout.addWidget(QLabel()) # novo QLabel vazio para adicionar espaçamento
        layout.addWidget(self.kdr_label, alignment=Qt.AlignCenter)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(10) # adiciona espaçamento de 10 pixels entre os widgets

        # definir layout
        self.setLayout(layout)

        # definir propriedades da janela
        self.setWindowTitle('Calculadora de KDR')
        self.setGeometry(400, 300, 200, 200)
        self.setStyleSheet("background-color: #0f0c0c; color: #e5e1e1; border-radius: 4px;")
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setMinimumSize(274, 270)
        self.show()

        # conectar sinais
        self.kills_entry.textChanged.connect(self.calculate_kdr)
        self.deaths_entry.textChanged.connect(self.calculate_kdr)


    def calculate_kdr(self):
        try:
            kills = float(self.kills_entry.text())
            deaths = float(self.deaths_entry.text())
            kdr = kills / deaths
            self.kdr_label.setText('KDR: {:.2f}'.format(kdr))
        except ZeroDivisionError:
            self.kdr_label.setText('KDR: {:.0f}'.format(kills))
        except ValueError:
            self.kdr_label.setText('KDR:')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = KdrCalculator()
    sys.exit(app.exec_())
