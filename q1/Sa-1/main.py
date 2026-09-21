class AssignmentSubmission:
    def __init__(self, student_name, student_id, class_name, assignment_title, due_date, is_submitted, grade, submitted_files):
        self.student_name = student_name
        self.student_id = student_id
        self.class_name = class_name
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = is_submitted
        self.__grade = grade
        self.__submitted_files = submitted_files

    def __validate__grade(self, grade):
        if not isinstance(grade, (int, float)):
            raise ValueError("Grade must be a number.")
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")
        return True
    def __check__submission_status(self):
        return self.__is_submitted
    def is__duplicate__(self, other_assignment):
        if not isinstance(other_assignment, AssignmentSubmission):
            raise ValueError("The other assignment must be an instance of AssignmentSubmission.")
        return (self.student_id == other_assignment.student_id and
                self.class_name == other_assignment.class_name and
                self._assignment_title == other_assignment._assignment_title)
    def add_file(self, filename: str):
        if not isinstance(filename, str):
            raise ValueError("Filename must be a string.")
        self.__submitted_files.append(filename)
        print(f"File '{filename}' added to submitted files.")
    def remove_file(self, filename: str):
        if filename in self.__submitted_files:
            self.__submitted_files.remove(filename)
            print(f"File '{filename}' removed from submitted files.")
        else:
            raise ValueError("File not found in submitted files.")
    def assign_grade(self, score: float):
        self.__validate__grade(score)
        self.__grade = score
    def get_grade(self, student_id: str, class_name: str, assignment_title: str):
        return self.__grade
    def view_files(self):
        return self.__submitted_files
    def get_status_report(self):
        status = "Submitted" if self.__is_submitted else "Not Submitted"
        return {
            "Student Name": self.student_name,
            "Student ID": self.student_id,
            "Class Name": self.class_name,
            "Assignment Title": self._assignment_title,
            "Due Date": self._due_date,
            "Submission Status": status,
            "Grade": self.__grade,
            "Submitted Files": self.__submitted_files
        }

print("--- INITIALIZING DROPBOX FOR STUDENTS ---")

student1 = AssignmentSubmission(

    student_name="Alex Gonzaga",

    student_id="pshs-1090-x",

    class_name="CS-101",

    assignment_title="CS-101",

    due_date="2026-10-01",

    is_submitted=False,

    grade=None,

    submitted_files=[]

)

student2 = AssignmentSubmission(

    student_name="Adelle",

    student_id="pshs-1920-x",

    class_name="CS-103",

    assignment_title="CS-103",

    due_date="2026-10-01",

    is_submitted=False,

    grade=None,

    submitted_files=[]



)

student3 = AssignmentSubmission(

    student_name="Juan dela Cruz",

    student_id="pshs-1033-x",

    class_name="CS-101",

    assignment_title="CS-101",

    due_date="2026-10-01",

    is_submitted=False,

    grade=None,

    submitted_files=[]


)

student4 = AssignmentSubmission(

    student_name="Maria Santos",

    student_id="pshs-1044-x",

    class_name="CS-101",

    assignment_title="CS-101",

    due_date="2026-10-01",

    is_submitted=False,

    grade=None,

    submitted_files=[]


)

student5 = AssignmentSubmission(

    student_name="Jose Reyes",

    student_id="pshs-1055-x",

    assignment_title="CS-101",

    class_name="CS-101",

    due_date="2026-10-01",

    is_submitted=False,

    grade=None,

    submitted_files=[]


)


print("---TEST SCENARIO 1: Multiple Files via List---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("---TEST SCENARIO 2: Removing Files from List---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("---TEST SCENARIO 3: Preventing Duplicate Files---")
student3.add_file("script.py")
student3.add_file("script.py")  
print(f"Nicole's Files: {student3.view_files()}\n")

print("--TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100)
print()

print("--- FINAL EXAM REPORT --")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
