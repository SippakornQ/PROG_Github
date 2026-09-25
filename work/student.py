def create_student(student_id, first_name, last_name):
    return {
        "id": student_id,
        "first_name": first_name,
        "last_name": last_name,
        "courses": [],
    }


def display_student(student):
    if not student["courses"]:
        return

    sorted_courses = sorted(student["courses"], key=lambda c: c["id"])
    for course in sorted_courses:
        title = course["title"]
        if len(title) > 28:
            title = title[:25] + "..."
        print(f"{course['id']} {title:<28}")