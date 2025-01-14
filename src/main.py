import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
import open3d as o3d
from voice_command import listen_to_command  # Voice recognition module


class DesktopMate(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle('Desktop Mate VRM')
        self.setGeometry(100, 100, 800, 600)

        # Add a label
        self.label = QLabel(self)
        self.label.setText('Your Desktop Mate is loading...')
        self.label.move(50, 50)

        # Load the default VRM model
        self.load_vrm_model('assets/custom_avatar.vrm')

    def load_vrm_model(self, model_path):
        """Load the VRM model using Open3D"""
        try:
            mesh = o3d.io.read_triangle_mesh(model_path)
            if mesh.is_empty():
                raise ValueError("The VRM file is empty or invalid!")
            o3d.visualization.draw_geometries([mesh])
        except Exception as e:
            self.label.setText(f"Error loading model: {e}")
            print(f"Error: {e}")

    def choose_model(self):
        """Allow the user to select a custom VRM model"""
        file_dialog = QFileDialog()
        model_path, _ = file_dialog.getOpenFileName(self, "Select a VRM Model", "", "VRM Files (*.vrm)")
        if model_path:
            self.load_vrm_model(model_path)


# Main entry point
if __name__ == '__main__':
    # Initialize the application
    app = QApplication(sys.argv)
    window = DesktopMate()

    # Show the main window
    window.show()

    # Voice command handling
    print("Say a command (e.g., 'wave' or 'load model'):")
    command = listen_to_command()
    if command == "wave":
        print("Mate is waving!")  # Add waving animation logic here
    elif command == "load model":
        print("Mate is ready to load a custom model!")
        window.choose_model()
    elif command == "hello":
        print("Mate says: Hello!")

    # Run the application
    sys.exit(app.exec_())

