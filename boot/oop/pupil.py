class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        elif 80 <= score < 90:
            return "B"
        elif 70 <= score < 80:
            return "C"
        elif 60 <= score < 70:
            return "D"
        else:
            return "F"

    def add_course(self, course_name, score):
        letter = self.calculate_letter_grade(score)
        self.__courses[course_name] = letter

    def get_courses(self):
        return self.__courses
