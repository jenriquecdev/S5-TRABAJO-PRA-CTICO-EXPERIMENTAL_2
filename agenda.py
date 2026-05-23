import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QHBoxLayout, QFormLayout, QLabel, QLineEdit, 
    QPushButton, QListWidget, QGroupBox
)
from PySide6.QtCore import Qt

class AgendaContactos(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Agenda de Contactos")
        self.resize(600, 400) 

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout_contenedor_vertical = QVBoxLayout(self.central_widget)
        
        self.layout_principal = QHBoxLayout()

        self.init_ui()

    def init_ui(self):
        # --- SECCIÓN IZQUIERDA (FORMULARIO) ---
        self.seccion_izquierda = QGroupBox("Nuevo Contacto")
        self.layout_formulario_contenedor = QVBoxLayout()
        self.seccion_izquierda.setLayout(self.layout_formulario_contenedor)

        self.formulario = QFormLayout()
        
        self.txt_nombre = QLineEdit()
        self.txt_nombre.setPlaceholderText("Ingrese el nombre")
        
        self.txt_telefono = QLineEdit()
        self.txt_telefono.setPlaceholderText("Ingrese el teléfono")
        
        self.txt_correo = QLineEdit()
        self.txt_correo.setPlaceholderText("Ingrese el correo (opcional)")

        self.formulario.addRow("Nombre:", self.txt_nombre)
        self.formulario.addRow("Teléfono:", self.txt_telefono)
        self.formulario.addRow("Correo:", self.txt_correo)

        self.layout_formulario_contenedor.addLayout(self.formulario)
        self.layout_principal.addWidget(self.seccion_izquierda)

        self.seccion_derecha = QGroupBox("Lista de Contactos")
        self.layout_lista = QVBoxLayout()
        self.seccion_derecha.setLayout(self.layout_lista)

        self.list_widget = QListWidget()
        self.list_widget.addItem("Ana Pérez, (123) 456-7890\nana.perez@email.com")
        self.list_widget.addItem("Juan Gómez, (234) 567-1234\njuan.gomez@email.com")

        self.layout_lista.addWidget(self.list_widget)
        self.layout_principal.addWidget(self.seccion_derecha)

        self.layout_inferior = QHBoxLayout()
        self.btn_agregar = QPushButton("Agregar")
        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_limpiar = QPushButton("Limpiar")

        self.layout_inferior.addStretch()
        self.layout_inferior.addWidget(self.btn_agregar)
        self.layout_inferior.addWidget(self.btn_eliminar)
        self.layout_inferior.addWidget(self.btn_limpiar)

        # Integrar layouts al contenedor maestro
        self.layout_contenedor_vertical.addLayout(self.layout_principal)
        self.layout_contenedor_vertical.addLayout(self.layout_inferior)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = AgendaContactos()
    ventana.show()
    sys.exit(app.exec())