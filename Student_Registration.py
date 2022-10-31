class Student:
    def __init__(self, FirstName, LastName, course, YearAndSection):
        self.FirstName = FirstName
        self.LastName = LastName
        self.course = course
        self.YearAndSection = YearAndSection

    def introduce(self):
        print("Hello, I am " , self.FirstName , self.LastName, "from", self.course, self.YearAndSection)


students = []
while True:
    print("Answer the questions to register.")
    print()
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    myCourse = input("Enter your course: ")
    yrAndSec = input("Enter your year and section: ")
    learner = Student(fname,lname,myCourse,yrAndSec)
    students.append(learner)

    ifContinue = int(input("Press 1 if you want to register another student while press 2 if not: "))
    if ifContinue == 1:
        print()
    elif ifContinue == 2:
        break
    else:
        print("Invalid")
        break
print()
print("This are the list of students who registered:")
print()
for student in students:
    student.introduce()
