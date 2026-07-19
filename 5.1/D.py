class Programmer():

    def __init__(self, name, grade):
        rank = {
            "Junior": 10,
            "Middle": 15,
            "Senior": 20
        }
        self.name = name
        self.grade = grade
        self.wage = rank[grade]
        self.work_time = 0
        self.earnings = 0 

    def work(self, time):
        self.work_time += time
        self.earnings += self.wage * time

    def rise(self):
        if self.grade == "Junior":
            self.grade = "Middle"
            self.wage = 15
        elif self.grade == "Middle":
            self.grade = "Senior"
            self.wage = 20
        else:
            self.wage += 1

    def info(self):
        return f'{self.name} {self.work_time}ч. {self.earnings}тгр.'
    

programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())