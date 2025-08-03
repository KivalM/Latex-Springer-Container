# /// script
# requires-python = ">=3.11"
# dependencies = [
# "pyoverleaf[cli]",
# ]
# ///

import pyoverleaf
import glob
import os

def main() -> None:
    api = pyoverleaf.Api()
    api.login_from_browser()

    this_id = "688f46fd8b2d893c3e3564f6"
    print(f"Using project ID: {this_id}")

    root_folder = api.project_get_files(this_id)

    files_to_upload = glob.glob("**/*.*", recursive=True)
    files_to_upload = [
        f for f in files_to_upload
        if not f.startswith('output' + os.sep) and f != 'sync.py'
    ]

    print("Files to be uploaded:")
    for f in files_to_upload:
        print(f)

    for file_path in files_to_upload:
        print(f"Processing {file_path}...")
        
        # Get directory and file name
        directory, file_name = os.path.split(file_path)

        # Create folder structure on Overleaf
        current_folder = root_folder
        if directory:
            for part in directory.split(os.sep):
                # Check if folder exists
                folder = next((f for f in current_folder.children if f.name == part and f.type == 'folder'), None)
                if not folder:
                    print(f"Creating folder: {part} in {current_folder.name}")
                    folder = api.project_create_folder(this_id, current_folder.id, part)
                    current_folder.children.append(folder)
                current_folder = folder

        # Check if file exists and delete it to ensure a clean upload
        file_to_delete = next((f for f in current_folder.children if f.name == file_name and f.type == 'file'), None)
        if file_to_delete:
            print(f"Deleting existing file: {file_path}")
            api.project_delete_entity(this_id, file_to_delete)

        # Upload the new file
        print(f"Uploading {file_path} to {current_folder.name}...")
        try:
            with open(file_path, "rb") as f:
                content = f.read()
            api.project_upload_file(this_id, current_folder.id, file_name, content)
            print(f"Successfully uploaded {file_path}")
        except Exception as e:
            print(f"Error uploading {file_path}: {e}")


if __name__ == "__main__":
    main()
