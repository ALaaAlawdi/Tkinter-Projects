from fastapi import FastAPI
from models.item import Item # Import the Item model
from views.item_view import ItemView
from controllers.item_controller import ItemController
from database.database_manager import DatabaseManager

app = FastAPI()

database_manager = DatabaseManager()
item_controller = ItemController(database_manager)


app.include_router(item_controller.router) # Include the router

# Example usage (replace with real database interaction later)
item1 = Item("Laptop", "Powerful machine")
database_manager.add_item(item1)
item2 = Item("Mouse", "Wireless mouse")
database_manager.add_item(item2)