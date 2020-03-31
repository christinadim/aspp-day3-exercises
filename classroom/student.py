class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def __str__(self):
        return "%s %s," % (self.first_name, self.last_name)


class Student(Person):
    def __init__(self, first_name, last_name, subject_area):
        Person.__init__(self, first_name, last_name)
        self.subject_area = subject_area

    def getSubjectArea(self):
        return self.subject_area

    def printNameSubject(self):
        print(Person.__str__(self), self.subject_area)
