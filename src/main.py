import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
import open3d as o3d


class DesktopMate(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('DesktopMateVRM')
        self.setGeometry(100, 100, 800, 600)

        label = QLabel(self)
        label.setText('Your Desktop Mate is loading...')
        label.move(50, 50)

        # Load the VRM model
        self.load_vrm_model('assets/custom_avatar.vrm')

    def load_vrm_model(self, model_path):
        # Using open3d to load the 3D model
        mesh = o3d.io.read_triangle_mesh(model_path)
        o3d.visualization.draw_geometries([mesh])


# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DesktopMate()
    window.show()
    sys.exit(app.exec_())
