
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_name_and_id(self):
        print(f"Name: {self.name}\nID: {self.id}")


class Employee(Person):
    def __init__(self, name, id, salary, title):
        super().__init__(name, id)
        self.salary = salary
        self.title = title

test_person = Person("Joe", 1)
second_test_person = Employee("Jim", 3, 50000, "Accountant")

test_person.display_name_and_id()
second_test_person.display_name_and_id()