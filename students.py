students = [
    {'name': 'SOFA', 'ORT': 110, 'male': 'f'},
    {'name': 'ALEX', 'ORT': 98, 'male': 'm'},
    {'name': 'LINA', 'ORT': 120, 'male': 'f'},
    {'name': 'TIMUR', 'ORT': 75, 'male': 'm'},
    {'name': 'DIANA', 'ORT': 135, 'male': 'f'},
    {'name': 'ERLAN', 'ORT': 88, 'male': 'm'},
    {'name': 'NURA', 'ORT': 147, 'male': 'f'},
    {'name': 'ALI', 'ORT': 52, 'male': 'm'},
    {'name': 'ZARA', 'ORT': 123, 'male': 'f'},
    {'name': 'OMAR', 'ORT': 101, 'male': 'm'},
    {'name': 'JANA', 'ORT': 111, 'male': 'f'},
    {'name': 'RUSLAN', 'ORT': 67, 'male': 'm'},
    {'name': 'MIRA', 'ORT': 89, 'male': 'f'},
    {'name': 'NURIS', 'ORT': 144, 'male': 'm'},
    {'name': 'LANA', 'ORT': 130, 'male': 'f'},
    {'name': 'DASTAN', 'ORT': 76, 'male': 'm'},
    {'name': 'AYNA', 'ORT': 93, 'male': 'f'},
    {'name': 'BAKT', 'ORT': 105, 'male': 'm'},
    {'name': 'ELINA', 'ORT': 114, 'male': 'f'},
    {'name': 'SAMAT', 'ORT': 83, 'male': 'm'},
    {'name': 'NINA', 'ORT': 134, 'male': 'f'},
    {'name': 'ASLAN', 'ORT': 60, 'male': 'm'},
    {'name': 'GULYA', 'ORT': 99, 'male': 'f'},
    {'name': 'ISLAM', 'ORT': 71, 'male': 'm'},
    {'name': 'RAISA', 'ORT': 149, 'male': 'f'},
    {'name': 'ARSLAN', 'ORT': 41, 'male': 'm'},
    {'name': 'SARA', 'ORT': 126, 'male': 'f'},
    {'name': 'TALGAT', 'ORT': 87, 'male': 'm'},
    {'name': 'AINURA', 'ORT': 138, 'male': 'f'},
    {'name': 'YERLAN', 'ORT': 53, 'male': 'm'},
    {'name': 'ALINA', 'ORT': 117, 'male': 'f'},
    {'name': 'AZAMAT', 'ORT': 109, 'male': 'm'},
    {'name': 'AKBAR', 'ORT': 30, 'male': 'm'},
    {'name': 'LAILA', 'ORT': 25, 'male': 'f'}
]

def distribute_students(students):
    univer = []
    college = []
    army = []
    marry = []

    for student in students:
        name = student['name']
        ort = student['ORT']
        gender = student['male']

        if ort > 110:
            univer.append(name)
        elif 40 <= ort <= 109:
            college.append(name)
        else:
            if gender == 'm':
                army.append(name)
            else:
                marry.append(name)

    print("UNIVER:", tuple(univer))
    print("COLLEGE:", tuple(college))
    print("ARMY:", tuple(army))
    print("MARRY:", tuple(marry))

distribute_students(students)