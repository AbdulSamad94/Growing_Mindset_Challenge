import json


def load_users(file_path="users.json"):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Return an empty dict if file not found


def save_users(users, file_path="users.json"):
    with open(file_path, "w") as f:
        json.dump(users, f, indent=4)


def load_data(file_path="data.json"):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"entries": []}


def save_data(data, file_path="data.json"):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
