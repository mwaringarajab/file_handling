def read_and_modify_file():
    # Ask user for filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Modify each line (e.g., make it uppercase)
        modified_lines = [line.upper() for line in lines]

        # Write the modified content to a new file
        new_filename = f"modified_{filename}"
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_lines)

        print(f"Modified content has been saved to: {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
