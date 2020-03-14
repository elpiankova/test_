import datetime

# print(datetime.datetime.now().year)


class Person:
    def __init__(self, birth_year=None, skills=None):
        self.time_created = datetime.datetime.now()
        self.birth_year = birth_year
        if skills is None:
            self.skills = []
        else:
            self.skills = skills

    def age(self, year=None):
        if year is None:
            year = datetime.datetime.now().year
        res = year - self.birth_year
        return res

    def add_skill(self, new_skill):
        self.skills.append(new_skill)


p = Person()

import time
time.sleep(4)

p2 = Person()

print(p.time_created)
print(p2.time_created)

