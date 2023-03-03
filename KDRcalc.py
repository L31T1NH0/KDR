from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
import sys

class KdrCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # create labels and entries for kills and deaths
        kills_label = QLabel()
        self.kills_entry = QLineEdit()
        self.kills_entry.setPlaceholderText('Kill')
        self.kills_entry.setStyleSheet('border: 1px solid black; font-size: 16px; padding: 5px; text-align: center;')
        deaths_label = QLabel()
        self.deaths_entry = QLineEdit()
        self.deaths_entry.setPlaceholderText('Death')
        self.deaths_entry.setStyleSheet('border: 1px solid black; font-size: 16px; padding: 5px; text-align: center;')

        # create label for KDR output
        self.kdr_label = QLabel('KDR:')
        self.kdr_label.setStyleSheet('border-bottom: 1px solid black; font-size: 16px; padding: 5px;')

        # create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(kills_label)
        layout.addWidget(self.kills_entry)
        layout.addWidget(deaths_label)
        layout.addWidget(self.deaths_entry)
        layout.addSpacing(10)
        layout.addWidget(self.kdr_label, alignment=Qt.AlignCenter)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(0)

        # set layout
        self.setLayout(layout)

        # set window properties
        self.setWindowTitle('Calculadora de KDR')
        self.setGeometry(400, 300, 200, 200)
        self.setStyleSheet("background-color: #0f0c0c; color: #e5e1e1; border-radius: 4px;")
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setMinimumSize(274, 270)
        self.show()

        # connect signals
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
