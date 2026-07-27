import random


data = []


def generate_id():
    return "".join(random.choices("0123456789", k=6))


def is_valid(val):
    if val is None or val.strip() == "":
        return False
    return True


def find(id_val):
    for i in range(len(data)):
        if data[i] is not None and data[i]["id"] == id_val:
            return i
    return -1
