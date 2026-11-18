import json
import os

class StudentManager:
    def __init__(self, data_file="data/students.json"):
        self.data_file = data_file
        self.students = []
        self.load_data()

    def load_data(self):
        """Loads data from JSON file. Creates folder/file if it doesn't exist."""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    self.students = json.load(file)
            except json.JSONDecodeError:
                self.students = []
        else:
            self.students = []

    def save_data(self):
        """Saves current student list to JSON file."""
        with open(self.data_file, "w") as file:
            json.dump(self.students, file, indent=4)

    def validate_student(self, student_id, name, course, marks):
        """Validates input data. Returns (True, "") if valid, else (False, error_msg)"""
        if not student_id.strip() or not name.strip():
            return False, "Student ID and Name cannot be empty."
        
        if not student_id.isalnum():
            return False, "Student ID must be alphanumeric (no spaces or symbols)."
            
        # Check for duplicate ID (only for new additions)
        for student in self.students:
            if student["id"] == student_id:
                return False, f"Student ID '{student_id}' already exists."

        try:
            marks_val = int(marks)
            if marks_val < 0 or marks_val > 100:
                return False, "Marks must be between 0 and 100."
        except ValueError:
            return False, "Marks must be a valid number."

        return True, ""

    def add_student(self, student_id, name, course, marks, gender, date):
        """Adds a new student to the list and saves to file."""
        self.students.append({
            "id": student_id,
            "name": name,
            "course": course,
            "marks": int(marks),
            "gender": gender,
            "date": date
        })
        self.save_data()

    def delete_student(self, student_id):
        """Deletes a student by ID."""
        self.students = [s for s in self.students if s["id"] != student_id]
        self.save_data()

    def update_student(self, student_id, new_name, new_course, new_marks, gender, date):
        """Updates an existing student's details."""
        for student in self.students:
            if student["id"] == student_id:
                student["name"] = new_name
                student["course"] = new_course
                student["marks"] = int(new_marks)
                student["gender"] = gender
                student["date"] = date
                break
        self.save_data()

    def search_students(self, query):
        """Returns a list of students matching the query in ID or Name."""
        query = query.lower()
        return [s for s in self.students if query in s["name"].lower() or query in s["id"].lower()]