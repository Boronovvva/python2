class GeeksPeople:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Имя: {self.name}, Почта: {self.email}, Телефонный номер: {self.phone}. "

class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, group_where_study):
        GeeksPeople.__init__(self, name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study

    def study(self):
        print(f"Студент {self.name} учится в {self.group_where_study} группе.")

    def __str__(self):
        return super().__str__() + f"ID студента: {self.student_id}, Группа студента: {self.group_where_study}"

class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach):
        GeeksPeople.__init__(self, name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach

    def teach(self):
        print(f"Учитель {self.name} преподает в группе {self.group_where_teach}")

    def __str__(self) -> str:
        return super().__str__() + f"ID учителя: {self.teacher_id}, Группа учителя: {self.group_where_teach}"

class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        GeeksPeople.__init__(self, name, email, phone)
        self.admin_id = admin_id

    def create_group(self, course_name):
        print(f"Админ {self.name} создал новый курс: {course_name}.")

    def __str__(self) -> str:
        return super().__str__() + f"ID админа: {self.admin_id}"

class Mentor(Student, Teacher):
    def __init__(self, name, email, phone, student_id, group_where_study, teacher_id, group_where_teach):
        Student.__init__(self, name, email, phone, student_id, group_where_study)
        Teacher.__init__(self, name, email, phone, teacher_id, group_where_teach)

    def __str__(self) -> str:
        return f"ID ментора: {self.student_id}, Группа ментора: {self.group_where_study}" + f"ID ментора: {self.teacher_id}, Группа ментора: {self.group_where_teach}" 

student = Student("Бибисара", "@saraboronova003@gmail.com", "0990909300", "020201", "14-1b")
print(student)
student.study()
teacher = Teacher("Сыймык", "@teacher.com", "010203", "020301", "14-1b")
print(teacher)
teacher.teach()
admin = Admin("Нурболот", "@admin.com", "010203", "09090807")
print(admin)
admin.create_group("14-1b")
mentor = Mentor("Кудбухон", "@mentor.com", "010203", "090908", "14-1b", "020201", "15-1b")
print(mentor)
mentor.study()
mentor.teach()
