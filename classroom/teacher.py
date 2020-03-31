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


class Teacher(Person):
    def __init__(self, first_name, last_name, course):
        Person.__init__(self, first_name, last_name)
        self.course = course

    def getCourse(self):
        return self.course

    def printNameCourse(self):
        print(Person.__str__(self), self.course)
