import os

def save_document(data):

    folder = f"knowledge/{data['category']}"

    os.makedirs(folder, exist_ok=True)

    filename = data["intent"].replace(" ", "_")

    path = os.path.join(folder, filename + ".md")

    with open(path, "w") as f:

        f.write(data["markdown"])

    return path