classDiagram
    class Owner {
        +owner_id
        +name
        +email
        +add_pet()
        +remove_pet()
    }

    class Pet {
        +pet_id
        +name
        +species
        +age
        +medical_notes
        +add_task()
        +remove_task()
    }

    class Task {
        +task_id
        +title
        +task_type
        +scheduled_time
        +priority
        +recurring
        +completed
        +mark_complete()
        +is_due_today()
    }

    class Scheduler {
        +add_task()
        +sort_tasks_by_priority()
        +detect_conflicts()
        +generate_daily_schedule()
    }

    Owner "1" --> "*" Pet : owns
    Pet "1" --> "*" Task : assigned
    Scheduler --> Task : manages