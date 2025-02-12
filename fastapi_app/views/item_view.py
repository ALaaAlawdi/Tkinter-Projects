from fastapi.responses import JSONResponse

class ItemView:  # Think of this as a "response formatter"
    def format_item(self, item):
        return JSONResponse(content=item.to_dict())

    def format_item_list(self, items):
        item_list = [item.to_dict() for item in items]
        return JSONResponse(content=item_list)

    def format_error(self, message):
        return JSONResponse(content={"error": message}, status_code=400) # Example error response