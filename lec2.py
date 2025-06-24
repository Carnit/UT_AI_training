from typing import Dict, List, Tuple, Any

students_data: List[Dict[str, Any]] = []
subjects: List[str] = ["Math", "Science", "English", "History", "Computer"]

def get_student_data() -> Dict[str, Any]:
    name: str = input("Enter student name: ")
    roll: str = input("Enter roll number: ")
    scores: Dict[str, float] = {}
    for subject in subjects:
        score: float = float(input(f"Enter marks for {subject}: "))
        scores[subject] = score
    return {"name": name, "roll": roll, "scores": scores}

def calculate_average(scores: Dict[str, float]) -> float:
    return sum(scores.values()) / len(scores)

def assign_grade(avg: float) -> str:
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

def subject_wise_toppers(data: List[Dict[str, Any]]) -> Dict[str, Tuple[float, List[str]]]:
    toppers: Dict[str, Tuple[float, List[str]]] = {}
    for subject in subjects:
        max_score: float = max(student['scores'][subject] for student in data) 
        topper_list: List[str] = [
            student['name'] for student in data if student['scores'][subject] == max_score  
        ]
        toppers[subject] = (max_score, topper_list)
    return toppers

def display_report_card(student: Dict[str, Any]) -> None:
    print("\n--- Report Card ---")
    print(f"Name: {student['name']}")
    print(f"Roll: {student['roll']}")
    print("Scores:")
    for subject, score in student['scores'].items():
        print(f"  {subject}: {score}")
    avg: float = calculate_average(student['scores'])
    grade: str = assign_grade(avg)
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
    print("-------------------\n")

def find_subjects_with_same_top_score(toppers: Dict[str, Tuple[float, List[str]]]) -> Dict[float, Tuple[str, ...]]:
    score_to_subjects: Dict[float, List[str]] = {}
    for subject, (score, _) in toppers.items():
        score_to_subjects.setdefault(score, []).append(subject)

    same_score_subjects: Dict[float, Tuple[str, ...]] = {
        score: tuple(subs) for score, subs in score_to_subjects.items() if len(subs) > 1
    }
    return same_score_subjects

def main() -> None:
    while True:
        print("\n===== Student Management System =====")
        print("1. Add a new student")
        print("2. Display all report cards")
        print("3. Show subject-wise toppers")
        print("4. Show subjects with same top score")
        print("5. Exit")
        
        choice: str = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            student: Dict[str, Any] = get_student_data()
            students_data.append(student)
            print(f"\nStudent {student['name']} added successfully!")
            
        elif choice == "2":
            if not students_data:
                print("\nNo students added yet.")
            else:
                for student in students_data:
                    display_report_card(student)
                    
        elif choice == "3":
            if not students_data:
                print("\nNo students added yet.")
            else:
                toppers: Dict[str, Tuple[float, List[str]]] = subject_wise_toppers(students_data)
                print("\n=== Subject-wise Toppers ===")
                for subject, (score, names) in toppers.items():
                    print(f"{subject}: {', '.join(names)} (Score: {score})")
                    
        elif choice == "4":
            if not students_data:
                print("\nNo students added yet.")
            else:
                toppers_data: Dict[str, Tuple[float, List[str]]] = subject_wise_toppers(students_data)
                print("\nSubjects with SAME top score:")
                same_score_subjects: Dict[float, Tuple[str, ...]] = find_subjects_with_same_top_score(toppers_data)
                if same_score_subjects:
                    for score, subjects_tuple in same_score_subjects.items():
                        print(f"Score {score} in subjects: {', '.join(subjects_tuple)}")
                else:
                    print("No subjects have the same top score.")
                    
        elif choice == "5":
            print("\nExiting the program. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
