#Keenen Lee-Smith
#CIS261
#VIBE Coding

"""Student record manager with test-score and grade calculations."""


def calculate_average(scores):
	"""Return the average of a student's test scores."""
	return sum(scores) / len(scores) if scores else 0


def calculate_letter_grade(average):
	"""Convert a percentage average to a letter grade."""
	if average >= 90:
		return "A"
	if average >= 80:
		return "B"
	if average >= 70:
		return "C"
	if average >= 60:
		return "D"
	return "F"


def get_score(prompt):
	"""Read and validate a test score from the user."""
	while True:
		try:
			score = float(input(prompt))
			if 0 <= score <= 100:
				return score
			print("Score must be between 0 and 100.")
		except ValueError:
			print("Please enter a number between 0 and 100.")


def display_student(student):
	"""Display one student's record."""
	average = calculate_average(student["scores"])
	grade = calculate_letter_grade(average)
	scores = ", ".join(f"{score:.1f}" for score in student["scores"])
	print(f"\nID: {student['id']}")
	print(f"Name: {student['name']}")
	print(f"Test scores: {scores or 'No scores recorded'}")
	print(f"Average: {average:.2f}%")
	print(f"Letter grade: {grade}")


def add_student(students):
	student_id = input("Enter student ID: ").strip()
	if not student_id:
		print("Student ID cannot be empty.")
		return
	if student_id in students:
		print("A student with that ID already exists.")
		return

	name = input("Enter student name: ").strip()
	if not name:
		print("Student name cannot be empty.")
		return

	scores = [
		get_score("Test 1 score: "),
		get_score("Test 2 score: "),
		get_score("Test 3 score: "),
	]

	students[student_id] = {"id": student_id, "name": name, "scores": scores}
	print("Student record added.")


def view_all_students(students):
	if not students:
		print("No student records found.")
		return

	print("\nStudent Summary")
	print("-" * 56)
	print(f"{'ID':<15}{'Name':<25}{'Average':>9}{'Grade':>7}")
	print("-" * 56)
	for student in students.values():
		average = calculate_average(student["scores"])
		grade = calculate_letter_grade(average)
		print(f"{student['id']:<15}{student['name']:<25}{average:>8.2f}%{grade:>7}")


def find_student(students):
	student_id = input("Enter student ID: ").strip()
	student = students.get(student_id)
	if student is None:
		print("Student not found.")
	return student


def update_student(students):
	student = find_student(students)
	if student is None:
		return

	print("1. Change name")
	print("2. Replace a test score")
	choice = input("Choose an update: ").strip()
	if choice == "1":
		name = input("Enter the new name: ").strip()
		if name:
			student["name"] = name
			print("Name updated.")
		else:
			print("Name cannot be empty.")
	elif choice == "2":
		test_number = input("Enter the test number to replace (1-3): ").strip()
		if test_number in {"1", "2", "3"}:
			index = int(test_number) - 1
			student["scores"][index] = get_score("Enter the new test score: ")
			print("Test score updated.")
		else:
			print("Test number must be 1, 2, or 3.")
	else:
		print("Invalid update choice.")


def delete_student(students):
	student = find_student(students)
	if student is None:
		return
	del students[student["id"]]
	print("Student record deleted.")


def main():
	students = {}
	while True:
		print("\nStudent Record Manager")
		print("1. Add student")
		print("2. View all students")
		print("3. View one student")
		print("4. Update student")
		print("5. Delete student")
		print("6. Exit")
		choice = input("Choose an option: ").strip()

		if choice == "1":
			add_student(students)
		elif choice == "2":
			view_all_students(students)
		elif choice == "3":
			student = find_student(students)
			if student is not None:
				display_student(student)
		elif choice == "4":
			update_student(students)
		elif choice == "5":
			delete_student(students)
		elif choice == "6":
			print("Goodbye!")
			break
		else:
			print("Please choose an option from 1 to 6.")


if __name__ == "__main__":
	main()

