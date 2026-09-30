class Student:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []

    def __repr__(self):
        return f"({self.id}, '{self.first_name} {self.last_name}')"

    def display(self):
        if not self.courses:
            return

        print("+----------+------------------------------+")
        print("| Cour. ID | Name                         |")
        print("+----------+------------------------------+")

        sorted_courses = sorted(self.courses, key=lambda c: c.id)
        for course in sorted_courses:
            title = course.title
            if len(title) > 28:
                title = title[:25] + "..."
            print(f"| {course.id} | {title:<28} |")

        print("+----------+------------------------------+")