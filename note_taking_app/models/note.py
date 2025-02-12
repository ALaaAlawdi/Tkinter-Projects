class Note:
    def __init__(self, title="Untitled Note", content=""):  # Default values!
        self.title = title
        self.content = content

    def __str__(self):  # For displaying in the listbox
        return self.title

    def to_dict(self):  # For saving to JSON
        return {"title": self.title, "content": self.content}

    @classmethod
    def from_dict(cls, data):  # For loading from JSON
        return cls(data["title"], data["content"])