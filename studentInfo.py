import random

lastNames=["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson", "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White"]

def main():
  students = [
    Student("Larsson", "Hal", 47, 250, 6),
    Student("BonJovi", "Jon", 55, 135, 5),
    Student("BonJovi", "Jon", 55, 135, 5),
    Student("BonJovi", "Jon", 55, 135, 5),
    Student("BonJovi", "Jon", 55, 135, 5),
    Student("BonJovi", "Jon", 55, 135, 5),
    Student("BonJovi", "Jon", 55, 135, 5),
    Student("BonJovi", "Jon", 55, 135, 5),
    Student("BonJovi", "Jon", 55, 135, 5),
    Student("BonJovi", "Jon", 55, 135, 5),
    Student("BonJovi", "Jon", 55, 135, 5),
  ]

  printHeader()
  selection = int(getUserSelection())
  if selection == 0:
    printStudentsByAge(students)
  elif selection == 1:
    printStudentsBylastName(students)
  elif selection == 2:
    printStudentsByfirstName(students)
  elif selection == 3:
    printSumAge
  else:
    print ("SELECTION NOT RECOGNIZED")

class Student:
  def __init__(self, lastName, firstname, age, weight, height):
    self.assignRandomlastName()
    self.assignRandomfirstName()
    self.assignRandomAge()
    self.assignRandomWeight()
    self.assignRandomHeight()

  def assignRandomlastName(self):
    self.lastName = random.choice (lastNames)

  def assignRandomfirstName(self):
    self.firstName = random.choice (firstNames)

  def assignRandomAge(self):
    self.age = random.randint(0,100)

  def assignRandomWeight(self):
    self.weight = random.randint(100,300)

  def assignRandomHeight(self):
    self.height = random.randint(5,7)

inputQuestions = [
  "For STUDENTS BY AGE, type 0",
  "For STUDENTS BY LAST NAME, type 1",
  "For STUDENTS BY FIRST NAME, type 2",
  "For SUM of STUDENT AGES type 3",
  "For AVERAGE of STUDENT AGES type 5",
]

def getUserSelection():
  print (inputQuestions[0])
  print (inputQuestions[1])
  print (inputQuestions[2])
  print (inputQuestions[3])
  print (inputQuestions[4])
  return input("Type selection and press enter:")

def printHeader():
    print("STUDENT SORTING")

def printStudent(student):
    print (student.lastName + ", " + student.firstName + ", " + str(student.age) + ", " + str(student.weight) + ", " + str(student.height))


def printStudentsByAge(students):
  print ("----Students By Age-----")
  sortStudents = sorted(students, key=lambda student: student.age)
  for student in sortStudents:
      printStudent(student)

def printStudentsBylastName(students):
  print ("----Students By -----")
  sortStudents = sorted(students, key=lambda student: student.lastName)
  for student in sortStudents:
    printStudent(student)

def printStudentsByfirstName(students):
  print ("----Students By -----")
  sortStudents = sorted(students, key=lambda student: student.firstName)
  for student in sortStudents:
    printStudent(student)

def printSumAge(students):
  print ("Answer:")

def printAvgAge(students):
  print ("Answer:")

def ageRange(studentA, studentB):
  return math.abs(studentA.age - studentB.age)


main()
