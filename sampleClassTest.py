#
#
# Sample Class Test


class ClassStudent(object):
    def __init__(self, name, score):
        self.name = name
        self.score = float(score)

    def print_name(self):
        print("My name is: %s" % self.name)

    def print_score(self):
        print("My Score is: %f" % self.score)

    def print_attribute(self):
        print("My name is: %s,\t and score is: %.2f" % (self.name, self.score))

    def strGetGrade(self):
        if self.score >= 90:
            return "A"
        elif self.score < 90 and self.score >= 80:
            return "B"
        elif self.score < 80 and self.score >= 70:
            return "C"
        elif self.score < 70 and self.score >= 60:
            return "D"
        else:
            return "F"


addy = ClassStudent("AddyXiao", 91.5)
clerk = ClassStudent("ClerkXiao", 80)
elea = ClassStudent("Elea", 70)

addy.print_attribute()

