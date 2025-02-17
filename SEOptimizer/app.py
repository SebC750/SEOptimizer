from controllers.converter_controller import ConverterController

converter = ConverterController()


def custom_file_destination_prompt():
    unique_file_directory_choice = input(
        "Would you like to say where the file should be? Y/N (By default, the program will output it in the Documents folder.)")
    match unique_file_directory_choice.lower().strip():
        case "y":
            custom_file_destination = input("What is the file destination?")
            return custom_file_destination
        case "n":
            return None
        case _:
            raise ValueError("Please answer with Y/y for yes and N/n for no.")


def menu():
    print("| ------------------------------------------------ |")
    print("| SEOptimizer                                      |")
    print("| ------------------------------------------------ |")
    print("| 1) Convert from gif to mp4                       |")                     
    print("| 2) Convert image to webp                         |")               
    print("| 3) Exit                                          |")
    print("| ------------------------------------------------ |\n")


def main():

    choice = 0
    while True:
        menu()
        choice = int(input("Select file conversion type: "))
        match choice:
            case 1:
                try:

                    file_name = input(
                        "Choose gif file to convert. Include the file extension: ")
                    print("Selected file directory: ", file_name)
                    custom_file_destination = custom_file_destination_prompt()
                    converter.gif_to_mp4_controller(
                        file_name, custom_file_destination)

                except TypeError as type_error_message:
                    print("Please input a valid directory. Must be a string.")
                    print("Full error message: ", str(type_error_message))
                finally:
                    print("Request complete.")
            case 2:
                try:

                    print("Converting image to webp...")
                    file_name = input(
                        "Choose file to convert. Include the file extension: ")
                    custom_file_destination = custom_file_destination_prompt()
                    converter.image_to_webp_controller(
                        file_name, custom_file_destination)

                except TypeError as type_error_message:
                    print("Please input a valid directory. Must be a string.")
                    print("Full error message: ", str(type_error_message))
                finally:
                    print("Request complete.")
            case 3:
                exit_choice = input(
                    "Are you sure you want to exit the program? Y/N\n")
                if (exit_choice.lower().strip() == "n"):
                    continue
                else:
                    print("Goodbye!")
                    exit()
            case _:
                raise ValueError("Please choose an option from the menu.")

if __name__ == "__main__":
    main()
