import string
import random


def generate_key(key_length=8):
    """
    Function to generate a key 
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(characters, k=key_length))
    return password