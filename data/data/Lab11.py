import matplotlib.pyplot as plt
import os

student_list = open("students.txt")
student_list = student_list.read()
list_of_students = student_list.split("\n")
assignment_file = open("assignments.txt")
assignment_file = assignment_file.read()
assignment_list = assignment_file.split("\n")


class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.rawscore = 0
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_rawscore(self):
        return self.rawscore
    def set_rawscore(self, rawscore):
        self.rawscore = rawscore

class Assignment:
    def __init__(self, name, id, points):
        self.name = name
        self.id = id
        self.points = points
        self.grades = []
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_points(self):
        return self.points
    def add_grades(self, grade):
        self.grades.append(grade)
    def get_grades(self):
        return self.grades

class Submission:
    def __init__(self, student_id, assignment_id, percentage):
        self.student_id = student_id
        self.assignment_id = assignment_id
        self.percentage = percentage
    def get_student_id(self):
        return self.student_id
    def get_assignment_id(self):
        return self.assignment_id
    def get_percentage(self):
        return self.percentage

my_dict = {}
my_assignments = []
grade_dict = {}
liststoodents = []
for i in range(len(list_of_students)):
    for char in list_of_students[i]:
        id_of_student = list_of_students[i][:3]
        name_of_student = list_of_students[i][3::]
        my_dict[name_of_student] = id_of_student
    student = Student(name_of_student, id_of_student)
    liststoodents.append(student)

count = 1
for l in range(len(assignment_list)):
    if count == 1:
        asn_name = assignment_list[l]
        count += 1
        continue
    if count == 2:
        asn_id = assignment_list[l]
        count += 1
        continue
    if count == 3:
        asn_weight = assignment_list[l]
        count = 1
    object_assignment = Assignment(asn_name, asn_id, asn_weight)
    my_assignments.append(object_assignment)

directory_path = "submissions"
list_of_submission = []
# Iterate through the directory
for filename in os.listdir(directory_path):
    filepath = os.path.join(directory_path, filename)
    opensubmissions = open(filepath)
    opensubmissions = opensubmissions.read()
    list_submission = opensubmissions.split("|")
    gradez = Submission(list_submission[0], list_submission[1], list_submission[2])
    list_of_submission.append(gradez)
    # get the raw score and add to student_rawscore
    for estudente in liststoodents:
        if gradez.get_student_id() == estudente.get_id():
            #calculate raw score
            for assignment in my_assignments:
                if assignment.get_id() == gradez.get_assignment_id():
                    score = int(assignment.get_points()) * int(gradez.get_percentage())/100
                    studentscore = estudente.get_rawscore()
                    estudente.set_rawscore(int(studentscore)+int(score))
######option 1 over

#Option 2

# take the key from assignments and query submmisions( gradez) for all gredes
# create a list

#for loop on assignments
#for each assignment get the id
#for loop on submissions looking for the id
# when you find the id, add it to the list
grades = []
for q in my_assignments:
    for x in list_of_submission:

         if q.get_id() == x.get_assignment_id():
             score = int(x.get_percentage())
             q.add_grades(score)











print(f"1. Student grade\n2. Assignment statistics\n3. Assignment graph")

user_input = int(input("Enter your selection: "))
if user_input == 1:
    name_input = input("What is the student's name: ")
    if name_input in my_dict:
        id_of_student = my_dict[name_input]
        for k in liststoodents:
            if k.get_id() == id_of_student:
                fgrade = k.get_rawscore()/10
                fgrade = int(round(fgrade, 0))
                print(f"{fgrade}%")

if user_input == 2:
    valid = False

    assignment_input = input("What is the assignment name: ")
    for l in my_assignments:
        if assignment_input == l.get_name():
            mini = min(l.get_grades())
            print(f"Min: {round(mini)}%")
            total = 0
            for score in l.get_grades():
                total += score

            avge = total//30
            print(f"Avg: {(avge)}%")
            maxi = max(l.get_grades())
            print(f"Max: {round(maxi)}%")
            valid = True

    if not valid:
        print("Assignment not found")


if user_input == 3:
    valid = False
    assignment_input = input("What is the assignment name: ")
    for l in my_assignments:
        if assignment_input == l.get_name():
            print(l.get_grades())
            plt.hist(l.get_grades(), bins=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
            plt.show()
            valid = True
    if not valid:
        print("Assignment not found")