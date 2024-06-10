import sys
import keyboard
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer

class Panel(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setWindowFlag(Qt.X11BypassWindowManagerHint)
        
        # Configurar layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Botón para ocultar/mostrar
        self.toggle_button = QPushButton('Ocultar')
        self.toggle_button.clicked.connect(self.toggle_visibility)
        layout.addWidget(self.toggle_button)

        # Configurar la posición de la ventana en la esquina inferior derecha
        screen_geometry = QApplication.desktop().availableGeometry()
        self.setGeometry(screen_geometry.width() - 300, screen_geometry.height() - 100, 300, 100)

        # Crear un atajo de teclado global para mostrar el panel
        keyboard.add_hotkey('ctrl+shift+f', self.toggle_visibility)

        # Mostrar la ventana
        self.show()

    def toggle_visibility(self):
        if self.isVisible():
            self.hide()
            self.toggle_button.setText('Mostrar')
        else:
            self.show()
            self.toggle_button.setText('Ocultar')
        
    def hide_panel(self):
        self.hide()
        self.toggle_button.setText('Mostrar')

    def show_panel(self):
        self.show()
        self.toggle_button.setText('Ocultar')

    def enterEvent(self, event):
        #self.timer.stop()
        ...
    def leaveEvent(self, event):
        # 
        ...
if __name__ == '__main__':
    app = QApplication(sys.argv)
    panel = Panel()
    sys.exit(app.exec_())

