import os

# removes files in designated filepath(s)
def remove_files(*filepaths):
    for path in filepaths:
        if isinstance(path, str) and os.path.exists(path): # ensure the path exists
            os.remove(path)
            print(f"Removed {path}")
