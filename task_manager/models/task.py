

class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):  # لطباعة معلومات المهمة بسهولة
        return f"{self.title} ({'مكتملة' if self.completed else 'غير مكتملة'})"