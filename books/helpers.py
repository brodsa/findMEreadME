import string
import random
import os


def get_id():
    """ Function to get id from text file """
    with open("./books/data/book_key_seed.txt", 'r') as file:
        id_seed = file.read()
        return id_seed


def update_id(new_id_seed):
    """ Function to update id from text file """
    with open("./books/data/book_key_seed.txt", 'w') as file:
        file.write(new_id_seed)


def generate_key(id_book, key_length=8):
    """
    Function to generate a key
    """
    id_seed = get_id()
    random.seed(id_seed)
    chars = string.ascii_letters + string.digits
    chars_selected = "".join(random.choices(chars, k=key_length))
    key = f"{id_book}-{chars_selected[:4]}-{chars_selected[4:]}-{id_seed}"
    new_id = int(id_seed.strip()) + 1
    update_id(str(new_id))
    return key
