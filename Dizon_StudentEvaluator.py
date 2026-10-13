name = ""
score1 = 0
score2 = 0
score3 = 0
performance_level = ""
def display_header():
    print("Student Performance Report")
display_header()
def get_student_info():
    global score1, score2, score3, name
    name = str(input("Enter Student Name: "))
    score1 = float(input("Enter score for assessment 1: "))
    score2 = float(input("Enter score for assessment 2: "))
    score3 = float(input("Enter score for assessment 3: "))

get_student_info()
average = (score1 + score2 + score3)/3
def evaluate_performance():
    global average, performance_level
    if 90 > average > 99:
        performance_level = "Outstanding"
    elif 85 > average > 89:
        performance_level = "Very Satisfactory"
    elif 80 > average > 84:
        performance_level = "Satisfactory"
    elif 75 > average > 79:
        performance_level = "Fairly Satisfactory"
    elif average <=74:
        performance_level = "Needs Improvement"
def display_report():
    global average, performance_level, score1, score2, score3
    print("Student Name: ", name)
    print("Score 1: ", score1)
    print("Score 2: ", score2)
    print("Score 3: ", score3)
    print(f"Average score: {average:.2f}")
    print("Performance Level: ", performance_level)



evaluate_performance()
display_report()