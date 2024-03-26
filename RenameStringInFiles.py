import os

def rename_string_in_files(directory, old_string, new_string):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file:
                file_content = file.read()

            new_content = file_content.replace(old_string, new_string)

            with open(filepath, 'w') as file:
                file.write(new_content)

if __name__ == "__main__":
    # Replace 'your_directory' with the path to the directory containing your files
    directory = 'G:/example/files'

    # Replace 'Hello' with the string you want to rename, and 'NewString' with the new string
    old_string = 'Hello'
    new_string = 'NewString'

    rename_string_in_files(directory, old_string, new_string)
