import sys
from person import Person


def parse_student_grades(grade_string):
    """
    Create a dictionary mapping student utln's to their person representations.

    Args:
        The entire contents of a grade file, as a string.
    Returns:
        A dictionary mapping utln's to person representations.
    """
    status = "FINDING STUDENT"
    student = {}
    students = {}
    for line in grade_string.split('\n'):
        if len(line) == 0:
            continue
        if ".fullname" in line:
            continue
        if status ==  "FINISHING STUDENT":
            if line[0] == " ":
                student["comments"] += [line]
            else:
                status = "FINDING STUDENT"
                new_student = Person(student["utln_line"], student["comments"])
                students[new_student.utln] = new_student
                student = {}
        if status == "FINDING STUDENT":
            if line[0] != " ":
                student = {"utln_line":line, "comments":[]}
                status = "FINISHING STUDENT"
    return students

def main(args):
    """
    Replace incorrect grades with correct grades.

    Args:
        args: a list of command line arguments
    """
    with open(args[1], "rb") as fp:
        old = fp.read()
    with open(args[2], "rb") as fp:
        new = fp.read()
    grades = parse_student_grades(old)
    new_grades = parse_student_grades(new)

    for utln in args[3:]:
        print utln
        if utln in grades and utln in new_grades:
            grades[utln] = new_grades[utln]

    for student in grades:
        grades[student].output()

if __name__ == "__main__":
    main(sys.argv)
