class Student:
  def __init__(self, name, roll_no, cgpa):
      self.name = name
      self.roll_no = roll_no
      self.cgpa = cgpa

def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Example usage:
students = [
  Student("Alice", "A101", 3.7),
  Student("Bob", "B102", 3.5),
  Student("Charlie", "C103", 4.0),
  Student("David", "D104", 3.9),
]

sorted_students = sort_students(students)

for student in sorted_students:
  print(f"Name: {student.name}, Roll No: {student.roll_no}, CGPA: {student.cgpa}")
