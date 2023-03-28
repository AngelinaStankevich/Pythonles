from enum import Enum, IntEnum


class PriorityEnum(IntEnum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class Task:
    def __init__(self, name_task: str, task: str, priority_task: PriorityEnum):
        self.name_task = name_task
        self.task = task
        self.priority_task = priority_task

    def __repr__(self):
        return f"{self.task}{self.name_task}{self.priority_task}"


class ToDoList:

    def __init__(self):
        self.to_do_list: list[Task] = []

    def add_list(self, task: Task):
        self.to_do_list.append(task)

    def edit_task(self, task: Task, new_task: str):
        if task in self.to_do_list:
            self.to_do_list[self.to_do_list.index(task)].task = new_task

    def priority_task(self, task: Task, new_priority: Enum):
        if task in self.to_do_list:
            self.to_do_list[self.to_do_list.index(task)].task = new_priority

    def del_task(self, task: Task):
        if task in self.to_do_list:
            self.to_do_list.remove(task)

    def get_list(self) -> list[Task]:
        return sorted(self.to_do_list, key=lambda task: task.priority_task, reverse=True)


task = Task("first", "new_first", PriorityEnum.LOW)
task1 = Task("first", "new first", PriorityEnum.MEDIUM)
task2 = Task("first", "new first", PriorityEnum.HIGH)
task3 = Task("first", "new first", PriorityEnum.LOW)

to_do_list = ToDoList()
to_do_list.get_list()
to_do_list.add_list(task)
to_do_list.add_list(task1)
to_do_list.add_list(task2)

print(to_do_list.get_list())
print(to_do_list.to_do_list)
