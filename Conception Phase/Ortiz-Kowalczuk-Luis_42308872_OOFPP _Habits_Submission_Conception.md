# Overview

This document describes the concept of a habit tracing application called **HTrack**. It is going to cover the back-end engine written in Python without a dedicated GUI. During the development phase, Tkinter will be used for testing and presentation of the solution.

# Architecture

The **HTrack** app is going to consist of the following elements:
- Python modules:
   - main.py - Main module from which rest of the modules are going to be initiated. It will also be a placeholder of any additional code to be run during the initialization of the application.
   - gui.py - Module containing GUI elements.
   - habits.py - Module containing the *habit* class declaration.
   - tasks.py - Module containing the *task* class declaration.
   - db.py - Module containing functions operating any database related operations.
   - tests.py - Module contsining tests using the *pytest* module
- db folder - Folder containing all the apps data.
   
# Minimum Viable Product

The MVP of this solution is going to contain the following functionalities:
- A user can define multiple habits in the application. A habit has a task specification and a periodicity.
-  For each habit, the app will track when it has been created, and the date and time the habit tasks have been completed.  
- A task can be completed, i.e., “checked-off”, by a user at any point in time.
- Each task needs to be checked-off at least once during the period the user defined for the respective habit. If a user misses to complete a habit during the specified period, the user is said to break the habit.
- If a user manages to complete the task of a habit x consecutive periods in a row, i.e., without breaking the habit, we say that the user established a streak of x periods. For instance, if a user wants to work out every day and does so for two full weeks, they establish a 14-day streak of working out.
- The habits users enter in the app are not only stored but can also be analysed:
   - return a list of all currently tracked habits,
   - return a list of all habits with the same periodicity,
   - return the longest run streak of all defined habits,
   - return the longest run streak for a given habit. 

# Optional Functionalities

In addition to the MVP, the following functionalities will be considered depending on the team work capacity:
- Periodicity is fully customizable by any repeatable frequency of hours, days, weeks, months, and years.
- Each user can have a separate profile with individual data.
- Profiles can be compared between each other.
- The periods between tasks of a habit can be changed at any time without the loss of data.
- An additional streak calculaion will be added that will take into account the periodicity. The higher amount of completed tasks the greater the weight of the streak.
- A notification system that will remind the user that the task is close to its due date/time.

# GUI

This solution will not support any GUI solution. For the purpose of testing and presentation, Tkinter will be used with generic elements.

# Database

At this stage, there are 2 solutions taken under consideration:
- SQL database
- JSON files

Using SQL is a more efficient and universal solution, but when the SQL files handling is going to be proven too complex, JSON will be used instead.

# Workflow

The lifecycle of a successfully completed habit is as follows:

```mermaid
graph TD;
   Trigger new habbit-->Fill out the following data;
```