# FIRST YEAR CSE REPORT CARD

subjects = [
    "Programming in Python",
    "Data Structures",
    "Digital Logic",
    "Discrete Mathematics",
    "Computer Organization"
]

def calculate_average(marks):
    total = 0
    for m in marks:
        total += m
    return total / len(marks)

def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"

def find_highest(marks):
    highest = marks[0]
    for m in marks:
        if m > highest:
            highest = m
    return highest

def find_lowest(marks):
    lowest = marks[0]
    for m in marks:
        if m < lowest:
            lowest = m
    return lowest

def count_passed(marks):
    count = 0
    for m in marks:
        if m >= 40:
            count += 1
    return count

def get_result(marks):
    for m in marks:
        if m < 40:
            return "FAIL"
    return "PASS"

def generate_report(name, subjects, marks):
    avg = calculate_average(marks)
    grade = calculate_grade(avg)
    highest = find_highest(marks)
    lowest = find_lowest(marks)
    passed = count_passed(marks)
    result = get_result(marks)

    print("\nFIRST YEAR CSE REPORT CARD")
    print(f"Student Name : {name}\n")
    print("{:<25} {:>5}".format("Subject", "Marks"))
    print("-" * 32)
    for i in range(len(subjects)):
        print("{:<25} {:>5}".format(subjects[i], marks[i]))
    print("-" * 32)
    print("{:<25} : {:.1f}".format("Average Marks", avg))
    print("{:<25} : {}".format("Highest Marks", highest))
    print("{:<25} : {}".format("Lowest Marks", lowest))
    print("{:<25} : {}/{}".format("Subjects Passed", passed, len(marks)))
    print("{:<25} : {}".format("Overall Grade", grade))
    print("{:<25} : {}".format("Overall Result", result))


# Main program
name = input("Enter student name: ")
marks = []
for i in range(len(subjects)):
    m = int(input(f"Enter marks for {subjects[i]} (0-100): "))
    marks.append(m)

generate_report(name, subjects, marks)

