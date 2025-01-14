from PyQt5.QtWidgets import QMainWindow, QPushButton

class DesktopMate(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the main window properties
        self.setWindowTitle("Desktop Mate")
        self.setGeometry(100, 100, 800, 600)

        # Add a button to the UI
        button = QPushButton("Say Hello", self)
        button.setGeometry(100, 100, 150, 50)
        button.clicked.connect(self.say_hello)

    def say_hello(self):
        # This method is called when the button is clicked
        print("Mate says: Hello, world!")
