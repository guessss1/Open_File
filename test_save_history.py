import os
import json

def save_history(file_save, link, file):
    history = []
    history.append({"Name_file": os.path.basename(file),
                    "save_file_history": os.path.basename(file_save),
                    "link": link})
    with open(file_save, "w") as f:
        json.dump(history, f, indent=4)

def test_save_history():
    t_file_save = "test_file.json"
    t_link = "https://file.io/9jaHyVk3PC1S"
    t_file_name = "3.3.py"

    save_history(t_file_save, t_link, t_file_name)


test_save_history()
