def create_course(course_id, title):
    return {"id": course_id, "title": title, "students": []}


def enroll(course, student):
    if student not in course["students"]:
        course["students"].append(student)
    if course not in student["courses"]:
        student["courses"].append(course)


def remove_enrollment(course, student):
    if student in course["students"]:
        course["students"].remove(student)
    if course in student["courses"]:
        student["courses"].remove(course)


def display_course(course):
    formatted_students = [
        f"({s['id']}, '{s['first_name']} {s['last_name']}')"
        for s in course["students"]
    ]
    print("[" + ", ".join(formatted_students) + "]")