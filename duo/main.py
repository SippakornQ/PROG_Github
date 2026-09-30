from course import Course
from student import Student

s = Student("001", "Indy", "Example")
c1 = Course("05696110", "Database Programming in P...")
c2 = Course("05696111", "Foundation of Programming")

c1.enroll(s)
c2.enroll(s)

print("--- ผลลัพธ์ c1.display() ---")
c1.display()

print("\n--- ผลลัพธ์ s.display() ---")
s.display()