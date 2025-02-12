from fastapi import APIRouter, Depends
from views.item_view import ItemView
from models.item import Item

class ItemController:
    def __init__(self, database_manager):
        self.database_manager = database_manager
        self.router = APIRouter()  # FastAPI router for this controller
        self.add_routes()

    def add_routes(self): # Define routes after the manager is available.
      self.router.add_api_route("/items", self.get_items, methods=["GET"])
      self.router.add_api_route("/items", self.create_item, methods=["POST"])
      self.router.add_api_route("/items/{item_name}", self.get_item, methods=["GET"])

    def get_items(self):
        items = self.database_manager.get_all_items()
        return ItemView().format_item_list(items)

    def get_item(self, item_name: str):
      item = self.database_manager.get_item(item_name)
      if item:
        return ItemView().format_item(item)
      return ItemView().format_error("Item Not Found")

    def create_item(self, item: dict):  # FastAPI handles request body parsing
        new_item = Item(item["name"], item["description"])
        self.database_manager.add_item(new_item)
        return ItemView().format_item(new_item) # Return the created item