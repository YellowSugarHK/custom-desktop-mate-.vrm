import logging

logging.basicConfig(filename="errors.log", level=logging.ERROR, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def load_vrm_model(self, model_path):
    """Load the VRM model and handle errors gracefully."""
    try:
        mesh = o3d.io.read_triangle_mesh(model_path)
        if mesh.is_empty():
            raise ValueError("The VRM file is empty or invalid!")
        o3d.visualization.draw_geometries([mesh])  # Replace this later with an embedded viewer
    except Exception as e:
        self.label.setText("Error loading model! Check errors.log.")
        logging.error(f"Error loading VRM: {e}")
