from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom

school = School("BM", "Dhaka")

# Addning Class Room
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# Adding Student
rahim = Student('Rahim', eight)
karim = Student('karim', nine)
fahim = Student('Fahim', ten)
hamim = Student('Hamim', ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hamim)

# Adding Teacher
sayem = Teacher('Sayem')
saiful = Teacher('Saiful')
Tofa = Teacher('Tofa')

# Adding Subjects
math = Subject('Math', Tofa)
english = Subject('English', sayem)
bangla = Subject('Bangla', saiful)
science = Subject('Science', saiful)

eight.add_subject(bangla)
eight.add_subject(math)
nine.add_subject(english)
nine.add_subject(math)
nine.add_subject(bangla)
ten.add_subject(math)
ten.add_subject(english)
ten.add_subject(bangla)
ten.add_subject(science)

eight.take_semester_final_exam()

print(school)