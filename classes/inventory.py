import csv
import os

class Inventory:
    def __init__(self, id,title,rating,release_year,copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = copies_available

# Used to get all of the inventory info in the store class

    @classmethod
    def get_inventory_list(cls):
        videos = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")

        with open(path, 'r') as inventory_file:
            inventory_reader = csv.DictReader(inventory_file)
            for video in inventory_reader:
                videos.append(Inventory(**dict(video)))
        return videos


