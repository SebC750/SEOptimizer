from controllers import converter_controller
from models import file_converter
converter = converter_controller.ConverterController()
repository = file_converter.FileConverterRepository()

def test_image_to_webp():   
    response = converter.image_to_webp_controller(self=None,
        file_name="test_assets/colosseum.jpg")
    assert response["success"] == True

def test_gif_to_mp4():
    response = converter.gif_to_mp4_controller(self=None,
        file_name="test_assets/animation.gif")
    assert response["success"] == True

def test_image_to_webp_custom_destination():
    response = converter.image_to_webp_controller(self=None,
        file_name="api.png", file_destination="/Users/sebastianchalarca/Documents/Coding_Projects/SEOptimizer/SEOptimizer/output")
    assert response["success"] == True

def test_gif_to_mp4_custom_destination():
    response = converter.gif_to_mp4_controller(self=None,
        file_name="test_assets/animation.gif", file_destination="/Users/sebastianchalarca/Documents/Presentation Components")
    assert response["success"] == True



