import pawpal_system
from datetime import datetime, timedelta

# Owner, pets, and scheduler setup
owner = pawpal_system.Owner(owner_id=1, name="Priscilla", email="diame2005@gmail.com")
pet1 = pawpal_system.Pet(pet_id=1, name="Rufus", species="Dog", age=5)
pet2 = pawpal_system.Pet(pet_id=2, name="Luna", species="Cat", age=3)
pet3 = pawpal_system.Pet(pet_id=3, name="Pam", species="Turtle", age=2)
owner.add_pet(pet1)
owner.add_pet(pet2)
owner.add_pet(pet3)

scheduler = pawpal_system.Scheduler()

# Add tasks out of order
tasks = [
    pawpal_system.Task(task_id=1, title="Walk Luna", scheduled_time=datetime.now() + timedelta(hours=6), priority=2),
    pawpal_system.Task(task_id=2, title="Feed Rufus", scheduled_time=datetime.now() + timedelta(hours=1), priority=5, frequency="daily"),
    pawpal_system.Task(task_id=3, title="Clean Pam's tank", scheduled_time=datetime.now() + timedelta(hours=4), priority=3),
    pawpal_system.Task(task_id=4, title="Vet check Rufus", scheduled_time=datetime.now() + timedelta(hours=6), priority=1),
    pawpal_system.Task(task_id=5, title="Luna play session", scheduled_time=datetime.now() + timedelta(hours=1), priority=4),
]

scheduler.add_task(pet2, tasks[0])
scheduler.add_task(pet1, tasks[1])
scheduler.add_task(pet3, tasks[2])
scheduler.add_task(pet1, tasks[3])
scheduler.add_task(pet2, tasks[4])

# Add a conflicting task to test warning
conflict_task = pawpal_system.Task(task_id=6, title="Conflict walk Luna", scheduled_time=tasks[0].scheduled_time, priority=1)
scheduler.add_task(pet2, conflict_task)

print("\n== Master task list sorted by time ==")
master = owner.get_all_tasks()
sorted_by_time = scheduler.sort_tasks_by_time(master)
for task in sorted_by_time:
    print(f"{task.title} ({task.frequency or 'one-time'}) - {task.scheduled_time.strftime('%Y-%m-%d %H:%M')} - {task.completed} - {task.priority}")

print("\n== Filter by pet: Luna ==")
for task in scheduler.filter_by_pet(owner, "Luna"):
    print(f"{task.title} at {task.scheduled_time.strftime('%H:%M')} ({'Done' if task.completed else 'Pending'})")

print("\n== Filter by status: pending ==")
for task in scheduler.filter_by_status(master, completed=False):
    print(f"{task.title} ({task.scheduled_time.strftime('%H:%M')})")

# Recurring task behavior
print("\n== Completing a recurring task (Feed Rufus) ==")
recurring = pet1.tasks[0]
new_task = recurring.mark_complete()
print(f"Marked complete: {recurring.title}, completed={recurring.completed}")
if new_task:
    print(f"Created new occurrence: {new_task.title} at {new_task.scheduled_time.strftime('%Y-%m-%d %H:%M')}")
    scheduler.add_task(pet1, new_task)

# Detect conflicts for owner
print("\n== Conflicts across owner tasks ==")
conflicts = scheduler.detect_conflicts_for_owner(owner)
for a, b in conflicts:
    print(f"Warning: '{a.title}' conflicts with '{b.title}' at {a.scheduled_time.strftime('%Y-%m-%d %H:%M')}")

print("\n== Final schedule by time for today and future ==")
for task in scheduler.sort_tasks_by_time(owner.get_all_tasks()):
    print(f"{task.title} - {task.scheduled_time.strftime('%Y-%m-%d %H:%M')} - completed={task.completed} - pet={(task.title.split()[1] if 'Rufus' in task.title or 'Luna' in task.title else 'Pam')}" )

