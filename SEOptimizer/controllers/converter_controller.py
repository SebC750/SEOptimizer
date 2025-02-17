from models import file_converter

class ConverterController:

    def image_to_webp_controller(self, file_name, file_destination=None):
        try:
            print("Now handling file to webp")
            repository = file_converter.FileConverterRepository()     
            response = repository.image_to_webp(file_name, file_destination)
            return response
        except Exception as e:
            print(f"ERROR MESSAGE: {e}")

    def gif_to_mp4_controller(self, file_name, file_destination=None):
        try:
            print("Now handling gif to mp4")
            repository = file_converter.FileConverterRepository() 
            response = repository.gif_to_mp4(file_name, file_destination)
            return response
        except Exception as e:
            print(f"ERROR MESSAGE: {e}")


