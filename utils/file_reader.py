def read_input(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read().strip()
