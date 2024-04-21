from task import Task

class Section:
    def __init__(self, name:str):
          self.name = name
          self.tasks = []
          
    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        
    def complete_task(self, task_name: str):
        if task_name not in self.tasks:
            return f"Could not find task with the name {task_name}"
        else:
            task_name.completed = True
            return f"Completed task {task_name}"
        
    def clean_section(self):
        removed_tasks = 0
        
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                removed_tasks+=1
                
        return f"Cleared {removed_tasks} tasks."
    
    def view_section(self):
        
        summary =  f"Section {self.name}:"
        for task in self.tasks:
            summary+= f"\n{task.details()}"
            
        return summary

