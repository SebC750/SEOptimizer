from ffmpy import FFmpeg
from pathlib import Path
import os

default_directory = Path.home() / "Documents"

class FileConverterRepository:
    def __init__(self):
        print("File converter created.")

    def gif_to_mp4(self, file_name, file_destination):
        print("Selected file: ", file_name, "\n")
        print("Converting gif to mp4....\n")
        try:
            if not os.path.exists(file_name):
                print(f"ERROR: File '{file_name}' not found!")
                return {"success": False, "error": "File not found"}

            file_destination = file_destination or default_directory
            output_string = os.path.join(file_destination, f"{Path(file_name).stem}.mp4")

            os.makedirs(os.path.dirname(output_string), exist_ok=True)

            conversion_process = FFmpeg(
                inputs={file_name: None},
                outputs={output_string: '-c:v libx264 -pix_fmt yuv420p -b:v 1M -c:a aac -b:a 128k'}
            )
            conversion_process.run()
            print("Yay! Your file has been converted!")
            return {"success": True}
            
        except Exception as e:
            print(f"ERROR MESSAGE: {e}")
            return {"success": False, "error": str(e)}

    def image_to_webp(self, file_name, file_destination):
        print("Selected file: ", file_name, "\n")
        print("Converting image to webp....\n")
        try:
            if not os.path.exists(file_name):
                print(f"ERROR: File '{file_name}' not found!")
                return {"success": False, "error": "File not found"}

            file_destination = file_destination or default_directory
            output_string = os.path.join(file_destination, f"{Path(file_name).stem}.webp")

            os.makedirs(os.path.dirname(output_string), exist_ok=True)

            conversion_process = FFmpeg(
                inputs={file_name: None},
                outputs={output_string: None}
            )
            conversion_process.run()
            print("Yay! Your file has been converted!")
            return {"success": True}

        except Exception as e:
            print(f"ERROR MESSAGE: {e}")
            return {"success": False, "error": str(e)}

if __name__ == "__main__":
    pass
