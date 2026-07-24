class Person:
    """A simple person with a name and age."""

    def __init__(self , name, age):
        self.name = name
        self.age = age

    def display(self):
        return (f"Name: {self.name}\nAge: {self.age}")

class Employee(Person):
    """Base class for all employees."""

    def __init__(self, name, age, employee_id,salary=0.0):
        super().__init__(name, age)
        self.__employee_id = ""
        self.employee_id = employee_id
        self.__salary = 0.0
        self.salary = salary

    @classmethod
    def from_previous_information(cls, name,age,employee_id):
        print("Create an eployee when salary is not known yet.")
        return cls(name, age, employee_id)

    @classmethod
    def from_record(cls, record):
        print("Create an employee from a mapping- like record")
        return cls(record["name"], record["age"], record["employee_id"],record["salary"])

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        if not str(value).strip():
            raise ValueError("Employee ID cannot be empty")
        self.__employee_id = str(value).strip()

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,value):
        value = float(value)
        if value < 0:
            raise ValueError("salary cannot be negative.")
        self.__salary = value

    def display(self):
        return f"{super().display()}\nEmployee ID: {self.employee_id}\nSalary: ${self.salary:,.2f}"

    def __del__(self):

        self.name = None
        self.age = None

class Manager(Employee):
    print("An Employee responsible for a department.")

    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        return (f"{super().display()}\nRole: Manager\nDepartment:{self.department}")

class Developer(Employee):
    print("An employee with a primary programming language.")

    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        return (f"{super().display()}\nRole: Developer\nProgramming language: {self.programming_language}")

class EmployeeManagementSystem:
    print("Owns the employee collection and presents the console interfface.")

    def __init__(self):
        self.people = []

    @staticmethod
    def _read_int(prompt, minimum=0):
        while True:
            try:
                value = int(input(prompt))
                if value < minimum:
                    raise ValueError
                return value
            except ValueError:
                print(f"Please enter the whole number of at least{minimum}")

    @staticmethod
    def _read_salary():
        while True:
            try:
                value = float(input("salary: $"))
                if value < 0:
                    raise ValueError
                return value
            except ValueError:
                print("Please enter a non-negative amount.")

    def _read_common_employee_fields(self):
        name = input("Names: ").strip()
        age =self._read_int("Age: ", 0)
        employee_id = input("Employee ID: ").strip()
        salary = self._read_salary()
        return (name, age, employee_id, salary)

    def _find_employee(self, employee_id):
        return next ((p for p in self.people if isinstance(p, Employee) and p.employee_id == employee_id), None)

    def add_person(self):
        person = Person(input("Name: ").strip(), self._read_int("Age: ", 0))

        self.people.append(person)
        print("Person added.")

    def add_employee(self):
        name, age, employee_id, salary = self._read_common_employee_fields()

        if self._find_employee(employee_id):
            print("That employee ID already exists.")
            return
        self.people.append(Employee(name, age, employee_id, salary))
        print("Employee added")

    def add_manager(self):
        name, age, employee_id, salary = self._read_common_employee_fields()
        if self._find_employee(employee_id):
            print("That employee ID already exists")
            return
        self.people.append(Manager(name, age, employee_id, salary, input("Department: ").strip()))
        print("Manager added")


    def add_developer(self):
        name, age, employee_id, salary = self._read_common_employee_fields()
        if self._find_employee(employee_id):
                    print("That employee ID already exists")
                    return
        self.people.append(Developer(name, age, employee_id, salary, input("Programming language: ").strip()))
        print("Developer added")

    def show_details(self):
        if not self.people:
            print("No records found.")
            return
        for index, person in enumerate(self.people,start=1):
            print(f"\n--- Record {index} ---")
            print(person.display())

    def update_employee(self):
        employee = self._find_employee(input("Employee ID to update:").strip())
        if not employee:
            print("Employee not found.")
            return
        print("Leave a field blank to keep its current value.")
        name = input(f"Name [{employee.name}]:").strip()
        salary = input(f"Salary [{employee.salary:.2f}]: ").strip()
        if name:
            employee.name = name
        if salary:
            try:
                employee.salary = salary
            except ValueError as error:
                print(f"Update cancelled: {error}")
                return
        print("Employee update.")

    def remove_employee(self):
        employee = self._find_employee(input("Employee ID to remove:").strip())
        if not employee:
            print("Employee not found.")
            return
        self.people.remove(employee)
        print("Employee removed.")

    def demonstrate_inheritance(self):
        print(f"Manager is an Employee: {issubclass(Manager, Employee)}")
        print(f"Developer is an Employee: {issubclass(Developer, Employee)}")

    def run(self):
        actions = {
            "1": self.add_person, "2": self.add_employee, "3": self.add_manager, "4": self.add_developer, "5": self.show_details, "6": self.update_employee, "7": self.remove_employee, "8": self.demonstrate_inheritance,
        }
        while True:
            print("\n--- Employee Management System ---")
            print("1. Add a Person\n2. Add an Employee\n3. Add a Manager\n4. Add a Developer")
            print("5. Show Details\n6. Update an Employee\n7. Remove an Employee")
            print("8. Check Inheritance\n9. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "9":
                print("Exiting the system. Goodbye!")
                break
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice. Please chose 1 to 9.")

if __name__ == "__main__":
    EmployeeManagementSystem().run()
                      