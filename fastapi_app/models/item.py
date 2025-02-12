class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_dict(self):  # For easy serialization to JSON
        return {"name": self.name, "description": self.description}