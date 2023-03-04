from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
import sys
import os

class MouseSensibilidade(QWidget):
    def __init__(self):
        super().__init__()

        # Define o estilo do aplicativo
        estilo = """
        QWidget {
            background-color: #333333;
            color: #cccccc;
            font-size: 16px;
            font-family: Arial;
        }
        QLabel {
            font-size: 18px;
        }
        QLineEdit {
            background-color: #555555;
            border: 1px solid #666666;
            color: #cccccc;
            font-size: 16px;
            height: 30px;
            padding: 5px;
        }
        """

        # Define o estilo para o aplicativo
        self.setStyleSheet(estilo)
        self.estilo = estilo

        # Crie as caixas de entrada e saída
        self.peso_atual_label = QLabel("Peso do mouse atual (em gramas): ")
        self.peso_atual_input = QLineEdit()
        self.sensibilidade_atual_label = QLabel("Sensibilidade atual: ")
        self.sensibilidade_atual_output = QLabel()
        self.peso_novo_label = QLabel("Peso do mouse que você quer saber a nova sensibilidade (em gramas): ")
        self.peso_novo_input = QLineEdit()
        self.sensibilidade_nova_label = QLabel("Nova sensibilidade: ")
        self.sensibilidade_nova_output = QLabel()

        # Configure o layout da janela
        layout = QVBoxLayout()
        layout.addWidget(self.peso_atual_label)
        layout.addWidget(self.peso_atual_input)
        layout.addWidget(self.sensibilidade_atual_label)
        layout.addWidget(self.sensibilidade_atual_output)
        layout.addWidget(self.peso_novo_label)
        layout.addWidget(self.peso_novo_input)
        layout.addWidget(self.sensibilidade_nova_label)
        layout.addWidget(self.sensibilidade_nova_output)

        # Configure a janela
        self.setLayout(layout)
        self.setWindowTitle("Calculadora de Sensibilidade de Mouse")
        self.setGeometry(200, 200, 400, 300)

        # Obtenha a sensibilidade atual do arquivo "options.txt"
        sensibilidade_atual = self.obter_sensibilidade_atual()
        self.sensibilidade_atual_output.setText(str(sensibilidade_atual))

        # Conecte o sinal "textChanged" dos inputs ao método "atualizar_sensibilidade"
        self.peso_atual_input.textChanged.connect(self.atualizar_sensibilidade)
        self.peso_novo_input.textChanged.connect(self.atualizar_sensibilidade)

        self.show()

    def atualizar_sensibilidade(self):
        # Obtenha os valores de entrada
        peso_atual_text = self.peso_atual_input.text()
        if peso_atual_text != '':
            try:
                peso_atual = float(peso_atual_text)
            except ValueError:
                self.peso_atual_input.setText('')
                peso_atual = 0.0
        else:
            peso_atual = 0.0

        peso_novo_text = self.peso_novo_input.text()
        if peso_novo_text != '':
            try:
                peso_novo = float(peso_novo_text)
            except ValueError:
                self.peso_novo_input.setText('')
                peso_novo = 0.0
        else:
            peso_novo = 0.0

        # Obtenha a sensibilidade atual do arquivo "options.txt"
        sensibilidade_atual = self.obter_sensibilidade_atual()

        # Calcule a nova sensibilidade usando a regra de três
        sensibilidade_nova = None
        if peso_atual != 0.0:
            try:
                sensibilidade_nova = sensibilidade_atual * (peso_novo / peso_atual)
            except ZeroDivisionError:
                self.sensibilidade_nova_output.setText('')
        if sensibilidade_nova is not None:
            # Exiba a nova sensibilidade na caixa de saída
            self.sensibilidade_nova_output.setText("{:.7f}".format(sensibilidade_nova))

    def obter_sensibilidade_atual(self):
        # Obtenha o caminho completo do arquivo "options.txt"
        caminho_arquivo = os.path.join(os.getenv('APPDATA'), '.minecraft', 'options.txt')

        # Abra o arquivo para leitura
        with open(caminho_arquivo, 'r') as f:
            # Leia todas as linhas do arquivo
            linhas = f.readlines()

        # Obtenha a segunda linha, que contém a sensibilidade atual
        sensibilidade_linha = linhas[1]

        # Obtenha a sensibilidade atual a partir da linha
        sensibilidade_atual = float(sensibilidade_linha.split(':')[1].strip())

        return sensibilidade_atual

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MouseSensibilidade()
    sys.exit(app.exec_())
