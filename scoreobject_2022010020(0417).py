class Student:
    def __init__(self, student_id, name, scores):
        self.student_id = student_id
        self.name = name
        self.scores = scores

    def calculate_total(self):
        return sum(self.scores)

    def calculate_average(self):
        return self.calculate_total() / len(self.scores)

    def calculate_grade(self):
        average = self.calculate_average()
        if average >= 95:
            return "A+"
        elif average >= 90:
            return "A"
        elif average >= 85:
            return "B+"
        elif average >= 80:
            return "B"
        elif average >= 75:
            return "C+"
        elif average >= 70:
            return "C"
        elif average >= 65:
            return "D+"
        elif average >= 60:
            return "D"
        else:
            return "F"

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def input_students(self):
        for _ in range(5):  # 기본적으로 5명의 학생 입력
            student_id = input("학번: ")
            name = input("이름: ")
            scores = [float(input(f"{subject}: ")) for subject in ['영어', 'C-언어', '파이썬']]
            self.students.append(Student(student_id, name, scores))
            print()

    def add_student(self):
        student_id = input("학번 입력: ")
        name = input("이름 입력: ")
        scores = [float(input(f"{subject}: ")) for subject in ['영어', 'C-언어', '파이썬']]
        self.students.append(Student(student_id, name, scores))
        print("학생 정보가 추가되었습니다.\n")

    def remove_student(self):
        identifier = input("삭제할 학생의 학번 또는 이름을 입력하세요: ")
        original_length = len(self.students)
        self.students = [student for student in self.students if student.student_id != identifier and student.name != identifier]
        if len(self.students) < original_length:
            print("학생 정보가 삭제되었습니다.\n")
        else:
            print("해당 학생이 없습니다.\n")

    def find_student(self):
        identifier = input("탐색할 학생의 학번 또는 이름을 입력하세요: ")
        found_students = [student for student in self.students if student.student_id == identifier or student.name == identifier]
        if found_students:
            for student in found_students:
                print(f"학번: {student.student_id}, 이름: {student.name}, 점수: {student.scores}")
        else:
            print("해당 학생이 없습니다.\n")

    def count_students_above_80(self):
        count = sum(1 for student in self.students if student.calculate_average() >= 80)
        print(f"평균 80점 이상인 학생의 수: {count}\n")

    def output_students(self):
        self.students.sort(key=lambda student: student.calculate_total(), reverse=True)
        print("\n\n==============================================================================================")
        print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
        print("==============================================================================================")
        for rank, student in enumerate(self.students, start=1):
            print(f"{student.student_id}\t{student.name}\t{student.scores[0]}\t{student.scores[1]}\t{student.scores[2]}\t{student.calculate_total()}\t{student.calculate_average():.2f}\t{student.calculate_grade()}\t{rank}")

    def menu(self):
        options = {
            "1": ("학생 정보 입력", self.input_students),
            "2": ("학생 정보 삭제", self.remove_student),
            "3": ("학생 정보 탐색", self.find_student),
            "4": ("평균 80점 이상 학생 수", self.count_students_above_80),
            "5": ("학생 정보 출력", self.output_students),
            "6": ("종료", lambda: "exit")
        }
        while True:
            print("\n[학생 정보 관리 시스템 메뉴]")
            for key, value in options.items():
                print(f"{key}: {value[0]}")
            choice = input("메뉴 선택: ")
            if choice == "6":
                print("시스템을 종료합니다.")
                break
            elif choice in options:
                action = options[choice][1]
                if action:
                    action()  # 선택된 옵션의 함수 실행
            else:
                print("잘못된 입력입니다. 다시 시도해주세요.")

def main():
    system = StudentManagementSystem()
    system.input_students()  # 먼저 학생 정보 입력
    system.output_students()  # 입력된 학생 정보 출력
    system.menu()  # 메뉴 기능 실행

if __name__ == "__main__":
    main()