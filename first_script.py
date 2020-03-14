class Person:
    # scope = ["people", "something"]
    def __init__(self, name="", surname="", age=None, position=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.position = position

    def __str__(self):
        return f"<Person with name {self.name}>"

    def full_name(self):
        return f"{self.name} {self.surname}"

    def get_older(self, years):
        self.age += years

    # def __add__(self, other):
    #     return Person(x=self.name+other.name, y=1, z=2)

class Employee(Person):
    def get_older(self, years=1):
        self.age += years

class ITEmployee(Employee):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skills = []


if __name__ == "__main__":
    e1 = ITEmployee("Olya", 25, "QA")
    print(e1.name)

# p2 = Person()
# print(p2.name)


# p1.set_name(["Vasya"])
# print(p1.name)
# p1.scope.append(1)

# p2.set_name(["657t6"])
# print(p2.scope)
# print(p1.scope is p2.scope)
