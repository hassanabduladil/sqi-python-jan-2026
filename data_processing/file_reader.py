def read_data(file_path):
    with open("data.txt", "r", encoding="utf-8") as f:
        contents = f.readlines()
        names_and_ages = [tuple(content.strip().split(",")) for content in contents]
        return names_and_ages