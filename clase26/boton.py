titulo = QLabel("Formulario de Registro")
titulo.setAlignment(Qt.AlignCenter)  # centrado
titulo.setStyleSheet("font-size: 18pt; font-weight: bold;")  # grande y negrita
layout.addWidget(titulo, 0, 0, 1, 2)  # fila 0, columna 0, ocupa 1 fila y 2 columnas

label_nombre = QLabel("Nombre:")
entrada_nombre = QLineEdit()
layout.addWidget(label_nombre, 1, 0)   # fila 1, columna 0
layout.addWidget(entrada_nombre, 1, 1) # fila 1, columna 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
