class Student:
   def __init__(self, name, roll_no, marks):
     self.name = name
     self.roll_no = roll_no
     self.marks = marks
   def display(self):
      print("Name:", self.name)
      print("Roll No:", self.roll_no)
      print("Marks:", self.marks)
   def grade(self):
    if self.marks >= 50:
      return "Pass"
    else:
      return "Fail"
student1 = Student("Arun", 101, 85)
student1.display()
print("Result:", student1.grade())