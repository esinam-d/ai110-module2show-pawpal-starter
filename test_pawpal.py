from datetime import datetime, timedelta

from pawpal_system import Pet, Task


def test_mark_complete_sets_completed_true():
    task = Task(task_id=1, title='Feed dog', scheduled_time=datetime.now(), priority=5, completed=False)
    assert not task.completed

    task.mark_complete()
    assert task.completed


def test_add_task_increases_task_count():
    pet = Pet(pet_id=1, name='Buddy', species='Dog', age=4)
    initial_count = len(pet.tasks)

    task = Task(task_id=1, title='Brush fur', scheduled_time=datetime.now(), priority=3)
    pet.add_task(task)

    assert len(pet.tasks) == initial_count + 1
    assert pet.tasks[-1] is task
