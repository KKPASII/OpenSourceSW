n = int(input())
student_tuples = []

def func1(obj):
    return (-obj[1], obj[2] == 'true')

for i in range(n):
    line = input().split()
    name = line[0]
    score = int(line[1])
    tf = line[2]
    student_tuples.append((name, score, tf))

sorted_students = sorted(student_tuples, key=func1)
for student in sorted_students:
    print(student)