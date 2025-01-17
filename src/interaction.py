from PyQt5.QtWidgets import QApplication, QMainWindow
import open3d as o3d

class DesktopMate(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Desktop Mate")
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def mousePressEvent(self, event):
        print("Mate says: You clicked me!")

if __name__ == "__main__":
    app = QApplication([])
    window = DesktopMate()
    app.exec_()
