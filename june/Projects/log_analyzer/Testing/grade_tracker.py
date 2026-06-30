class GradeTracker:
    def __init__(self, student_name: str):
        self.student_name = student_name
        self.grades = []

    def add_grade(self, grade: float):
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100.")
        self.grades.append(grade)

    def calculate_average(self) -> float:
        if not self.grades:
            return 0.0
        return round(sum(self.grades) / len(self.grades), 2)

    def is_passing(self) -> bool:
        return self.calculate_average() >= 70.0
