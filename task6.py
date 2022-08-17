subj = {}
with open('task6.txt', 'r') as in_f:
    for line in in_f:
        subj, lecture, practice, lab = line.split()
        subj[subj] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')
