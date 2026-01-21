from student_manager import StudentManager
from result_manager import ResultManager

student_manager = StudentManager()
result_manager = ResultManager()

while True:
    print("\nStudent Result Management System")
    print("1. Add Student (Manual)")
    print("2. View Students")
    print("3. Add Result (Manual)")
    print("4. View Results")
    print("5. Add Sample Student & Result")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Student ID: ")
        name = input("Name: ")
        dept = input("Department: ")
        student_manager.add_student(sid, name, dept)
        print("Student added successfully.")

    elif choice == "2":
        students = student_manager.view_students()
        for s in students:
            print(s.strip())

    elif choice == "3":
        sid = input("Student ID: ")
        course = input("Course: ")
        score = input("Score: ")
        result_manager.add_result(sid, course, score)
        print("Result added successfully.")

    elif choice == "4":
        results = result_manager.view_results()
        for r in results:
            print(r.strip())

    elif choice == "5":
        # Predefined inputs (as required in assignment)
        student_manager.add_student(
            "24CSC001",
            "Andrew Oluwole",
            "Computer Science"
        )

        result_manager.add_result(
            "24CSC001",
            "SEN 201",
            "78"
        )

        print("Sample student and result added successfully.")

    elif choice == "6":
        print("Exiting system...")
        break

    else:
        print("Invalid choice!")
