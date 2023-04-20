from teacher import Teacher
from student import Student


print()
print('Student')
student1 = Student('123-3232', 'Arroyo', 'Karen', 'Cande', 'Student', '1st', 'BSCS', 'A')
print(student1.getName())
print(student1.getYrCourseSec())
print(student1)

print()
print('Teacher')
teacher1 = Teacher('73748', 'Lorilla', 'Joseph', 'Villanueva', 'Teacher', 'DCLIS', 'Instructor')
print(teacher1.getDepartment())
print(teacher1.getName())
print(teacher1)
print()