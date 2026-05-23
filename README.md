# S5-TRABAJO-PRA-CTICO-EXPERIMENTAL_2
Agenda desarrollada con QT para Python
1.	Introducción. 
Este proyecto consiste en el diseño y desarrollo de una Interfaz Gráfica de Usuario para una aplicación de gestión de contactos, utilizando el framework Qt a través de su biblioteca para Python (PySide6 o PyQt6).
El objetivo de esta aplicación es proporcionar un entorno visual intuitivo y organizado que permita la interacción con datos personales básicos. El software se divide en dos secciones principales:
•	Formulario de Entrada: Un panel dedicado a la captura de información (Nombre, Teléfono y Correo Electrónico) mediante campos de texto validados visualmente.
•	Panel de Visualización: Un área de listado que permite al usuario observar de manera clara los registros existentes en el sistema.
Este desarrollo se enfoca estrictamente en la arquitectura visual y la experiencia de usuario (UX), priorizando una distribución limpia mediante el uso de layouts y componentes nativos de Qt para garantizar una interfaz profesional, funcional y minimalista.
2.	Desarrollo. 
2.1.	Instalación del Entorno (Qt para Python)
Para el desarrollo de esta interfaz, utilizaremos PySide6, que es la biblioteca oficial de Qt para Python. Este framework permite acceder a todas las capacidades de las herramientas de C++ desde un entorno Pythonic.
Requisitos
•  Python 3.x instalado.
•  pip (gestor de paquetes de Python) actualizado.



2.2.	Creación del Entorno Virtual
Para mantener la limpieza del sistema y evitar conflictos de dependencias, se recomienda crear un entorno virtual dentro de la carpeta del proyecto:
# Crear el entorno virtual
python -m venv env

# Activar el entorno virtual
# En Windows:
env\Scripts\activate
# En macOS/Linux:
source env/bin/activate

2.3.	Instalación de PySide6
Una vez activo el entorno, se procede a instalar la biblioteca principal de Qt mediante el siguiente comando en la terminal:
pip install PySide6

2.4.	Verificación de Instalación
Para confirmar que la instalación fue exitosa y que el backend de Qt está listo para ser utilizado, puede ejecutar el siguiente comando que imprimirá la versión instalada:

python -c "import PySide6; print(PySide6.__version__)"

 
2.5.	Importaciones y Estructura Base de la Clase

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

1. Importación de Módulos
I.	import sys: Módulo nativo de Python necesario para gestionar los argumentos de la línea de comandos y el cierre limpio del proceso de la aplicación.
II.	PySide6.QtWidgets: Contiene el conjunto de elementos visuales (widgets). Se importan componentes como QMainWindow (ventana), QHBoxLayout (gestor de distribución horizontal) y los elementos que compondrán el formulario.
III.	PySide6.QtCore.Qt: Proporciona enumeraciones y constantes fundamentales de Qt, como alineaciones o tipos de punteros.
2. Clase AgendaContactos (Controlador de la Interfaz)
I.	class AgendaContactos(QMainWindow): Se define la clase principal heredando de QMainWindow, lo que otorga a nuestra aplicación las características de una ventana estándar de sistema operativo (barra de título, botones de minimizar/cerrar).
II.	super().__init__(): Llama al constructor de la clase padre para asegurar que la ventana se inicialice correctamente con todas las propiedades de Qt.
3. Configuración y Contenedor Central
I.	setWindowTitle y resize: Establecen la identidad visual de la ventana y sus dimensiones iniciales en píxeles.
II.	self.central_widget: En Qt, una QMainWindow requiere un widget que sirva de contenedor para todo el contenido. Aquí creamos un QWidget genérico para este fin.
III.	setCentralWidget: Asigna formalmente el contenedor anterior como el eje de la interfaz.
4. Gestión de Distribución (Layouts)
I.	QHBoxLayout(self.central_widget): Se instancia un gestor de diseño horizontal. Este es un punto crítico, ya que según la referencia de imagen.png, la interfaz se divide en dos grandes bloques contiguos (Formulario a la izquierda y Lista a la derecha).
5. Ciclo de Vida de la Aplicación
I.	QApplication(sys.argv): Crea la instancia de la aplicación. Es el motor que gestiona los eventos del usuario (clics, teclado).
II.	ventana.show(): Envía la instrucción al gestor de ventanas para hacer visible la interfaz.
III.	sys.exit(app.exec()): Inicia el bucle de eventos infinito. La aplicación se mantendrá en ejecución hasta que el usuario la cierre, momento en el que se devolverá el código de salida al sistema operativo.
 
2.6.	Sección del Formulario. 


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


1. Contenedores de Agrupación
I.	QGroupBox("Nuevo Contacto"): Se utiliza este componente para crear un marco visual con un título superior. Esto ayuda a cumplir con el requisito de jerarquía visual y separación de secciones solicitado, tal como se aprecia en el diseño de referencia.
II.	QVBoxLayout(): Se establece un layout vertical interno para el GroupBox. Esto permite que, si en el futuro se agregan más elementos bajo el formulario, se mantengan alineados verticalmente.
2. Gestión de Formulario (QFormLayout)
I.	QFormLayout(): Es un layout especializado para la creación de formularios. Su ventaja técnica es que alinea automáticamente las etiquetas (QLabel) a la izquierda y los campos de entrada (QLineEdit) a la derecha de forma simétrica, garantizando una interfaz limpia y profesional.
II.	addRow: Método que simplifica la creación de pares etiqueta-campo sin necesidad de instanciar cada QLabel manualmente, optimizando el código.
3. Campos de Entrada (QLineEdit)
I.	QLineEdit(): Componentes de una sola línea para la captura de texto.
II.	setPlaceholderText: Se implementa un texto de ayuda tenue dentro de los campos. Esta es una buena práctica de UX que indica al usuario qué tipo de información se espera antes de que comience a escribir, mejorando la usabilidad de la agenda.
4. Integración en el Layout Principal
I.	self.layout_principal.addWidget(self.seccion_izquierda): Finalmente, se añade el bloque completo del formulario al layout horizontal principal definido en el Paso 1. Al ser el primer elemento añadido, ocupará la posición izquierda de la ventana.
2.7.	Sección de Visualización.
        self.seccion_derecha = QGroupBox("Lista de Contactos")
        self.layout_lista = QVBoxLayout()
        self.seccion_derecha.setLayout(self.layout_lista)

        self.list_widget = QListWidget()
        self.list_widget.addItem("Ana Pérez, (123) 456-7890\nana.perez@email.com")
        self.list_widget.addItem("Juan Gómez, (234) 567-1234\njuan.gomez@email.com")

        self.layout_lista.addWidget(self.list_widget)
        self.layout_principal.addWidget(self.seccion_derecha)
En esta fase se implementa el componente de salida y visualización de la información:
1. Contenedor de Grupo Derecho
I.	QGroupBox("Lista de Contactos"): Al igual que en la sección izquierda, se utiliza un QGroupBox para mantener la simetría visual de la aplicación. Este contenedor agrupa todos los elementos relacionados con la visualización de la base de datos de contactos.
II.	QVBoxLayout(): Se asigna un layout vertical para que la lista ocupe todo el espacio disponible dentro del marco, permitiendo que el componente crezca proporcionalmente si se redimensiona la ventana.
2. Componente de Visualización (QListWidget)
I.	QListWidget(): Es el widget encargado de mostrar una lista de elementos que el usuario puede seleccionar. Es ideal para este proyecto ya que permite manejar múltiples filas de texto de manera eficiente.
II.	addItem: Método utilizado para insertar elementos en la lista. Aunque el requerimiento menciona que no se necesita lógica CRUD real, se añaden elementos estáticos para validar que la jerarquía visual y el formato de los datos (Nombre, Teléfono, Correo) coincidan con la referencia estética de la aplicación.
3. Integración en el Layout Principal
I.	self.layout_principal.addWidget(self.seccion_derecha): Se añade este bloque al layout horizontal principal. Al ser el segundo elemento agregado al QHBoxLayout, Qt lo posiciona automáticamente a la derecha del formulario de entrada, completando la estructura de dos columnas solicitada.
2.8.	Barra de Botones
        self.layout_inferior = QHBoxLayout()
        self.btn_agregar = QPushButton("Agregar")
        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_limpiar = QPushButton("Limpiar")

        self.layout_inferior.addStretch()
        self.layout_inferior.addWidget(self.btn_agregar)
        self.layout_inferior.addWidget(self.btn_eliminar)
        self.layout_inferior.addWidget(self.btn_limpiar)

        self.layout_contenedor_vertical.addLayout(self.layout_principal)
        self.layout_contenedor_vertical.addLayout(self.layout_inferior)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = AgendaContactos()
    ventana.show()
    sys.exit(app.exec())

En esta fase final se implementan los controles de acción y se ajusta la disposición global de la interfaz:
1. Gestión de Botones (QPushButton)
I.	QPushButton: Se instancian los tres botones requeridos: "Agregar", "Eliminar" y "Limpiar". Estos componentes son los disparadores de eventos estándar en aplicaciones Qt.
II.	addStretch(): Esta es una técnica avanzada de diseño en Qt. El "stretch" actúa como un resorte invisible que empuja los botones hacia la derecha, permitiendo que la distribución se vea equilibrada y profesional, evitando que los botones se estiren innecesariamente para llenar el ancho de la ventana.
2. Layouts Anidados (Arquitectura de Contenedores)
I.	QHBoxLayout() (Inferior): Se crea un nuevo layout horizontal exclusivamente para los botones, lo que permite que se mantengan alineados en una sola fila independientemente del tamaño de la lista o el formulario superior.
II.	QVBoxLayout() (Contenedor Maestro): Para integrar todo, se crea un layout vertical que envuelve a los anteriores. Este contenedor coloca el bloque de datos (layout_principal) arriba y la botonera (layout_inferior) abajo.
3. Jerarquía Visual Final
I.	Al aplicar esta estructura de layouts anidados, logramos que la aplicación sea responsiva. Si redimensionas la ventana en tu MacBook, los elementos se ajustarán proporcionalmente manteniendo la estética definida en los requisitos.
Con esto, el diseño visual de la Agenda de Contactos está completo y cumple con todos los puntos solicitados: uso de layouts, componentes obligatorios y una jerarquía clara.
3.	Conclusion. 
La implementación de esta interfaz gráfica en Qt para Python demuestra cómo una arquitectura modular y el uso correcto de gestores de diseño (layouts) permiten replicar entornos visuales profesionales y escalables. A través de la Programación Orientada a Objetos, se logró una separación clara entre los componentes de captura de datos y los de visualización, cumpliendo con los requisitos de jerarquía visual y funcionalidad estética solicitados en la actividad.

4.	Bibliografia.
1.	Apple Inc. (2024). Apple Silicon Support and Compatibility for Developers. https://developer.apple.com/apple-silicon/
2.	Beazley, D. M. (2021). Python Distilled. Addison-Wesley Professional.
3.	Dierbach, C. (2012). Introduction to Computer Science Using Python: A Computational Problem-Solving Focus. Wiley.
4.	Fitzpatrick, M. (2024). Create GUI Applications with PySide6. pythonguis.com.
5.	Lutz, M. (2013). Learning Python. O'Reilly Media.
6.	Qt Group. (2026). Qt for Python Documentation: PySide6 Basics. https://doc.qt.io/qtforpython-6/
7.	Qt Group. (2026). Qt Layout Management System. https://doc.qt.io/qt-6/layout.html
8.	Qt Group. (2026). QListWidget Class Reference. https://doc.qt.io/qt-6/qlistwidget.html
9.	Python Software Foundation. (2026). The Python Standard Library: sys — System-specific parameters and functions. https://docs.python.org/3/library/sys.html
10.	Python Software Foundation. (2026). venv — Creation of virtual environments. https://docs.python.org/3/library/venv.html
11.	Summerfield, M. (2018). Rapid GUI Programming with Python and Qt. Prentice Hall.
12.	Van Rossum, G., Warsaw, B., & Coghlan, N. (2001). PEP 8 – Style Guide for Python Code. https://peps.python.org/pep-0008/
 

