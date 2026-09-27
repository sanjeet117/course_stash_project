class Course:

    def __init__(self, course_id, course_name, instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor

    def display_course(self):
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"course Instructor: {self.instructor}")


course = Course(101, "Python Programming", "Sanjeet")

course.display_course()
