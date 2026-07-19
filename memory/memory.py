from memory.profile import remember, recall_all


def save_memory(text):

    remember("note", text)


def read_memory():

    data = recall_all()

    if not data:
        return "Memory is empty."

    result = ""

    for key, value in data.items():
        result += f"{key}: {value}\n"

    return result