from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timedelta

""" TASK CLASS """
@dataclass
class Task:
    task_id: int
    title: str
    scheduled_time: datetime
    priority: int
    completed: bool = False  # default value
    frequency: str | None = None  # 'daily', 'weekly', or None

    def mark_complete(self) -> "Task | None":
        """Mark task as completed and create next recurring task if applicable."""
        self.completed = True
        return self.create_next_occurrence()

    def create_next_occurrence(self) -> "Task | None":
        """Return a new task instance for the next occurrence if recurring."""
        if self.frequency == "daily":
            next_time = self.scheduled_time + timedelta(days=1)
        elif self.frequency == "weekly":
            next_time = self.scheduled_time + timedelta(weeks=1)
        else:
            return None

        return Task(
            task_id=self.task_id + 1000,
            title=self.title,
            scheduled_time=next_time,
            priority=self.priority,
            completed=False,
            frequency=self.frequency,
        )

    def reschedule(self, new_time: datetime) -> None:
        """Set a new scheduled time for the task."""
        self.scheduled_time = new_time

    def is_due_today(self) -> bool:
        """Check whether task is due today."""
        return self.scheduled_time.date() == datetime.now().date()

"""PET CLASS """
@dataclass
class Pet:
    pet_id: int
    name: str
    species: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Attach a task to this pet."""
        self.tasks.append(task)

    def remove_task(self, task_id: int) -> None:
        """Remove a task by its task_id."""
        self.tasks = [t for t in self.tasks if t.task_id != task_id]

    def get_tasks_for_today(self) -> list[Task]:
        """Return pet tasks scheduled for today."""
        return [task for task in self.tasks if task.is_due_today()]


"""OWNER CLASS"""
class Owner:
    def __init__(self, owner_id: int, name: str, email: str) -> None:
        self.owner_id = owner_id
        self.name = name
        self.email = email
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        self.pets.append(pet)

    def remove_pet(self, pet_id: int) -> None:
        """Remove a pet by its pet_id."""
        self.pets = [pet for pet in self.pets if pet.pet_id != pet_id]

    def get_all_tasks(self) -> list[Task]:
        """Collect all tasks from all pets."""
        tasks: list[Task] = []
        for pet in self.pets:
            tasks.extend(pet.tasks)
        return tasks


"""SCHEDULER CLASS"""
class Scheduler:
    def sort_tasks_by_time(self, tasks: list[Task]) -> list[Task]:
        """Return tasks sorted by scheduled time."""
        return sorted(tasks, key=lambda t: t.scheduled_time)

    def add_task(self, pet: Pet, task: Task) -> None:
        """Delegate task addition to a pet with conflict check."""
        if self.has_conflict(pet, task):
            print(f"Warning: conflict detected for {pet.name} at {task.scheduled_time}. Task not added.")
            return
        pet.tasks.append(task)

    def sort_tasks_by_priority(self, tasks: list[Task]) -> list[Task]:
        """Return tasks sorted by descending priority."""
        return sorted(tasks, key=lambda t: t.priority, reverse=True)

    def detect_conflicts(self, tasks: list[Task]) -> list[tuple[Task, Task]]:
        """Find tasks that share the same scheduled time."""
        """Find tasks that share the same scheduled time."""
        conflicts: list[tuple[Task, Task]] = []
        sorted_tasks = sorted(tasks, key=lambda t: t.scheduled_time)
        for i in range(len(sorted_tasks)):
            for j in range(i + 1, len(sorted_tasks)):
                if sorted_tasks[i].scheduled_time == sorted_tasks[j].scheduled_time:
                    conflicts.append((sorted_tasks[i], sorted_tasks[j]))
        return conflicts

    def generate_daily_schedule(self, owner: Owner, date: datetime) -> list[Task]:
        """Assemble today's tasks for an owner and sort them."""
        daily = [task for task in owner.get_all_tasks() if task.scheduled_time.date() == date.date()]
        return self.sort_tasks_by_priority(daily)
    
    def filter_by_pet(self, owner, pet_name):
        """
        Return all tasks belonging to a specific pet.
          """
        for pet in owner.pets:
            if pet.name == pet_name:
                return pet.tasks
        return []
    
    def filter_by_status(self, tasks, completed=False):
        """
          Return tasks filtered by completion status.
            """
        return [task for task in tasks if task.completed == completed]
    
    def has_conflict(self, pet, new_task):
        """Check if a new task conflicts with existing tasks for a pet."""
        for task in pet.tasks:
            if task.scheduled_time == new_task.scheduled_time:
                return True
        return False

    def detect_conflicts_for_owner(self, owner: Owner) -> list[tuple[Task, Task]]:
        """Find conflicting tasks across all pets for an owner."""
        all_tasks = owner.get_all_tasks()
        return self.detect_conflicts(all_tasks)
    