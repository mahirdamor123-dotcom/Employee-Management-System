# Employee Management System

A menu-driven Python project that demonstrates Object-Oriented Programming (OOP) concepts.

## Features

- Create a Person
- Create an Employee
- Create a Manager
- Create a Developer
- View all saved records
- Update employee details
- Remove an employee
- Check inheritance using `issubclass()`

## OOP Concepts Used

- Classes and objects
- Inheritance
- Encapsulation using private attributes
- Getter and setter methods using `@property`
- Method overriding
- `super()`
- `issubclass()`
- Constructors and destructor

## Classes

- `Person` – stores name and age.
- `Employee` – inherits from `Person` and adds employee ID and salary.
- `Manager` – inherits from `Employee` and adds department.
- `Developer` – inherits from `Employee` and adds programming language.

## How to Run

1. Install Python.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python project-5.py
```

5. Choose options from the menu to manage employee records.

## Assumptions

- Employee IDs must be unique.
- Age must be a non-negative whole number.
- Salary must be a non-negative number.
- Records are stored only while the program is running.
