import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox

class HelloWorld(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Hello World - [Your Name]")
        self.setGeometry(300, 300, 300, 200)

        # Layout
        layout = QVBoxLayout()

        # Widgets
        self.label = QLabel("Welcome to PyQt6!")
        self.button = QPushButton("Click Me")

        # Connect button click to function (Signal/Slot)
        self.button.clicked.connect(self.show_message)

        # Add to layout
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def show_message(self):
        QMessageBox.information(self, "Message", "Hello! You clicked the PyQt6 button.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelloWorld()
    window.show()
    sys.exit(app.exec())