import string
import random
import os
import json


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


def convert_geonames():
    """
        A function to convert original countries json into djnago json format.
        Is called only once and manually convert_geonames()
    """
    # open source data
    with open("./data/geonames.json") as file:
        data_js = json.load(file)
        records = []
        i = 0

        # create records for django json format
        for item in data_js:
            if item["cou_name_en"] in ('Ireland', 'Czech Republic', 'Austria') and int(item["population"])>20000:
                record = {
                    'model': 'books.city',
                    'pk': i,
                    'fields': {
                        'city': item["name"],
                        'country': item["cou_name_en"]
                    }
                }
                i += 1
                records.append(record)

        # write the new json into new json file
        with open('./fixtures/cities.json', 'w') as django_js:
            django_js.write(json.dumps(records))