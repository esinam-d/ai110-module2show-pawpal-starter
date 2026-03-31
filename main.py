import pawpal_system
from datetime import datetime, timedelta

# Create an owner:
owner = pawpal_system.Owner(owner_id=1, name="Priscilla", email="diame2005@gmail.com")

# Create a 3 pets and add it to the owner:
pet1 = pawpal_system.Pet(pet_id=1, name="Rufus", species="Dog", age=5)
owner.add_pet(pet1)

pet2 = pawpal_system.Pet(pet_id=2, name="Luna", species="Cat", age=3)
owner.add_pet(pet2)

pet3 = pawpal_system.Pet(pet_id=3, name="Pam", species="Turtle", age=2)
owner.add_pet(pet3)

# Add tasks to pets
task1= pawpal_system.Task(task_id=1, title="Feed Rufus dog treats", scheduled_time=datetime.now() + timedelta(hours=3), priority=1)

task2= pawpal_system.Task(task_id=2, title="Walk Luna around Lake Hollingsworth", scheduled_time=datetime.now() + timedelta(hours=2), priority=2)

task3= pawpal_system.Task(task_id=3, title="Clean Pam's turtle case ", scheduled_time=datetime.now() + timedelta(hours=3), priority=3)

task4= pawpal_system.Task(task_id=4, title="Book Rufus's vet appointment for next week", scheduled_time= datetime.now() + timedelta(hours=4), priority=1)

task5= pawpal_system.Task(task_id=5, title="Buy Luna's cat food", scheduled_time= datetime.now() + timedelta(days=5), priority=5) #Low priority because theres still some cat food left, enough to last a few more days.

task6= pawpal_system.Task(task_id=6, title="Buy Pam's turtle food", scheduled_time= datetime.now() + timedelta(days=1), priority=2) #Medium priority because Pam is running low on turtle food, but she still has some left.

scheduler = pawpal_system.Scheduler()
scheduler.add_task(pet1, task1)
scheduler.add_task(pet2, task2)
scheduler.add_task(pet3, task3)
scheduler.add_task(pet1, task4)
scheduler.add_task(pet2, task5)
scheduler.add_task(pet3, task6)



#Print all tasks for the owner
print("Today's Schedule")
for pet in owner.pets: #Iterate through each pet
    print(f"\nTasks for {pet.name}:")
    for task in pet.get_tasks_for_today(): #Get tasks for today for each pet
        print(f"- {task.title} at {task.scheduled_time.strftime('%H:%M')} (Priority: {task.priority})")
