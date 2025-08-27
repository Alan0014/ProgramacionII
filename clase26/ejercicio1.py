import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton,
    QRadioButton, QButtonGroup, QComboBox, QCheckBox, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 500, 500)  # ventana más grande

        # -------------------------------
        # Color de fondo
        paleta = self.palette()
        paleta.setColor(QPalette.Window, QColor("#f0f0f0"))  # gris claro
        self.setPalette(paleta)

        # -------------------------------
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignCenter)  # centrar todo el layout
        layout.setVerticalSpacing(15)       # espacio entre filas
        self.setLayout(layout)

        # -------------------------------
        # Título
        titulo = QLabel("Formulario de Registro")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setFont(QFont("Arial", 20, QFont.Bold))
        layout.addWidget(titulo, 0, 0, 1, 2)

        # -------------------------------
        # Campo Nombre
        label_nombre = QLabel("Nombre:")
        label_nombre.setFont(QFont("Arial", 12))
        self.entrada_nombre = QLineEdit()
        self.entrada_nombre.setFont(QFont("Arial", 12))
        layout.addWidget(label_nombre, 1, 0)
        layout.addWidget(self.entrada_nombre, 1, 1)

        # Campo Email
        label_email = QLabel("Email:")
        label_email.setFont(QFont("Arial", 12))
        self.entrada_email = QLineEdit()
        self.entrada_email.setFont(QFont("Arial", 12))
        layout.addWidget(label_email, 2, 0)
        layout.addWidget(self.entrada_email, 2, 1)

        # Campo Contraseña
        label_pass = QLabel("Contraseña:")
        label_pass.setFont(QFont("Arial", 12))
        self.entrada_pass = QLineEdit()
        self.entrada_pass.setFont(QFont("Arial", 12))
        self.entrada_pass.setEchoMode(QLineEdit.Password)
        layout.addWidget(label_pass, 3, 0)
        layout.addWidget(self.entrada_pass, 3, 1)

        # -------------------------------
        # Género
        label_genero = QLabel("Género:")
        label_genero.setFont(QFont("Arial", 12))
        self.radio_m = QRadioButton("Masculino")
        self.radio_m.setFont(QFont("Arial", 12))
        self.radio_f = QRadioButton("Femenino")
        self.radio_f.setFont(QFont("Arial", 12))

        self.grupo_genero = QButtonGroup(self)
        self.grupo_genero.addButton(self.radio_m)
        self.grupo_genero.addButton(self.radio_f)

        layout.addWidget(label_genero, 4, 0)
        layout.addWidget(self.radio_m, 4, 1)
        layout.addWidget(self.radio_f, 5, 1)

        # -------------------------------
        # País
        label_pais = QLabel("País:")
        label_pais.setFont(QFont("Arial", 12))
        self.combo_pais = QComboBox()
        self.combo_pais.setFont(QFont("Arial", 12))
        self.combo_pais.addItems(["Seleccione un país", "Argentina", "Brasil", "Chile", "México", "España"])
        layout.addWidget(label_pais, 6, 0)
        layout.addWidget(self.combo_pais, 6, 1)

        # -------------------------------
        # Checkbox
        self.checkbox = QCheckBox("Acepto los términos y condiciones")
        self.checkbox.setFont(QFont("Arial", 12))
        layout.addWidget(self.checkbox, 7, 0, 1, 2)

        # -------------------------------
        # Botón Registrarse
        boton = QPushButton("Registrarse")
        boton.setFont(QFont("Arial", 14, QFont.Bold))
        boton.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px;")
        boton.clicked.connect(self.validar_registro)
        layout.addWidget(boton, 8, 0, 1, 2)

    # -------------------------------
    def validar_registro(self):
        nombre = self.entrada_nombre.text().strip()
        email = self.entrada_email.text().strip()
        contrasena = self.entrada_pass.text().strip()
        pais = self.combo_pais.currentText()

        genero = None
        if self.radio_m.isChecked():
            genero = "Masculino"
        elif self.radio_f.isChecked():
            genero = "Femenino"

        if not nombre or not email or not contrasena:
            QMessageBox.warning(self, "Error", "Todos los campos de texto deben completarse.")
            return
        if genero is None:
            QMessageBox.warning(self, "Error", "Debe seleccionar un género.")
            return
        if pais == "Seleccione un país":
            QMessageBox.warning(self, "Error", "Debe seleccionar un país válido.")
            return
        if not self.checkbox.isChecked():
            QMessageBox.warning(self, "Error", "Debe aceptar los términos y condiciones.")
            return

        QMessageBox.information(
            self, "Éxito",
            f"Registro exitoso:\n\nNombre: {nombre}\nEmail: {email}\nGénero: {genero}\nPaís: {pais}"
        )

# -------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
