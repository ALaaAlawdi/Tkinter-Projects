from models.task import Task

class TaskController:
    def __init__(self, database_manager, main_page, add_task_page):
        self.database_manager = database_manager
        self.main_page = main_page
        self.add_task_page = add_task_page

    def load_tasks(self):
        tasks = self.database_manager.get_all_tasks()
        self.main_page.update_task_list(tasks)

    def show_add_task_page(self):
        self.main_page.pack_forget()  # إخفاء الصفحة الرئيسية
        self.add_task_page.pack()  # إظهار صفحة إضافة مهمة

    def show_main_page(self):
        self.add_task_page.pack_forget() # إخفاء صفحة إضافة مهمة
        self.main_page.pack() # إظهار الصفحة الرئيسية
        self.load_tasks() # تحديث قائمة المهام

    def add_task(self):
        title, description = self.add_task_page.get_task_data()
        if title:
            task = Task(title, description)
            self.database_manager.add_task(task)
            self.add_task_page.clear_entries() # مسح الإدخالات بعد الإضافة
            self.show_main_page() # العودة للصفحة الرئيسية وتحديث القائمة
        else:
            # ... عرض رسالة خطأ إذا كان العنوان فارغاً ...
            pass

    def complete_selected_task(self):
        try:
            selected_task_index = self.main_page.task_listbox.curselection()[0]
            selected_task_text = self.main_page.task_listbox.get(selected_task_index)
            # استخراج العنوان من النص المعروض في القائمة (هناك طرق أفضل لذلك)
            title = selected_task_text.split("(")[0].strip()
            self.database_manager.complete_task(title)
            self.load_tasks() # تحديث قائمة المهام بعد الإكمال
        except IndexError:
            # ... عرض رسالة خطأ إذا لم يتم تحديد مهمة ...
            pass