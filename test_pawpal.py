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


def test_sort_tasks_by_time():
    tasks = [
        Task(task_id=1, title='A', scheduled_time=datetime(2026, 4, 1, 12, 0), priority=1),
        Task(task_id=2, title='B', scheduled_time=datetime(2026, 4, 1, 8, 0), priority=1),
    ]
    from pawpal_system import Scheduler
    s = Scheduler()
    sorted_tasks = s.sort_tasks_by_time(tasks)
    assert [t.task_id for t in sorted_tasks] == [2, 1]


def test_filter_by_status():
    tasks = [
        Task(task_id=1, title='A', scheduled_time=datetime.now(), priority=1, completed=False),
        Task(task_id=2, title='B', scheduled_time=datetime.now(), priority=1, completed=True),
    ]
    from pawpal_system import Scheduler
    s = Scheduler()
    pending = s.filter_by_status(tasks, completed=False)
    assert len(pending) == 1


def test_mark_complete_daily_recurs():
    task = Task(task_id=10, title='Daily walk', scheduled_time=datetime(2026, 4, 1, 9, 0), priority=4, frequency='daily')
    new_task = task.mark_complete()
    assert task.completed is True
    assert new_task is not None
    assert new_task.frequency == 'daily'
    assert new_task.scheduled_time.date() == datetime(2026, 4, 2, 9, 0).date()
