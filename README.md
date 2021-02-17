# Estimation-tracker
The goal of this project is to create an estimation tracker to help a developer using it to give better time estimations when someone is asking him/her "How much time is needed to do a task". As developers, we usually underestimate the time needed.

You can use any web framework to create this project. preferred Django or Flask.

To complete this project, these features are required on the same view:
- Create a task
  - Obligatory inputs: Name of the task, Planning Time, Self Estimated Time, Real time spent
  - Optional inputs: Notes, Level, Risk
  - Calculated inputs: Estimated time by calc

- List task

Tasks displayed in the list are sorted by date (most recent to older ones)

Each row should display the following info:

- Name of the task: String
- Planning Time: HH:MM:SS, Time needed to plan work for this task
- Self Estimated Time: HH:MM:SS, Time estimation given by the developer
- Real Time spent HH:MM:SS, Real time spent to complete the task (To add when the task is completed)
- Level: String, Estimation of complexity of the task, can be "Easy", "Medium" or "Hard"
- Risk of exceeding estimated time: String, Estimation of risk, can be "Not risky", "OK", "Risky", "Very risky"
Calculated info:

- Correctness: Percentage %, Ratio of real time over the estimated time
- Estimated time by calc: HH:MM:SS, Estimated time for subsequent tasks using Correctness and Self estimated time to predict the estimated time
 
Examples:

| Name |	Planning Time | Self Estimated	Time | Estimated Time By Calc | Real Time HH:SS	| Risk | Level | Correctness % | Notes |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Total | - | - | - | - | - | - | 186% | - |
| Coding Challenge |	02:00:00 | 00:01:00 | | 00:02:00 | OK | Easy | 200% | Harder than expected  |
| Add a contact form view to CC.on |	00:10:00 | 00:25:00 | 00:50:00| 00:43:00 | OK | Easy | 172% | Issue about sendgrid to allow email on behalf on someone else  |
