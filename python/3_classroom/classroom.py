import random
import string


class Classroom:
    classrooms = {}

    def __init__(self, class_id, teacher_id, subject_id, meeting_id):
        self.class_id = class_id
        self.teacher_id = teacher_id
        self.subject_id = subject_id
        self.meeting_id = meeting_id
        self.students = []

        # Generate a unique booking ID
        self.booking_id = self.generate_booking_id()

        # Store classroom
        Classroom.classrooms[self.booking_id] = self

    @staticmethod
    def generate_booking_id():
        while True:
            booking = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            if booking not in Classroom.classrooms:
                return booking

    def add_student(self, student_id):
        self.students.append(student_id)


class Teacher:
    def __init__(self, teacher_id):
        self.teacher_id = teacher_id

    def create_classroom(self, class_id, subject_id, meeting_id):
        room = Classroom(class_id, self.teacher_id, subject_id, meeting_id)

        print("\nClassroom Created Successfully")
        print("------------------------------")
        print("Teacher ID :", self.teacher_id)
        print("Class ID   :", class_id)
        print("Booking ID :", room.booking_id)
        print()

        return room.booking_id


class Student:
    def __init__(self, student_id):
        self.student_id = student_id

    def join_classroom(self, booking_id):
        if booking_id in Classroom.classrooms:
            room = Classroom.classrooms[booking_id]
            room.add_student(self.student_id)

            print(f"Student {self.student_id} joined {room.class_id}")
        else:
            print("Invalid Booking ID")


# -----------------------------
# Available IDs
# -----------------------------

class_ids = ["1_A", "1_B", "1_C", "1_D"]

student_ids = list(range(1150401, 1150601))

teacher_ids = [f"T_{i:03d}" for i in range(1, 51)]


# -----------------------------
# Teacher creates classroom
# -----------------------------

teacher = Teacher("T_001")

booking_id = teacher.create_classroom(
    class_id="1_A",
    subject_id="Python",
    meeting_id="M101"
)

# -----------------------------
# Students join
# -----------------------------

student1 = Student(1150401)
student2 = Student(1150402)

student1.join_classroom(booking_id)
student2.join_classroom(booking_id)

# -----------------------------
# Display classroom information
# -----------------------------

room = Classroom.classrooms[booking_id]

print("\nClassroom Details")
print("------------------")
print("Class ID   :", room.class_id)
print("Teacher ID :", room.teacher_id)
print("Subject    :", room.subject_id)
print("Meeting ID :", room.meeting_id)
print("Booking ID :", room.booking_id)
print("Students   :", room.students)