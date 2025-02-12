import sqlite3
from models.task import Task

class DatabaseManager:
    def __init__(self, db_name="tasks.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                completed BOOLEAN NOT NULL
            )
        """)
        self.conn.commit()

    def add_task(self, task):
        self.cursor.execute("INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)",
                            (task.title, task.description, task.completed))
        self.conn.commit()

    def get_all_tasks(self):
        self.cursor.execute("SELECT title, description, completed FROM tasks")
        rows = self.cursor.fetchall()
        tasks = [Task(row[0], row[1], bool(row[2])) for row in rows]
        return tasks

    def complete_task(self, title): # مثال لإكمال مهمة معينة
        self.cursor.execute("UPDATE tasks SET completed = TRUE WHERE title = ?", (title,))
        self.conn.commit()

    def close(self):
        self.conn.close()