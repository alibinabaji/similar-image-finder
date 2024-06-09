import shutil

def save_uploaded_file(uploaded_file, save_path):
    with open(save_path, "wb") as f:
        shutil.copyfileobj(uploaded_file, f)
