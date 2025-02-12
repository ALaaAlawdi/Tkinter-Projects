from models.item import Item

class DatabaseManager:  # In-memory data for now (replace with a real DB later)
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_all_items(self):
        return self.items

    def get_item(self, item_name):
      for item in self.items:
        if item.name == item_name:
          return item
      return None