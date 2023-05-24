class Subject:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class GradingSystem:
    def __init__(self):
        self.subjects = []

    def add_subject(self, name, grade):
        subject = Subject(name, grade)
        self.subjects.append(subject)

    def calculate_average_grade(self):
        total = sum(subject.grade for subject in self.subjects)
        average = total / len(self.subjects)
        return average
