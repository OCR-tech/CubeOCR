import os

def replace_in_file(file_path, old_text, new_text):
    """
    Replaces all occurrences of old_text with new_text in the specified file.

    Args:
        file_path (str): Path to the file.
        old_text (str): Text to be replaced.
        new_text (str): Replacement text.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace the text
    updated_content = content.replace(old_text, new_text)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

def replace_in_project(directory, old_text, new_text):
    """
    Recursively replaces all occurrences of old_text with new_text in all files in the directory.

    Args:
        directory (str): Path to the project directory.
        old_text (str): Text to be replaced.
        new_text (str): Replacement text.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):  # Only process Python files
                file_path = os.path.join(root, file)
                replace_in_file(file_path, old_text, new_text)
                print(f"Updated: {file_path}")

# Replace 'flag_setting_init' with 'FLAG_SETTING_INIT' in the project directory
project_directory = r'D:\Workspace\app\src'
replace_in_project(project_directory, 'old_text', 'new_text')
