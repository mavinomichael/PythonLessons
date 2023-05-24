from BeginnerLessons.GradingSystem.grading import GradingSystem


def init():
    completed = False
    grading_system = GradingSystem()

    while not completed:
        subject_name = input('Enter name of subject')
        if not subject_name:
            break
        grade = int(input('Enter grade for subject'))
        if not grade:
            break
        grading_system.add_subject(subject_name, grade)
        response = input('Do you want to add another subject? YES/NO')
        if response.strip() == 'YES':
            completed = False
        elif response.strip() == 'NO':
            completed = True
            average = grading_system.calculate_average_grade()
            print(f'The average score is {average}')
        else:
            raise ValueError('Your input is invalid, please enter YES or NO')
