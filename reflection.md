# PawPal+ Project Reflection

## 1. System Design
This program allows nthe user to add a pet, schedule walks with ntheir pet and schedule a feeding time.

**a. Initial design**

- Briefly describe your initial UML design.
ans.) Task: This represents individual pet care activities. Responsible for tracking details, completion, and scheduling info.
Pet: Represents a pet. Responsible for storing personal infor and tasks, adding/ and removing tasks, and reporting the tasks due today.
Owner: Represents the owner. Responisble for managing multiple pts and retrieving all tasks across pets.
Scheduler: This is responsible for sorting tasks, detecting conflicts, handling recurring tasks, and generating daily schedules

- What classes did you include, and what responsibilities did you assign to each?

**b. Design changes**

- Did your design change during implementation?

Ans.) Yes, the designed was refined after reviewing AI feedback.

- If yes, describe at least one change and why you made it.

Ans.) Based on the feedback, I clarified that:
- Pet methods such as add_task() and remove_task() should directly modify the pet's internal task list.
- Owner.get_all_tasks() should be a combination of tasks from all owned pets instead of storing duplicate task data.
- Scheduler methods should explicitly define how tasks are added and processed, ensuring clear data flow between classes.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
